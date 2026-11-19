#!/usr/bin/env python3
"""Genera la narración de cada escena.

- Portugués de Brasil (pt-BR): ElevenLabs, voz "Mariana M" (ELEVEN_VOICE_PT, por defecto
  0t7A9YvHlaUjp3Mon3X1), modelo eleven_multilingual_v2. La API se llama a través del
  proxy del entorno (api.elevenlabs.io); la clave la inyecta el entorno, no va en el repo.
- Español (es): Kokoro (TTS local), voz ef_dora. Requiere models/ (no se versiona).

Uso: python3 narrate.py <timeline.json> <carpeta_audio>
"""
import json
import os
import pathlib
import subprocess
import sys
import urllib.request

MODELS = pathlib.Path(__file__).resolve().parents[1] / "models"
SPEED = 0.90      # Kokoro (español)
SPEED_PT = 1.08   # ElevenLabs (portugués): ritmo ágil, sin pausas muertas

ELEVEN_VOICE_PT = os.environ.get("ELEVEN_VOICE_PT", "0t7A9YvHlaUjp3Mon3X1")  # Mariana M (pt-BR)
ELEVEN_MODEL = "eleven_multilingual_v2"
ELEVEN_URL = "https://api.elevenlabs.io/v1/text-to-speech/{voice}?output_format=mp3_44100_128"


def probe_duration(path: pathlib.Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nw=1:nk=1", str(path)],
        check=True, capture_output=True, text=True,
    ).stdout.strip()
    return float(out)


def eleven_speech(text: str, mp3_path: pathlib.Path) -> None:
    body = json.dumps({
        "text": text,
        "model_id": ELEVEN_MODEL,
        "voice_settings": {"stability": 0.55, "similarity_boost": 0.75, "style": 0.0,
                           "use_speaker_boost": True, "speed": SPEED_PT},
    }).encode("utf-8")
    req = urllib.request.Request(
        ELEVEN_URL.format(voice=ELEVEN_VOICE_PT), data=body, method="POST",
        headers={"Content-Type": "application/json", "Accept": "audio/mpeg"},
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        mp3_path.write_bytes(resp.read())


def narrate_pt(timeline: dict, out: pathlib.Path) -> dict:
    scenes = []
    for i, sc in enumerate(timeline["scenes"]):
        mp3 = out / f"scene-{i:02d}.mp3"
        wav = out / f"scene-{i:02d}.wav"
        eleven_speech(sc["say"], mp3)
        # WAV mono 44,1 kHz: formato que espera assemble.py
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(mp3), "-ac", "1", "-ar", "44100", str(wav)], check=True)
        dur = round(probe_duration(wav), 3)
        scenes.append({"id": sc["id"], "wav": str(wav), "duration": dur})
        print(f"  narración {sc['id']}: {dur:.1f} s (ElevenLabs {ELEVEN_VOICE_PT})")
    return {"provider": "elevenlabs", "voice_id": ELEVEN_VOICE_PT, "model": ELEVEN_MODEL,
            "lang": "pt-BR", "speed": SPEED_PT, "scenes": scenes}


def narrate_es(timeline: dict, out: pathlib.Path) -> dict:
    import soundfile as sf  # importación diferida: solo hace falta para español
    from kokoro_onnx import Kokoro

    lang, voice = "es", "ef_dora"
    kokoro = Kokoro(str(MODELS / "kokoro-v1.0.onnx"), str(MODELS / "voices-v1.0.bin"))
    scenes = []
    for i, sc in enumerate(timeline["scenes"]):
        samples, sr = kokoro.create(sc["say"], voice=voice, speed=SPEED, lang=lang)
        wav = out / f"scene-{i:02d}.wav"
        sf.write(str(wav), samples, sr)
        scenes.append({"id": sc["id"], "wav": str(wav), "duration": round(len(samples) / sr, 3)})
        print(f"  narración {sc['id']}: {len(samples) / sr:.1f} s ({voice})")
    return {"provider": "kokoro", "voice": voice, "lang": lang, "scenes": scenes}


def main(timeline_path: str, out_dir: str) -> None:
    timeline = json.loads(pathlib.Path(timeline_path).read_text(encoding="utf-8"))
    out = pathlib.Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    result = narrate_pt(timeline, out) if timeline["locale"] != "es" else narrate_es(timeline, out)
    (out / "narration.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✓ Narración: {out}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
