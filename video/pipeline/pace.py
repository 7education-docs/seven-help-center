#!/usr/bin/env python3
"""Ritmo de los guiones: sin esperas muertas y con más dinamismo.

scale  -> parte de un guion (p. ej. el de la revisión 1161ff9) y:
          - recorta las esperas fijas (x0,55, mínimo 250 ms) y los resaltados (x0,6, mínimo 700 ms);
          - escribe el tecleo más rápido;
          - las esperas largas (≥ 20 s, p. ej. la generación de la IA) pasan a timelapse: "speed": 8.
          --drop id1,id2 quita escenas (p. ej. las que dependen de datos que no hay en la demo).
pad    -> tras una grabación con narración, añade a cada escena solo la espera que falta
          para que la imagen dure lo que la voz (+0,25 s). Las esperas añadidas se marcan con "pad": true
          y se rehacen en cada pasada.

timelapse -> las escenas donde la grabación dura mucho más que la voz (esperas reales de la IA o
          de subida) se aceleran (máx. 8×) hasta durar la voz + 1 s. Se aplica en el timeline y en el guion.

Uso:  pace.py scale <guion.json> [--base-rev 1161ff9] [--drop a,b]
      pace.py pad   <guion.json> <timeline.json> <narration.json>
      pace.py timelapse <guion.json> <timeline.json> <narration.json>
"""
import json
import subprocess
import sys
from pathlib import Path

WAIT_KEEP_MS = 20000  # por encima, es una espera real (IA) y se acelera como timelapse
TIMELAPSE = 8
PAD_EXTRA = 0.25


def scale(path: Path, base_rev: str | None, drop: set[str]) -> None:
    if base_rev:
        raw = subprocess.run(["git", "show", f"{base_rev}:{path.as_posix()}"], check=True, capture_output=True, text=True).stdout
        spec = json.loads(raw)
    else:
        spec = json.loads(path.read_text(encoding="utf-8"))
    spec["scenes"] = [s for s in spec["scenes"] if s["id"] not in drop]
    for sc in spec["scenes"]:
        sc.pop("speed", None)
        acts = [a for a in sc.get("actions", []) if not a.get("pad")]
        for a in acts:
            if a["do"] == "wait":
                if a.get("ms", 0) >= WAIT_KEEP_MS:
                    sc["speed"] = TIMELAPSE
                else:
                    a["ms"] = max(250, round(a["ms"] * 0.55))
            elif a["do"] == "highlight":
                a["ms"] = max(700, round(a.get("ms", 1200) * 0.6))
            elif a["do"] == "type":
                a["delay"] = max(25, round(a.get("delay", 70) * 0.7))
        sc["actions"] = acts
    path.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"✓ ritmo: {path.name} ({len(spec['scenes'])} escenas)")


def pad(path: Path, timeline_path: Path, narration_path: Path) -> None:
    spec = json.loads(path.read_text(encoding="utf-8"))
    tl = json.loads(timeline_path.read_text(encoding="utf-8"))
    nar = json.loads(narration_path.read_text(encoding="utf-8"))["scenes"]
    added = []
    for sc, t, n in zip(spec["scenes"], tl["scenes"], nar):
        sc["actions"] = [a for a in sc.get("actions", []) if not a.get("pad")]
        if sc.get("speed", 1) > 1:
            continue
        rec = (t["endMs"] - t["startMs"]) / 1000
        extra = n["duration"] + PAD_EXTRA - rec
        if extra > 0.3:
            ms = round(extra * 1000)
            sc["actions"].append({"do": "wait", "ms": ms, "pad": True})
            added.append(f'{sc["id"]}+{ms}')
    path.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"✓ pad: {path.name}: " + (", ".join(added) or "sin cambios"))


def timelapse(path: Path, timeline_path: Path, narration_path: Path) -> None:
    spec = json.loads(path.read_text(encoding="utf-8"))
    tl = json.loads(timeline_path.read_text(encoding="utf-8"))
    nar = json.loads(narration_path.read_text(encoding="utf-8"))["scenes"]
    changed = []
    for sc, t, n in zip(spec["scenes"], tl["scenes"], nar):
        rec = (t["endMs"] - t["startMs"]) / 1000
        if rec > max(6.0, 1.8 * n["duration"]):
            sp = min(8.0, round(rec / (n["duration"] + 1.0) * 2) / 2)
            if sp > 1:
                sc["speed"] = sp
                t["speed"] = sp
                changed.append(f'{sc["id"]} x{sp}')
    path.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    timeline_path.write_text(json.dumps(tl, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✓ timelapse: {path.name}: " + (", ".join(changed) or "sin cambios"))


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "scale":
        args = sys.argv[2:]
        base = None
        drop = set()
        if "--base-rev" in args:
            i = args.index("--base-rev"); base = args[i + 1]; del args[i:i + 2]
        if "--drop" in args:
            i = args.index("--drop"); drop = set(args[i + 1].split(",")); del args[i:i + 2]
        scale(Path(args[0]), base, drop)
    elif cmd == "pad":
        pad(Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4]))
    elif cmd == "timelapse":
        timelapse(Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4]))
