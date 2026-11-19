#!/usr/bin/env python3
"""Cambia la narración de un vídeo ya grabado (español) por la voz nueva y reajusta la imagen.

Entrada: video/raw/es/<archivo>.mp4 y .vtt (grabación con subtítulos por escena) + guion es (scenes/*.es.json).
Proceso:
  1. Localiza el inicio de cada escena en la grabación (primer subtítulo de su texto).
  2. Genera la narración de cada escena con ElevenLabs (voz ELEVEN_VOICE_ES, ritmo SPEED_ES).
  3. Ajusta cada tramo de imagen a la duración de su voz (acelera o ralentiza, entre ×0,5 y ×2;
     si la voz aún es más larga, se mantiene el último fotograma).
  4. Escribe el vídeo y los subtítulos nuevos en video/work/es-retimed/<archivo>.{mp4,vtt}.
Uso: python3 retime-es.py <archivo> [...]   (p. ej. cita curso-pestanas)
"""
import json
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from narrate import eleven_speech, probe_duration  # noqa: E402
from assemble import cues_for, wrap, LEAD, PAD  # noqa: E402

ROOT = HERE.parents[1]
SCENES = ROOT / 'video' / 'scenes'
RAW = ROOT / 'video' / 'raw' / 'es'
WORK = ROOT / 'video' / 'work' / 'es-retimed'
SPEED_ES = 1.08
MIN_F, MAX_F = 0.5, 2.0
FILE_TO_SCENE = {'C-1': 'curso-pestanas'}  # archivo de salida -> guion


def norm(s: str) -> str:
    return re.sub(r'[^a-záéíóúñü0-9]', '', s.lower())


def ts_to_s(h, m, s, ms):
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000


def read_cues(path: pathlib.Path):
    cues = []
    for block in re.split(r'\n\s*\n', path.read_text(encoding='utf-8').strip()):
        m = re.search(r'(\d\d):(\d\d):(\d\d)\.(\d+)\s*-->\s*(\d\d):(\d\d):(\d\d)\.(\d+)\n(.*)', block, re.S)
        if m:
            g = m.groups()
            cues.append((ts_to_s(*g[0:4]), ts_to_s(*g[4:8]), g[8].strip()))
    return cues


def scene_starts(scenes, cues):
    """Inicio (s) de cada escena: subtítulo cuyo texto empieza como el de la escena."""
    starts, ci = [], 0
    for sc in scenes:
        key = norm(sc['say'])[:18]
        found = None
        for j in range(ci, len(cues)):
            if norm(cues[j][2]).startswith(key):
                found = j
                break
        if found is None:
            raise SystemExit(f"no encuentro en la grabación la escena '{sc['id']}': {sc['say'][:50]}")
        starts.append(max(0.0, cues[found][0] - LEAD))
        ci = found + 1
    return starts


def run(cmd):
    subprocess.run(cmd, check=True)


def process(name: str) -> None:
    key = FILE_TO_SCENE.get(name, name)
    spec = json.loads((SCENES / f'{key}.es.json').read_text(encoding='utf-8'))
    scenes = spec['scenes']
    raw_mp4, raw_vtt = RAW / f'{name}.mp4', RAW / f'{name}.vtt'
    assert raw_mp4.exists() and raw_vtt.exists(), f'falta {raw_mp4}'
    out_name = name
    work = WORK / out_name
    work.mkdir(parents=True, exist_ok=True)
    cues = read_cues(raw_vtt)
    starts = scene_starts(scenes, cues)
    total = probe_duration(raw_mp4)
    ends = starts[1:] + [total]

    segs, sub_cues, offset = [], [], 0.0
    for i, sc in enumerate(scenes):
        mp3, wav = work / f'scene-{i:02d}.mp3', work / f'scene-{i:02d}.wav'
        eleven_speech(sc['say'], mp3, speed=SPEED_ES, voice=VOICE_ES)
        run(['ffmpeg', '-y', '-v', 'error', '-i', str(mp3), '-ac', '1', '-ar', '44100', str(wav)])
        d = probe_duration(wav)
        s, e = starts[i], ends[i]
        vdur = max(0.2, e - s)
        L = d + PAD                                  # duración final de la escena
        f = min(MAX_F, max(MIN_F, L / vdur))         # factor de tiempo de la imagen
        V = vdur * f                                 # duración de la imagen tras el ajuste
        extra = max(0.0, L - V)                      # si la voz aún dura más: último fotograma
        seg = work / f'seg-{i:02d}.mp4'
        vf = (f"[0:v]trim=start={s:.3f}:end={e:.3f},setpts=(PTS-STARTPTS)*{f:.4f},fps=30,"
              f"tpad=stop_mode=clone:stop_duration={extra:.3f}[v]")
        af = f"[1:a]apad=whole_dur={L:.3f},atrim=0:{L:.3f},aresample=44100[a]"
        run(['ffmpeg', '-y', '-v', 'error', '-i', str(raw_mp4), '-i', str(wav),
             '-filter_complex', f"{vf};{af}", '-map', '[v]', '-map', '[a]', '-t', f'{L:.3f}',
             '-c:v', 'libx264', '-preset', 'medium', '-crf', '21', '-pix_fmt', 'yuv420p',
             '-c:a', 'aac', '-b:a', '160k', str(seg)])
        segs.append(seg)
        for a, b, text in cues_for(sc['say'], offset + LEAD, d - LEAD):
            sub_cues.append((a, b, wrap(text)))
        print(f"  {name} · {sc['id']}: voz {d:.1f} s · imagen {vdur:.1f}→{V:.1f} s (×{f:.2f})")
        offset += L

    listf = work / 'concat.txt'
    listf.write_text(''.join(f"file '{p.resolve()}'\n" for p in segs), encoding='utf-8')
    out_mp4 = work / f'{out_name}.mp4'
    run(['ffmpeg', '-y', '-v', 'error', '-f', 'concat', '-safe', '0', '-i', str(listf), '-c', 'copy', str(out_mp4)])
    lines = ['WEBVTT', '']
    for n, (a, b, text) in enumerate(sub_cues, 1):
        lines += [str(n), f'{vtt(a)} --> {vtt(b)}', text, '']
    (work / f'{out_name}.vtt').write_text('\n'.join(lines), encoding='utf-8')
    print(f'✓ {name}: {offset:.1f} s → {out_mp4}')


def vtt(t: float) -> str:
    ms = int(round(t * 1000)); h, ms = divmod(ms, 3600_000); m, ms = divmod(ms, 60_000); s, ms = divmod(ms, 1000)
    return f'{h:02d}:{m:02d}:{s:02d}.{ms:03d}'


if __name__ == '__main__':
    import narrate
    VOICE_ES = narrate.ELEVEN_VOICE_ES
    for n in sys.argv[1:]:
        process(n)
