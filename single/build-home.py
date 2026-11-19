#!/usr/bin/env python3
"""Genera la portada de documentación en español (index.html) y en portugués (pt-br/index.html).

Los estilos salen de single/home.html (bloque <style>); el resto se genera aquí, para que las dos
versiones no se desalineen. Uso: python3 single/build-home.py
"""
import html as H
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = (ROOT / 'single' / 'home.html').read_text(encoding='utf-8')
TPL = (ROOT / 'single' / 'template.html').read_text(encoding='utf-8')
CSS = re.search(r'<style>(.*?)</style>', SRC, re.S).group(1)
# selector de idioma: mismo CSS que el helpdesk
LANG_CSS = TPL[TPL.index('.lang-menu{'):TPL.index('[aria-current="true"]{background:var(--tint);color:var(--primary)}') + len('[aria-current="true"]{background:var(--tint);color:var(--primary)}')]
BASE = 'https://www.7education.com/'
GLOBE = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">'
         '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.7 3.8 5.7 3.8 9s-1.3 6.3-3.8 9c-2.5-2.7-3.8-5.7-3.8-9S9.5 5.7 12 3z"/></svg>')
LI = '<svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9.75h4V21H3zM9.5 9.75h3.8v1.6h.05c.53-1 1.83-2.05 3.77-2.05 4.03 0 4.78 2.65 4.78 6.1V21h-4v-4.9c0-1.17-.02-2.68-1.63-2.68-1.64 0-1.89 1.28-1.89 2.6V21h-4z"/></svg>'
IG = '<svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>'

# enlaces del pie: los mismos de la web de referencia
LINKS = {
 'Autoridades de escuelas': 'a-quienes-apoyamos/autoridades', 'Escuelas de primaria': 'a-quienes-apoyamos/escuelas-de-primaria',
 'Escuelas de secundaria': 'a-quienes-apoyamos/escuelas-de-secundaria', 'Educación especial': 'a-quienes-apoyamos/escuelas-de-educacion-especial',
 'Escuelas de infantil': 'a-quienes-apoyamos/escuelas-de-infantil', 'Visión general': 'soluciones/vision-general',
 'Comunicación escolar': 'soluciones/comunicacion-escolar', 'Gestión del aula': 'soluciones/gestion-del-aula',
 'Gestión del aprendizaje': 'soluciones/gestion-del-aprendizaje', 'Administración del centro': 'soluciones/administracion-del-centro',
 'Funcionalidades IA': 'soluciones/funcionalidades-ia', 'Seven Blog': 'blog', 'Webinars y eventos': 'recursos/eventos',
 'Sobre nosotros': 'sobre-nosotros', 'Únete al equipo': 'equipo', 'Noticias y prensa': 'noticias',
 'Privacidad': 'politica-de-privacidad', 'Aviso legal': 'aviso-legal',
}
COLS = {
 'es': [('A quién apoyamos', ['Autoridades de escuelas', 'Escuelas de primaria', 'Escuelas de secundaria', 'Educación especial', 'Escuelas de infantil']),
        ('Soluciones', ['Visión general', 'Comunicación escolar', 'Gestión del aula', 'Gestión del aprendizaje', 'Administración del centro', 'Funcionalidades IA']),
        ('Recursos', ['Seven Blog', 'Webinars y eventos']),
        ('Sobre nosotros', ['Sobre nosotros', 'Únete al equipo', 'Noticias y prensa']),
        ('Legal', ['Privacidad', 'Aviso legal', None])],
 'pt': [('A quem apoiamos', ['Autoridades de escolas', 'Escolas de ensino fundamental', 'Escolas de ensino médio', 'Educação especial', 'Escolas de educação infantil']),
        ('Soluções', ['Visão geral', 'Comunicação escolar', 'Gestão da sala de aula', 'Gestão da aprendizagem', 'Administração da escola', 'Funcionalidades de IA']),
        ('Recursos', ['Blog da Seven', 'Webinars e eventos']),
        ('Sobre nós', ['Sobre nós', 'Junte-se à equipe', 'Notícias e imprensa']),
        ('Legal', ['Privacidade', 'Aviso legal', None])],
}
# mismo orden de enlaces que COLS['es'] para ambos idiomas
ES_KEYS = [t for _, items in COLS['es'] for t in items if t]
PT_TO_KEY = dict(zip([t for _, items in COLS['pt'] for t in items if t], ES_KEYS))

T = {
 'es': dict(lang='es', title='Help Center · Seven Education', kicker='Documentación de Seven Education', h1='Help Center',
            lead='Elige el producto para encontrar guías, vídeos y respuestas a las dudas más habituales.',
            country_all='Todos los países', cta='Abrir centro de ayuda →', soon='Próximamente', soon_h='Próximamente',
            sa_desc='Guías de inicio, cursos, conversaciones, documentos, series de lecciones, fichas, tareas de corrección y configuración.',
            ed={'Brasil': 'Centro de ayuda de Educamos en Brasil.', 'Argentina': 'Centro de ayuda de Educamos en Argentina.',
                'Chile': 'Centro de ayuda de Educamos en Chile.', 'México': 'Centro de ayuda de Educamos en México.'},
            countries={'Brasil': 'Brasil', 'Argentina': 'Argentina', 'Chile': 'Chile', 'México': 'México'},
            sa_url='seven-assistant/', copy='Copyright © Seven Education 2026', prefix='', other_url='pt-br/', other_label='Português',
            here_label='Español', back_root_label='Knowledge Hub', sa_label='Seven Assistant', aria_lang='Idioma', home_label='Seven Education'),
 'pt': dict(lang='pt-BR', title='Help Center · Seven Education', kicker='Documentação da Seven Education', h1='Help Center',
            lead='Escolha o produto para encontrar guias, vídeos e respostas para as dúvidas mais comuns.',
            country_all='Todos os países', cta='Abrir centro de ajuda →', soon='Em breve', soon_h='Em breve',
            sa_desc='Guias de início, cursos, conversas, documentos, séries de aulas, fichas, tarefas de correção e configurações.',
            ed={'Brasil': 'Centro de ajuda da Educamos no Brasil.', 'Argentina': 'Centro de ajuda da Educamos na Argentina.',
                'Chile': 'Centro de ajuda da Educamos no Chile.', 'México': 'Centro de ajuda da Educamos no México.'},
            countries={'Brasil': 'Brasil', 'Argentina': 'Argentina', 'Chile': 'Chile', 'México': 'México'},
            sa_url='../seven-assistant/#pt-br-home', copy='Copyright © Seven Education 2026', prefix='../', other_url='../', other_label='Español',
            here_label='Português', back_root_label='Knowledge Hub', sa_label='Seven Assistant', aria_lang='Idioma', home_label='Seven Education'),
}
PRODUCTS = [
 ('Seven Assistant', None, 'sa'),
 ('Educamos Brasil', 'Brasil', 'ed'), ('Educamos Argentina', 'Argentina', 'ed'),
 ('Educamos Chile', 'Chile', 'ed'), ('Educamos México', 'México', 'ed'),
]

