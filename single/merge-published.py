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
import pathlib
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
    apply_numbered(merged)
    ser = json.dumps(merged, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    open(out_path, 'w', encoding='utf-8').write(built[:bs] + ser + built[be:])
    print(f'✓ {out_path}: datos de artículos de la versión publicada + plantilla y vídeos nuevos')


SHOTS_NUM = pathlib.Path(__file__).resolve().parent / 'shots-num'
LANG_KEY = {'es': 'es', 'pt-BR': 'pt'}


def apply_numbered(merged: dict) -> None:
    """Cambia cada captura por su versión con números de paso (single/shots-num), solo donde existe.
    Las versiones numeradas se sirven como archivos: shots/<idioma>__<artículo>__<captura>.jpg."""
    for loc, lk in LANG_KEY.items():
        n_done = 0
        for art in merged[loc]['articles']:
            new_imgs = []
            for name in art.get('img') or []:
                key = f"{lk}__{art['id']}__{name}"
                if (SHOTS_NUM / f"{key}.jpg").exists():
                    merged[loc]['shots'][key] = f"shots/{key}.jpg"
                    merged[loc]['alt'][key] = merged[loc]['alt'].get(name, art.get('title', ''))
                    new_imgs.append(key)
                    n_done += 1
                else:
                    new_imgs.append(name)
            art['img'] = new_imgs
        print(f'  {loc}: {n_done} capturas numeradas')
    if os.environ.get('COPY_SHOTS'):
        dest = pathlib.Path(os.environ['COPY_SHOTS'])
        dest.mkdir(parents=True, exist_ok=True)
        import shutil
        for f in SHOTS_NUM.glob('*.jpg'):
            shutil.copyfile(f, dest / f.name)
        print(f'  copiadas {len(list(SHOTS_NUM.glob("*.jpg")))} capturas a {dest}')


if __name__ == '__main__':
    main()
