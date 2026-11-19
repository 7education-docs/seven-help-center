#!/usr/bin/env python3
"""Fusiona la página generada con los datos ya publicados en main.

Uso: git show origin/main:index.html > /tmp/published.html
     PUBLISHED=/tmp/published.html python3 single/merge-published.py site/index.html index.html

Motivo: algunos cambios de contenido (capturas de artículos, shots) se hicieron directamente
en el index.html publicado y no están en los fuentes. Se toman de la versión publicada;
la plantilla, los textos de interfaz (ui) y los vídeos (portada, póster, subtítulos, duración)
se toman de la generación nueva.
"""
import json
import os
import sys

MARK = '{"es":{"updated"'


def split(text):
    s = text.find(MARK)
    if s < 0:
        raise SystemExit('no se encuentra el bloque de datos en el HTML')
    data, end = json.JSONDecoder().raw_decode(text, s)
    return s, data, end


def main() -> None:
    built_path, out_path = sys.argv[1], sys.argv[2]
    published = open(os.environ['PUBLISHED'], encoding='utf-8').read()
    built = open(built_path, encoding='utf-8').read()
    ps, pdata, _ = split(published)
    bs, bdata, be = split(built)
    merged = json.loads(json.dumps(pdata))
    for loc in ('es', 'pt-BR'):
        merged[loc]['ui'] = bdata[loc]['ui']
        merged[loc]['videos'] = bdata[loc]['videos']
    ser = json.dumps(merged, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    open(out_path, 'w', encoding='utf-8').write(built[:bs] + ser + built[be:])
    print(f'✓ {out_path}: datos de artículos de la versión publicada + plantilla y vídeos nuevos')


if __name__ == '__main__':
    main()
