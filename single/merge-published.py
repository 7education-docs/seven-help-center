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
    import importlib.util
    spec = importlib.util.spec_from_file_location('faq_overlay', str(pathlib.Path(__file__).resolve().parent / 'faq-overlay.py'))
    faq = importlib.util.module_from_spec(spec); spec.loader.exec_module(faq)
    faq.apply_faq_overlay(merged)
    spec2 = importlib.util.spec_from_file_location('course_overlay', str(pathlib.Path(__file__).resolve().parent / 'course-overlay.py'))
    course = importlib.util.module_from_spec(spec2); spec2.loader.exec_module(course)
    course.apply_course_overlay(merged)
    spec3 = importlib.util.spec_from_file_location('content_expansions', str(pathlib.Path(__file__).resolve().parent / 'content-expansions.py'))
    content = importlib.util.module_from_spec(spec3); spec3.loader.exec_module(content)
    content.apply_content_overlay(merged)
    apply_numbered(merged)
    ser = json.dumps(merged, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    open(out_path, 'w', encoding='utf-8').write(built[:bs] + ser + built[be:])
    print(f'✓ {out_path}: datos de artículos de la versión publicada + plantilla y vídeos nuevos')


SHOTS_NUM = pathlib.Path(__file__).resolve().parent / 'shots-num'
LANG_KEY = {'es': 'es', 'pt-BR': 'pt'}


def load_review() -> dict:
    """key -> pasos (n) que muestra la captura, según la revisión (single/shots-num/review)."""
    out = {}
    for f in (SHOTS_NUM / 'review').glob('result*.json'):
        for it in json.loads(f.read_text(encoding='utf-8')):
            if not it.get('skip') and it.get('steps'):
                out[it['key']] = sorted({st['n'] for st in it['steps']})
    return out


def apply_numbered(merged: dict) -> None:
    """Cambia cada captura por su versión numerada (single/shots-num), donde existe, y
    coloca cada captura dentro del paso que muestra (art.stepImg: {n: clave}).
    Las versiones numeradas se sirven como archivos: shots/<idioma>__<artículo>__<captura>.jpg."""
    review = load_review()
    for loc, lk in LANG_KEY.items():
        n_done = 0
        for art in merged[loc]['articles']:
            keys = []
            for name in art.get('img') or []:
                if '__' in name:  # ya numerada en la versión publicada
                    keys.append(name)
                    continue
                key = f"{lk}__{art['id']}__{name}"
                if (SHOTS_NUM / f"{key}.jpg").exists():
                    merged[loc]['shots'][key] = f"shots/{key}.jpg"
                    merged[loc]['alt'][key] = merged[loc]['alt'].get(name, art.get('title', ''))
                    keys.append(key)
                else:
                    keys.append(name)
            step_img = {}
            # Cada captura va en el paso más alto que muestra y aún no tiene captura (la pantalla
            # muestra el resultado de ese paso). Se procesan primero las de paso más bajo.
            numbered = [k for k in keys if '__' in k and review.get(k)]
            n_done += sum(1 for k in keys if '__' in k)
            for key in sorted(numbered, key=lambda k: max(review[k])):
                for n in sorted(review[key], reverse=True):
                    if str(n) not in step_img:
                        step_img[str(n)] = key
                        break
            art['img'] = keys
            if step_img:
                art['stepImg'] = step_img
            else:
                art.pop('stepImg', None)
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
