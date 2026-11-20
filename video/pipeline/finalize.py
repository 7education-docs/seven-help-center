#!/usr/bin/env python3
"""Pone a cada vídeo su portada con nombre y ajusta los subtítulos.

Entrada:  video/raw/<pt-br|es>/<archivo>.mp4 y .vtt   (grabación + narración, sin portada)
Salida:   video/review/<pt-br|es>/<archivo>.mp4, .vtt y .jpg (póster)  -> lo lee build-single.mjs

- Portada de 4 s o más (o la duración de la narración del título + 1 s). Marca y subtítulo
  en pantalla, con el estilo de card.mjs.
- pt-BR: la portada se narra con ElevenLabs (voz Mariana M, mismo narrador que el vídeo).
  es: la portada no tiene narración (no hay voz española configurada en el pipeline).
- Subtítulos: se desplazan lo que dura la portada, y la portada tiene su propio subtítulo.
Uso: python3 finalize.py            (procesa los 16 vídeos)
     python3 finalize.py cita:pt-br  (uno solo)
"""
import json
import os
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from narrate import eleven_speech, probe_duration, ELEVEN_VOICE_ES, SPEED_ES  # noqa: E402  (mismo narrador que el resto del pipeline)

ROOT = HERE.parents[1]
TEXTS = json.loads((HERE / "intro-texts.json").read_text(encoding="utf-8"))
BRAND = {"pt": "Seven Assistant", "es": "Seven Assistant"}
MIN_INTRO = 2.5
TIME_RE = re.compile(r"(\d{2}):(\d{2}):(\d{2})\.(\d{3})\s*-->\s*(\d{2}):(\d{2}):(\d{2})\.(\d{3})")
FPS = 30


def run(cmd, **kw):
    subprocess.run(cmd, check=True, **kw)


def ts(sec: float) -> str:
    ms = int(round(sec * 1000))
    h, ms = divmod(ms, 3600_000)
    m, ms = divmod(ms, 60_000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d}.{ms:03d}"


def shift_vtt(raw: str, offset: float, intro_text: str, intro_dur: float) -> str:
    out = ["WEBVTT", "", "0", f"{ts(0.3)} --> {ts(intro_dur - 0.2)}", intro_text, ""]
    body = raw.split("\n", 1)[1] if raw.startswith("WEBVTT") else raw
    n = 1
    for block in re.split(r"\n\s*\n", body.strip()):
        lines = [l for l in block.split("\n") if l.strip()]
        if not lines:
            continue
        m = None
        idx = next((i for i, l in enumerate(lines) if "-->" in l), None)
        if idx is None:
            continue
        m = TIME_RE.search(lines[idx])
        if not m:
            continue
        g = [int(x) for x in m.groups()]
        a = g[0] * 3600 + g[1] * 60 + g[2] + g[3] / 1000 + offset
        b = g[4] * 3600 + g[5] * 60 + g[6] + g[7] / 1000 + offset
        out += [str(n), f"{ts(a)} --> {ts(b)}", *lines[idx + 1:], ""]
        n += 1
    return "\n".join(out) + "\n"



BED = ROOT / "video" / "work" / "music" / "bed-raw.mp3"   # música generada (ElevenLabs), se repite en bucle
FADE_V, FADE_A = 2.5, 2.5


HOLD_END = 1.0   # segundo final con negro, logotipo y música
LOGO_WHITE = ROOT / "video" / "work" / "brand" / "logo-white.png"   # logotipo en blanco para el final en negro