def footer(lang):
    cols = COLS[lang]
    heads = ''
    for h, items in cols:
        lis = ''
        for t in items:
            if t is None:
                lis += '<li><button type="button" class="f-cookies">Cookies</button></li>'
            else:
                key = t if lang == 'es' else PT_TO_KEY[t]
                lis += f'<li><a href="{BASE}{LINKS[key]}">{H.escape(t)}</a></li>'
        heads += f'<div class="f-col"><h3 class="f-h">{H.escape(h)}</h3><ul>{lis}</ul></div>'
    return ('<footer class="site-footer"><div class="f-inner"><div class="f-grid">'
            f'<div class="f-brand"><a href="{BASE}" aria-label="Seven Education"><img class="f-logo" src="{{LOGO}}" alt="Seven Education"></a>'
            f'<div class="f-social"><a href="https://www.linkedin.com/company/7education/" rel="noopener" aria-label="LinkedIn">{LI}</a>'
            f'<a href="https://instagram.com/seveneducation.es" rel="noopener" aria-label="Instagram">{IG}</a></div>'
            f'<p class="f-copy">{H.escape(T[lang]["copy"])}</p></div>' + heads + '</div></div></footer>')

def page(lang):
    t = T[lang]; p = t['prefix']
    css = CSS.replace("url('assets/", f"url('{p}assets/") + LANG_CSS
    lang_menu = ('<details class="lang-menu"><summary aria-label="' + H.escape(t['aria_lang']) + '">' + GLOBE + f'<span>{t["here_label"]}</span></summary><ul>'
                 + (f'<li><a href="./" lang="es"{" aria-current=\"true\"" if lang == "es" else ""}>Español</a></li>'
                    if lang == 'es' else '<li><a href="../" lang="es">Español</a></li>')
                 + (f'<li><a href="pt-br/" lang="pt-BR">Português</a></li>' if lang == 'es'
                    else f'<li><a href="./" lang="pt-BR" aria-current="true">Português</a></li>')
                 + '</ul></details>')
    cards = ''
    live = [n for n, c, k in PRODUCTS if k == 'sa']
    feature = True
    cards += (f'<a class="prod prod-feature" href="{t["sa_url"]}"><span class="country">{H.escape(t["country_all"])}</span>'
              f'<h2>Seven Assistant</h2><p>{H.escape(t["sa_desc"])}</p><span class="foot">{H.escape(t["cta"])}</span></a>')
    soon = ''
    for name, country, kind in PRODUCTS[1:]:
        c = t['countries'][country]
        soon += (f'<article class="prod is-soon" aria-label="{H.escape(name)}, {H.escape(t["soon"].lower())}"><span class="country">{H.escape(c)}</span>'
                 f'<h2>{H.escape(name)}</h2><p>{H.escape(t["ed"][country])}</p><span class="chip">{H.escape(t["soon"])}</span></article>')
    cards += f'<h2 class="soon-h">{H.escape(t["soon_h"])}</h2><div class="grid-soon">{soon}</div>'
    return f'''<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{H.escape(t['title'])}</title>
<meta name="description" content="{H.escape(t['lead'])}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap">
<style>{css}</style>
</head>
<body>
<header class="top"><div class="wrap top-row">
  <a class="brand" href="./"><img src="{p}assets/logo-seven-education.png" alt="Seven Education" height="40"></a>
  <div class="top-right"><span class="top-nav">{H.escape(t['back_root_label'])}</span>{lang_menu}</div>
</div></header>

<main class="wrap" style="padding-top:0">
  <section class="band" aria-labelledby="t"><div class="band-in">
    <p class="kicker">{H.escape(t['kicker'])}</p>
    <h1 id="t">{H.escape(t['h1'])}</h1>
    <p class="lead">{H.escape(t['lead'])}</p>
  </div></section>
  <section aria-label="{H.escape('Productos' if lang == 'es' else 'Produtos')}">
    <div class="grid" id="products">{cards}</div>
  </section>
</main>

{footer(lang).replace('{LOGO}', p + 'assets/logo-seven-education-footer.png')}
</body>
</html>
'''

if __name__ == '__main__':
    (ROOT / 'index.html').write_text(page('es'), encoding='utf-8')
    (ROOT / 'pt-br').mkdir(exist_ok=True)
    (ROOT / 'pt-br' / 'index.html').write_text(page('pt'), encoding='utf-8')
    print('✓ index.html (es) · pt-br/index.html (pt)')
