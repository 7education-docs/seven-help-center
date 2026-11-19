#!/usr/bin/env python3
"""Genera la narración de cada escena con Kokoro (TTS neuronal local, sin servicios externos).
Voces femeninas: ef_dora (español) y pf_dora (portugués de Brasil).
Uso: python3 narrate.py <timeline.json> <carpeta_audio>
"""
import json
import pathlib
import sys

import soundfile as sf
from kokoro_onnx import Kokoro

MODELS = pathlib.Path(__file__).resolve().parents[1] / "models"
VOICE = {"es": ("es", "ef_dora"), "pt": ("pt-br", "pf_dora")}
SPEED = 0.90  # ritmo más pausado y cálido para tono de vídeo comercial


def main(timeline_path: str, out_dir: str) -> None:
    timeline = json.loads(pathlib.Path(timeline_path).read_text(encoding="utf-8"))
    key = "es" if timeline["locale"] == "es" else "pt"
    lang, voice = VOICE[key]
    kokoro = Kokoro(str(MODELS / "kokoro-v1.0.onnx"), str(MODELS / "voices-v1.0.bin"))
    out = pathlib.Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    scenes = []
    for i, sc in enumerate(timeline["scenes"]):
        samples, sr = kokoro.create(sc["say"], voice=voice, speed=SPEED, lang=lang)
        wav = out / f"scene-{i:02d}.wav"
        sf.write(str(wav), samples, sr)
        scenes.append({"id": sc["id"], "wav": str(wav), "duration": round(len(samples) / sr, 3)})
        print(f"  narración {sc['id']}: {len(samples) / sr:.1f} s ({voice})")
    (out / "narration.json").write_text(
        json.dumps({"voice": voice, "lang": lang, "scenes": scenes}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"✓ Narración: {out}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
