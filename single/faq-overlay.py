#!/usr/bin/env python3
"""Reestructura el centro de ayuda: artículos de una sola cosa y preguntas frecuentes aparte.

- "Qué es Seven Assistant" absorbe "Moverte por la barra lateral" (un único artículo).
- Las preguntas que solo resuelven un problema pasan a la categoría "Preguntas frecuentes" (FAQ).
- Cada artículo muestra sus FAQ relacionadas con enlace directo (FAQ_LINKS + las que ya estaban relacionadas).
Se aplica sobre los datos publicados (merge-published.py). Las capturas de la barra lateral se pintan
con los números del nuevo artículo: ver faq-prepare.py.
"""
import copy

FAQ_IDS = ['no-encuentro-seccion', 'no-puedo-acceder', 'beta', 'idioma-no-cambia',
           'alumnado-no-entra', 'codigo-filtrado', 'respuesta-no-correcta', 'plantillas-vs-asistentes']
FAQ_LINKS = {
    'que-es': ['no-puedo-acceder', 'no-encuentro-seccion'],
    'idioma': ['idioma-no-cambia'],
    'unirse-curso': ['no-puedo-acceder', 'alumnado-no-entra'],
    'invitar-alumnado': ['alumnado-no-entra', 'codigo-filtrado'],
    'hacer-pregunta': ['respuesta-no-correcta'],
    'regenerar-respuesta': ['respuesta-no-correcta'],
    'crear-curso': ['beta'],
    'menu-de-cuenta': ['no-encuentro-seccion'],
    'configuracion-del-curso': ['codigo-filtrado'],
    'crear-asistente': ['plantillas-vs-asistentes'],
    'plantillas-de-curso': ['plantillas-vs-asistentes'],
    'plantilla-nombrar': ['plantillas-vs-asistentes'],
}
MERGED = {'que-es': 'barra-lateral'}   # id que absorbe -> id que desaparece
TITLES = {'es': 'Qué es Seven Assistant y cómo moverte por la barra lateral',
          'pt-BR': 'O que é o Seven Assistant e como se mover pela barra lateral'}
FAQ_CAT = {'es': {'id': 'faq', 'name': 'Preguntas frecuentes', 'desc': 'Respuestas rápidas a los problemas más habituales.'},
           'pt-BR': {'id': 'faq', 'name': 'Perguntas frequentes', 'desc': 'Respostas rápidas para os problemas mais comuns.'}}


def apply_faq_overlay(merged: dict) -> None:
    for loc in ('es', 'pt-BR'):
        d = merged[loc]
        arts = {a['id']: a for a in d['articles']}
        # 1) un único artículo: "Qué es" + "barra lateral"
        for keep, gone in MERGED.items():
            if keep in arts and gone in arts:
                qa, bl = arts[keep], arts[gone]
                offset = len(qa.get('steps') or [])
                qa['steps'] = (qa.get('steps') or []) + (bl.get('steps') or [])
                qa['tips'] = (qa.get('tips') or []) + (bl.get('tips') or [])
                # nombres base de las capturas (sin la clave del artículo): la fusión las numera para el nuevo artículo
                qa['img'] = [n.split('__')[-1] for n in (bl.get('img') or [])]
                qa['stepOffset'] = offset                   # numeración de la barra lateral en el nuevo artículo
                qa['title'] = TITLES[loc]
                rel = (qa.get('related') or []) + (bl.get('related') or [])
                qa['related'] = list(dict.fromkeys(r for r in rel if r not in (keep, gone)))
                d['articles'] = [a for a in d['articles'] if a['id'] != gone]
                arts.pop(gone)
                d.setdefault('aliases', {})[gone] = keep
        # 2) preguntas frecuentes
        if not any(c['id'] == 'faq' for c in d['categories']):
            d['categories'].append(dict(FAQ_CAT[loc]))
        for a in d['articles']:
            if a['id'] in FAQ_IDS:
                a['cat'] = 'faq'
        # 3) enlaces desde cada artículo a sus FAQ relacionadas
        for a in d['articles']:
            rel = a.get('related') or []
            # idempotente: se conservan las FAQ ya enlazadas y se añaden las de la tabla
            faq_rel = (a.get('faqRelated') or []) + [r for r in rel if r in FAQ_IDS] + [r for r in FAQ_LINKS.get(a['id'], []) if r in arts]
            a['related'] = [r for r in rel if r not in FAQ_IDS]
            a['faqRelated'] = list(dict.fromkeys(faq_rel))
            if not a['faqRelated']:
                a.pop('faqRelated', None)
    print('  faq overlay: es', sum(1 for a in merged['es']['articles'] if a.get('cat') == 'faq'), 'FAQ |',
          'pt', sum(1 for a in merged['pt-BR']['articles'] if a.get('cat') == 'faq'), 'FAQ')
