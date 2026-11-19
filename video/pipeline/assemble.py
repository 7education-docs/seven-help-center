#!/usr/bin/env python3
"""Ensambla la lección: recorta cada escena, la alarga si la narración es más larga, mezcla
la narración y genera subtítulos WebVTT (máx. 2 líneas de 42 caracteres, activables en el reproductor).
Uso: python3 assemble.py <timeline.json> <narration.json> <recording.webm> <salida.mp4> <salida.vtt>
"""
import json
import math
import pathlib
import re
import shutil
import subprocess
import sys
import textwrap

FPS = 30
PAD = 0.25          # silencio tras cada narración
LEAD = 0.15        # el subtítulo aparece justo antes de que empiece la voz
MIN_CUE = 1.6      # duración mínima de un subtítulo (lectura cómoda)
MAX_CHARS = 42


def run(cmd):
    subprocess.run(cmd, check=True)


def probe_duration(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(path)],
        check=True, capture_output=True, text=True,
    )
    return float(out.stdout.strip())


def vtt_time(t):
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    return f"{int(h):02d}:{int(m):02d}:{s:06.3f}"


def wrap(text):
    lines = textwrap.wrap(text, width=MAX_CHARS, break_long_words=False)
    if len(lines) > 2:  # reparto en dos líneas equilibradas
        half = math.ceil(len(lines) / 2)
        lines = [" ".join(lines[:half]), " ".join(lines[half:])]
    return "\n".join(lines)


def sentences(text):
    return [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s]


def cues_for(text, start, duration):
    """Reparte la duración de la escena entre frases; une frases demasiado cortas."""
    parts = sentences(text) or [text]
    total = sum(len(p) for p in parts) or 1
    raw, t = [], start
    for p in parts:
        d = duration * len(p) / total
        raw.append([t, t + d, p])
        t += d
    merged = []
    for c in raw:
        if merged and (merged[-1][1] - merged[-1][0]) < MIN_CUE:
            merged[-1][1] = c[1]
            merged[-1][2] += " " + c[2]
        else:
            merged.append(c)
    if len(merged) > 1 and (merged[-1][1] - merged[-1][0]) < MIN_CUE:
        merged[-2][1] = merged[-1][1]
        merged[-2][2] += " " + merged[-1][2]
        merged.pop()
    return merged


def main(timeline_path, narration_path, recording, out_mp4, out_vtt):
    timeline = json.loads(pathlib.Path(timeline_path).read_text(encoding="utf-8"))
    narration = json.loads(pathlib.Path(narration_path).read_text(encoding="utf-8"))
    out_mp4, out_vtt = pathlib.Path(out_mp4), pathlib.Path(out_vtt)
    out_mp4.parent.mkdir(parents=True, exist_ok=True)
    seg_dir = out_mp4.parent / f".segments-{out_mp4.stem}"
    shutil.rmtree(seg_dir, ignore_errors=True)
    seg_dir.mkdir(parents=True)
    rec_dur = probe_duration(recording)

    segs, cues, offset = [], [], 0.0
    for i, (sc, nar) in enumerate(zip(timeline["scenes"], narration["scenes"])):
        assert sc["id"] == nar["id"], "escenas desalineadas entre guion y narración"
        s = min(sc["startMs"] / 1000, rec_dur - 0.1)
        e = min(max(sc["endMs"] / 1000, s + 0.2), rec_dur - 0.05)
        speed = float(sc.get("speed", 1) or 1)   # >1: timelapse (p. ej. generación de la IA)
        vdur = (e - s) / speed
        T = max(vdur, nar["duration"] + PAD)          # duración final de la escena
        extra = max(0.0, T - vdur)                   # se mantiene el último fotograma
        seg = seg_dir / f"seg-{i:02d}.mp4"
        vf = (f"[0:v]trim=start={s:.3f}:end={e:.3f},setpts=(PTS-STARTPTS)/{speed},fps={FPS},"
              f"scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2,"
              f"tpad=stop_mode=clone:stop_duration={extra:.3f}[v]")
        af = f"[1:a]equalizer=f=180:t=h:w=160:g=2.5,equalizer=f=3200:t=q:w=1.2:g=-2,acompressor=threshold=-20dB:ratio=2.2:attack=15:release=180,apad=whole_dur={T:.3f},atrim=0:{T:.3f},aresample=48000[a]"
        run(["ffmpeg", "-y", "-v", "error", "-i", str(recording), "-i", nar["wav"],
             "-filter_complex", f"{vf};{af}", "-map", "[v]", "-map", "[a]", "-t", f"{T:.3f}",
             "-c:v", "libx264", "-preset", "medium", "-crf", "21", "-pix_fmt", "yuv420p",
             "-c:a", "aac", "-b:a", "160k", str(seg)])
        segs.append(seg)
        for c_start, c_end, c_text in cues_for(sc["say"], offset + LEAD, nar["duration"] - LEAD):
            cues.append((c_start, c_end, wrap(c_text)))
        offset += T
        print(f"  escena {sc['id']}: {T:.1f} s")

    listing = seg_dir / "list.txt"
    listing.write_text("".join(f"file '{p.name}'\n" for p in segs), encoding="utf-8")
    run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(listing),
         "-c", "copy", "-movflags", "+faststart", str(out_mp4)])
    shutil.rmtree(seg_dir, ignore_errors=True)

    lines = ["WEBVTT", ""]
    for n, (a, b, text) in enumerate(cues, 1):
        lines += [str(n), f"{vtt_time(a)} --> {vtt_time(b)}", text, ""]
    out_vtt.write_text("\n".join(lines), encoding="utf-8")
    print(f"✓ Video: {out_mp4} ({offset:.1f} s, {len(cues)} subtítulos)")


if __name__ == "__main__":
    main(*sys.argv[1:6])
