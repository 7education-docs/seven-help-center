#!/usr/bin/env bash
# Ensambla el sitio publicado:
#   /index.html                 portada de documentación (single/home.html)
#   /seven-assistant/index.html  helpdesk de Seven Assistant (build + datos publicados en main)
#   /videos, /shots, /assets     medios compartidos (en la raíz)
# Uso: PUBLISHED=<index.html publicado en main> single/assemble-site.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"; cd "$ROOT"
: "${PUBLISHED:?define PUBLISHED con el index.html publicado en main}"
PUBLIC_SITE=1 node single/build-single.mjs >/dev/null
mkdir -p seven-assistant
PUBLISHED="$PUBLISHED" python3 single/merge-published.py site/index.html seven-assistant/index.html >/dev/null
# el helpdesk vive una carpeta más abajo: sus medios están en la raíz
sed -i 's|"videos/|"../videos/|g; s|"shots/|"../shots/|g' seven-assistant/index.html
cp single/home.html index.html
echo "✓ portada: index.html · helpdesk: seven-assistant/index.html ($(wc -c < seven-assistant/index.html) bytes)"