def speech_end(path: pathlib.Path) -> float:
    """Instante en que termina la última locución (el silencio final empieza ahí)."""
    d = probe_duration(path)
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path), "-af",
                        "silencedetect=noise=-35dB:d=0.35", "-f", "null", "-"],
                       capture_output=True, text=True)
    starts = [float(x) for x in re.findall(r"silence_start: ([0-9.]+)", r.stderr)]
    ends = [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", r.stderr)]
    if len(starts) > len(ends):      # el último silencio llega hasta el final del vídeo
        return starts[-1]
    return max(0.0, d - 1.0)


def add_bed(src: pathlib.Path, dst: pathlib.Path, intro_dur: float) -> None:
    """Final: cuando termina de hablar, la imagen y el sonido se funden a negro y aparece el logotipo.
    La música sube solo durante esa transición. Después, HOLD_END segundos más de negro con logotipo y música."""
    se = speech_end(src)
    tr = se + 0.3                                 # pequeño respiro tras la última palabra
    tr_end = tr + FADE_V                          # fin del fundido a negro
    total = tr_end + HOLD_END
    logo_t = tr + 0.2                             # el logotipo entra durante el fundido a negro
    vol = (f"if(lt(t,1),0.12,if(lt(t,3),0.12-0.108*(t-1)/2,if(lt(t,{tr:.3f}),0.012,"
           f"if(lt(t,{tr_end - 0.5:.3f}),0.012+0.688*(t-{tr:.3f})/{FADE_V - 0.5:.3f},0.7))))")
    filt = (f"[0:v]tpad=stop_mode=clone:stop_duration=10,fade=t=out:st={tr:.3f}:d={FADE_V}[vf];"
            f"[2:v]format=rgba,scale=380:-1,fade=t=in:st={logo_t:.3f}:d={FADE_V - 0.7:.3f}:alpha=1[lg];"
            "[vf][lg]overlay=x=(main_w-overlay_w)/2:y=(main_h-overlay_h)/2[v];"
            "[0:a]apad=pad_dur=10[na];"
            f"[1:a]volume='{vol}':eval=frame[mus];"
            "[na][mus]amix=inputs=2:duration=first:normalize=0[mix];"
            f"[mix]afade=t=out:st={total - 1.0:.3f}:d=1.0[a]")
    run(["ffmpeg", "-y", "-v", "error", "-i", str(src), "-stream_loop", "-1", "-i", str(BED),
         "-loop", "1", "-i", str(LOGO_WHITE),
         "-filter_complex", filt, "-map", "[v]", "-map", "[a]", "-t", f"{total:.3f}",
         "-c:v", "libx264", "-preset", "medium", "-crf", "21", "-pix_fmt", "yuv420p", "-r", str(FPS),
         "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", str(dst)])
    print(f"    final: fin de la voz {se:.2f} s · fundido {tr:.2f}–{tr_end:.2f} s · total {total:.2f} s")


def process(file: str, lang: str, dir_key: str) -> None:
    texts = TEXTS[file][lang]
    title, subtitle = texts["title"], texts["subtitle"]
    raw_mp4 = ROOT / "video" / "raw" / dir_key / f"{file}.mp4"
    raw_vtt = ROOT / "video" / "raw" / dir_key / f"{file}.vtt"
    assert raw_mp4.exists() and raw_vtt.exists(), f"falta el vídeo bruto: {raw_mp4}"
    out_dir = ROOT / "video" / "review" / dir_key
    out_dir.mkdir(parents=True, exist_ok=True)
    work = ROOT / "video" / "work" / "intro" / dir_key / file
    work.mkdir(parents=True, exist_ok=True)

    card = work / "card.png"
    run(["node", str(HERE / "card.mjs"), str(card), BRAND[lang], title, subtitle],
        env={**os.environ, "NODE_PATH": os.environ.get("NODE_PATH", "")})

    # introducción hablada en el idioma del vídeo (es: voz española; pt-BR: voz de Mariana M)
    narr_text = texts["narration"]
    mp3, wav = work / f"intro-{lang}.mp3", work / f"intro-{lang}.wav"
    if not wav.exists():  # la narración de la portada no cambia: se reutiliza si ya existe
        eleven_speech(narr_text, mp3, speed=(SPEED_ES if lang == "es" else None),
                      voice=(ELEVEN_VOICE_ES if lang == "es" else None))
        run(["ffmpeg", "-y", "-v", "error", "-i", str(mp3), "-ac", "1", "-ar", "48000", str(wav)])
    intro_dur = round(max(MIN_INTRO, probe_duration(wav) + 0.5), 3)
    audio_in = ["-i", str(wav)]
    audio_chain = f"[1:a]atrim=0:{intro_dur},apad=whole_dur={intro_dur},aformat=sample_rates=48000:channel_layouts=mono[a0];"

    out_mp4 = out_dir / f"{file}.mp4"
    filt = (
        "[0:v]scale=1280:720,setsar=1,fps=30,format=yuv420p[v0];"
        + audio_chain +
        "[2:v]scale=1280:720,setsar=1,fps=30,format=yuv420p[v1];"
        "[2:a]aformat=sample_rates=48000:channel_layouts=mono[a1];"
        "[v0][a0][v1][a1]concat=n=2:v=1:a=1[v][a]"
    )
    tmp_mp4 = work / "concat.mp4"
    run(["ffmpeg", "-y", "-v", "error",
         "-loop", "1", "-t", str(intro_dur), "-i", str(card), *audio_in, "-i", str(raw_mp4),
         "-filter_complex", filt, "-map", "[v]", "-map", "[a]",
         "-c:v", "libx264", "-preset", "medium", "-crf", "21", "-pix_fmt", "yuv420p", "-r", str(FPS),
         "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", str(tmp_mp4)])
    add_bed(tmp_mp4, out_mp4, intro_dur)

    intro_text = narr_text  # el subtítulo de la portada = la narración
    (out_dir / f"{file}.vtt").write_text(
        shift_vtt(raw_vtt.read_text(encoding="utf-8"), intro_dur, intro_text, intro_dur), encoding="utf-8")
    run(["ffmpeg", "-y", "-v", "error", "-i", str(card), "-frames:v", "1", "-q:v", "3", str(out_dir / f"{file}.jpg")])
    dur = probe_duration(out_mp4)
    print(f"✓ {dir_key}/{file} ({lang}): portada {intro_dur:.1f} s · total {dur:.1f} s")


def main() -> None:
    jobs = [(f, "pt", "pt-br") for f in TEXTS] + [(f, "es", "es") for f in TEXTS]
    if len(sys.argv) > 1:
        wanted = set(sys.argv[1:])
        jobs = [j for j in jobs if f"{j[0]}:{j[2]}" in wanted]
    for file, lang, dir_key in jobs:
        process(file, lang, dir_key)


if __name__ == "__main__":
    main()
