#!/usr/bin/env python3
"""Dibuja los números de paso sobre cada captura que muestra un paso real.

Entrada: scratchpad de revisión result1..4.json (una entrada por par artículo × captura, con
         "skip" y "steps": [{"n", "x", "y"}] en píxeles de la imagen original).
Salida:  single/shots-num/<idioma>__<artículo>__<captura>.jpg (idioma: es | pt)

Uso: python3 single/number-shots.py <carpeta con result1..4.json>
"""
import json
import pathlib
import sys
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parents[1]
SHOTS = ROOT / 'single' / 'shots'
OUT = ROOT / 'single' / 'shots-num'
PINK = (230, 51, 110)
WHITE = (255, 255, 255)


def font(size: int):
    for cand in ['/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
                 '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf']:
        if pathlib.Path(cand).exists():
            return ImageFont.truetype(cand, size)
    return ImageFont.load_default()


def main(result_dir: str) -> None:
    pairs = []
    for i in range(1, 5):
        p = pathlib.Path(result_dir) / f'result{i}.json'
        if p.exists():
            pairs += json.loads(p.read_text(encoding='utf-8'))
    OUT.mkdir(parents=True, exist_ok=True)
    stats = {'badged': 0, 'skipped': 0, 'missing': 0}
    for item in pairs:
        key = item['key']
        if item.get('skip') or not item.get('steps'):
            stats['skipped'] += 1
            continue
        lang, article, name = key.split('__', 2)
        src = SHOTS / f'{name}.jpg'
        if not src.exists():
            stats['missing'] += 1
            continue
        img = Image.open(src).convert('RGB')
        d = ImageDraw.Draw(img)
        w, h = img.size
        r = max(14, round(w * 0.016))
        f = font(round(r * 1.15))
        for s in item['steps']:
            x = min(max(int(s['x']), r + 2), w - r - 2)
            y = min(max(int(s['y']), r + 2), h - r - 2)
            d.ellipse([x - r - 2, y - r - 2, x + r + 2, y + r + 2], fill=WHITE)
            d.ellipse([x - r, y - r, x + r, y + r], fill=PINK)
            txt = str(s['n'])
            d.text((x, y), txt, fill=WHITE, font=f, anchor='mm')
        img.save(OUT / f'{key}.jpg', quality=90)
        stats['badged'] += 1
    print(stats)


if __name__ == '__main__':
    main(sys.argv[1])
