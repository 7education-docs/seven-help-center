#!/usr/bin/env bash
# Pipeline completo de una lección: grabación -> narración -> ensamblado -> subtítulos.
# Uso: video/pipeline/run.sh video/scenes/1-1.es.json [carpeta_salida]
# Variables: SEVEN_BASE_URL, SEVEN_USER, SEVEN_PASS (solo para escenas con login)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
SCENES="$1"
OUT_ROOT="${2:-$ROOT/video/out}"
read -r LESSON LOCALE < <(python3 -c "import json,sys; d=json.load(open(sys.argv[1])); print(d['lesson'], d['locale'])" "$SCENES")
KEY="${LESSON/./-}"
SEG=$([ "$LOCALE" = "es" ] && echo es || echo pt-br)
WORK="$ROOT/video/work/$KEY-$LOCALE"
mkdir -p "$WORK" "$OUT_ROOT/$SEG"
echo "→ Grabando $LESSON ($LOCALE)"
WORK_DIR="$WORK" node "$ROOT/video/pipeline/record.mjs" "$SCENES"
echo "→ Narrando"
python3 "$ROOT/video/pipeline/narrate.py" "$WORK/timeline.json" "$WORK/audio"
echo "→ Ensamblando"
python3 "$ROOT/video/pipeline/assemble.py" "$WORK/timeline.json" "$WORK/audio/narration.json" \
  "$WORK/recording.webm" "$OUT_ROOT/$SEG/$KEY.mp4" "$OUT_ROOT/$SEG/$KEY.vtt"
