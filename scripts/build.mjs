// Generador estático del centro de ayuda Seven Assistant (sin dependencias).
// Uso: node scripts/build.mjs            -> genera dist/ayuda/...  (HELP_BASE=/ayuda por defecto)
//      HELP_BASE= node scripts/build.mjs  -> genera dist/... para servir en local desde la raíz
import { mkdir, writeFile, rm, cp, readdir, access } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { SITE } from '../content/config.mjs';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const BASE = SITE.basePath.replace(/\/$/, '');
const OUT = path.join(ROOT, 'dist', BASE);
const VIDEO_OUT = path.join(ROOT, 'video', 'out');

const load = async (rel) => (await import(pathToFileURL(path.join(ROOT, rel)).href)).default;
const CONTENT = { es: await load('content/es.mjs'), 'pt-BR': await load('content/pt-BR.mjs') };
// Cursos, roles y secciones de la nueva estructura (content/cursos-*.mjs) sustituyen a los campos base.
const COURSES = { es: await load('content/cursos-es.mjs'), 'pt-BR': await load('content/cursos-pt-BR.mjs') };
for (const loc of ['es', 'pt-BR']) Object.assign(CONTENT[loc], { courses: COURSES[loc].courses, roles: COURSES[loc].roles, sections: COURSES[loc].sections });
const LABELS = await load('content/labels.mjs');

const LOCALES = ['es', 'pt-BR'];
const SEG = { es: 'es', 'pt-BR': 'pt-br' };
const FONT_STACK = "Inter, ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif";

// Segmentos de URL localizados (la estructura de IDs es común).
const PATHS = {
  es: {
    courses: 'cursos', sections: 'secciones', routes: 'rutas', countries: 'paises',
    faq: 'preguntas-frecuentes', search: 'buscar',
    section: { cursos: 'cursos', conversaciones: 'conversaciones', documentos: 'documentos', 'series-de-lecciones': 'series-de-lecciones', 'tareas-de-correccion': 'tareas-de-correccion', 'fichas-interactivas': 'fichas-interactivas', plantillas: 'plantillas', configuracion: 'configuracion' },
  },
  'pt-BR': {
    courses: 'cursos', sections: 'secoes', routes: 'trilhas', countries: 'paises-e-escalas',
    faq: 'perguntas-frequentes', search: 'busca',
    section: { cursos: 'cursos', conversaciones: 'conversas', documentos: 'documentos', 'series-de-lecciones': 'series-de-aulas', 'tareas-de-correccion': 'tarefas-de-correcao', 'fichas-interactivas': 'fichas-interativas', plantillas: 'modelos', configuracion: 'configuracoes' },
  },
};

const esc = (s) => String(s ?? '').replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const t = (loc) => ({ ...LABELS[loc], ...CONTENT[loc].ui });
// URL relativa al dominio, con barra final: urlFor('es','cursos','x') -> /ayuda/es/cursos/x/
const urlFor = (loc, ...segs) => `${BASE}/${SEG[loc]}/${segs.filter(Boolean).map((s) => `${s}/`).join('')}`;
const absUrl = (u) => `${SITE.origin}${u}`;
const lessonKey = (id) => id.replace('.', '-');
const lessonVideoRel = (loc, id) => `videos/${SEG[loc]}/${lessonKey(id)}`;

// -------- Validación: paridad entre idiomas y coherencia de referencias --------
function validate() {
  const errors = [];
  const es = CONTENT.es;
  const pt = CONTENT['pt-BR'];
  const ids = (c) => c.courses.map((co) => co.id);
  if (JSON.stringify(ids(es)) !== JSON.stringify(ids(pt))) errors.push('Paridad: IDs de cursos distintos o en otro orden.');
  if (JSON.stringify(ids(es)) !== JSON.stringify(SITE.courseIds)) errors.push('config.courseIds no coincide con content.');
  if (es.courses.length !== 6) errors.push('Se esperaban 6 cursos.');
  for (const loc of LOCALES) {
    const c = CONTENT[loc];
    const lessonIds = c.courses.flatMap((co) => co.lessons.map((l) => l.id));
    const slugs = [...c.courses.map((co) => co.slug), ...c.courses.flatMap((co) => co.lessons.map((l) => l.slug))];
    if (new Set(slugs).size !== slugs.length) errors.push(`${loc}: slugs duplicados.`);
    if (new Set(lessonIds).size !== lessonIds.length) errors.push(`${loc}: IDs de lección duplicados.`);
    for (const co of c.courses) {
      if (!co.roles?.every((r) => SITE.roleIds.includes(r))) errors.push(`${loc}/${co.id}: rol desconocido.`);
      co.lessons.forEach((l) => {
        if (!l.steps?.length) errors.push(`${loc}/${l.id}: sin pasos.`);
        if (!l.quiz?.length) errors.push(`${loc}/${l.id}: sin preguntas de repaso.`);
        l.quiz?.forEach((q, i) => {
          if (!(q.answer >= 0 && q.answer < q.options.length)) errors.push(`${loc}/${l.id}: respuesta fuera de rango en pregunta ${i + 1}.`);
        });
      });
    }
    for (const id of SITE.sectionIds) {
      if (!c.sections[id]) errors.push(`${loc}: falta la sección ${id}.`);
      (c.sections[id]?.lessons ?? []).forEach((lid) => { if (!lessonIds.includes(lid)) errors.push(`${loc}/sección ${id}: lección ${lid} inexistente.`); });
      if (!PATHS[loc].section[id]) errors.push(`${loc}: sin slug de sección para ${id}.`);
    }
    for (const id of SITE.roleIds) {
      if (!c.roles[id]) errors.push(`${loc}: falta el rol ${id}.`);
      (c.roles[id]?.lessons ?? []).forEach((lid) => { if (!lessonIds.includes(lid)) errors.push(`${loc}/rol ${id}: lección ${lid} inexistente.`); });
    }
    if (c.countries.length !== 3) errors.push(`${loc}: se esperan 3 países.`);
  }
  // Paridad de lecciones (IDs y número de pasos/preguntas)
  const shape = (c) => c.courses.flatMap((co) => co.lessons.map((l) => `${l.id}:${l.steps.length}:${l.quiz.length}:${l.quiz.map((q) => q.answer).join('')}`));
  if (JSON.stringify(shape(es)) !== JSON.stringify(shape(pt))) errors.push('Paridad: estructura de lecciones distinta entre idiomas (pasos, preguntas o respuestas).');
  if (errors.length) {
    console.error(errors.map((e) => `  ✗ ${e}`).join('\n'));
    throw new Error(`Validación fallida (${errors.length} error/es).`);
  }
}

// -------- Índices de navegación --------
function indexFor(loc) {
  const c = CONTENT[loc];
  const lessons = c.courses.flatMap((co) => co.lessons.map((l, i) => ({ ...l, course: co, index: i })));
  const byId = Object.fromEntries(lessons.map((l) => [l.id, l]));
  return {
    byId,
    courseUrl: (co) => urlFor(loc, PATHS[loc].courses, co.slug),
    lessonUrl: (co, l) => urlFor(loc, PATHS[loc].courses, co.slug, l.slug),
    sectionUrl: (id) => urlFor(loc, PATHS[loc].sections, PATHS[loc].section[id]),
    homeUrl: () => urlFor(loc),
    searchUrl: () => urlFor(loc, PATHS[loc].search),
    routesUrl: () => urlFor(loc, PATHS[loc].routes),
    countriesUrl: () => urlFor(loc, PATHS[loc].countries),
    faqUrl: () => urlFor(loc, PATHS[loc].faq),
  };
}

// Equivalente de una página en otro idioma (para el selector y hreflang)
function equivalents(page) {
  const out = {};
  for (const loc of LOCALES) {
    const ix = indexFor(loc);
    if (page.type === 'lesson') {
      const cid = page.course.id; const lid = page.lesson.id;
      const co = CONTENT[loc].courses.find((x) => x.id === cid);
      out[loc] = ix.lessonUrl(co, co.lessons.find((l) => l.id === lid));
    } else if (page.type === 'course') {
      out[loc] = ix.courseUrl(CONTENT[loc].courses.find((x) => x.id === page.course.id));
    } else if (page.type === 'section') out[loc] = ix.sectionUrl(page.sectionId);
    else if (page.type === 'routes') out[loc] = ix.routesUrl();
    else if (page.type === 'countries') out[loc] = ix.countriesUrl();
    else if (page.type === 'faq') out[loc] = ix.faqUrl();
    else if (page.type === 'search') out[loc] = ix.searchUrl();
    else if (page.type === 'sections') out[loc] = urlFor(loc, PATHS[loc].sections);
    else out[loc] = ix.homeUrl();
  }
  return out;
}

// -------- Componentes HTML --------
const icon = {
  search: '<svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>',
  arrowR: '<svg aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
  arrowL: '<svg aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M11 6l-6 6 6 6"/></svg>',
  check: '<svg aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>',
  play: '<svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>',
};
const favicon = `data:image/svg+xml,${encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="8" fill="#3B2F9E"/><path d="M9 11h14v3H9zm0 7h10v3H9z" fill="#fff"/></svg>')}`;

function header(loc, page, eq) {
  const c = CONTENT[loc]; const L = t(loc); const ix = indexFor(loc);
  const navItems = [
    [ix.homeUrl(), L.nav.home],
    [`${ix.homeUrl()}#cursos`, L.nav.courses],
    [ix.routesUrl(), L.nav.routes],
    [ix.countriesUrl(), L.nav.countries],
    [ix.faqUrl(), L.nav.faq],
  ];
  const langs = LOCALES.map((other) => {
    const active = other === loc;
    return `<a class="lang-link" href="${eq[other]}" hreflang="${SITE.locales[other].hreflang}" lang="${SITE.locales[other].htmlLang}" ${active ? 'aria-current="true"' : ''} data-lang-choice="${other}">${esc(SITE.locales[other].label)}</a>`;
  }).join('');
  return `
<a class="skip-link" href="#main">${esc(L.skipNav)}</a>
<header class="site-header">
  <div class="container header-row">
    <a class="brand" href="${ix.homeUrl()}" aria-label="${esc(c.ui.brand)} — ${esc(c.ui.helpCenter)}">
      <span class="brand-mark" aria-hidden="true"></span>
      <span class="brand-text"><strong>${esc(c.ui.brand)}</strong><span>${esc(c.ui.helpCenter)}</span></span>
    </a>
    <div class="header-tools">
      <form class="header-search" action="${ix.searchUrl()}" method="get" role="search" data-suggest>
        <label class="sr-only" for="q-${loc}">${esc(c.ui.search)}</label>
        <input id="q-${loc}" name="q" type="search" autocomplete="off" minlength="2" placeholder="${esc(c.ui.searchPlaceholder)}" aria-controls="suggest-${loc}" aria-expanded="false">
        <button class="icon-btn" type="submit" aria-label="${esc(c.ui.searchButton)}">${icon.search}</button>
        <ul class="suggest" id="suggest-${loc}" role="listbox" hidden></ul>
      </form>
      <div class="lang-switch" role="group" aria-label="${esc(c.ui.language)}">${langs}</div>
    </div>
  </div>
  <nav class="main-nav" aria-label="Principal">
    <div class="container"><ul>${navItems.map(([href, label]) => `<li><a href="${href}">${esc(label)}</a></li>`).join('')}</ul></div>
  </nav>
</header>`;
}

function footer(loc) {
  const c = CONTENT[loc]; const L = t(loc); const ix = indexFor(loc);
  return `
<footer class="site-footer">
  <div class="container footer-grid">
    <div>
      <p class="footer-brand"><strong>${esc(c.ui.brand)}</strong> · ${esc(c.ui.helpCenter)}</p>
      <p class="muted">${esc(c.ui.footerNote)}</p>
    </div>
    <nav aria-label="Pie de página">
      <ul class="footer-links">
        <li><a href="${ix.homeUrl()}#cursos">${esc(L.nav.courses)}</a></li>
        <li><a href="${ix.routesUrl()}">${esc(L.nav.routes)}</a></li>
        <li><a href="${ix.countriesUrl()}">${esc(L.nav.countries)}</a></li>
        <li><a href="${ix.faqUrl()}">${esc(L.nav.faq)}</a></li>
      </ul>
    </nav>
  </div>
</footer>`;
}

function layout({ loc, title, description, page, body, jsonLd = [], bodyClass = '' }) {
  const L = t(loc);
  const LABELS_ = LABELS[loc];
  const eq = equivalents(page);
  const canonical = absUrl(eq[loc]);
  ALTS.set(eq[loc], eq);
  const alternates = [
    ...LOCALES.map((o) => `<link rel="alternate" hreflang="${SITE.locales[o].hreflang}" href="${absUrl(eq[o])}">`),
    `<link rel="alternate" hreflang="x-default" href="${absUrl(`${BASE}/`)}">`,
  ].join('\n  ');
  const ld = jsonLd.map((o) => `<script type="application/ld+json">${JSON.stringify(o)}</script>`).join('\n  ');
  const fullTitle = title === CONTENT[loc].home.title ? title : `${title} · ${CONTENT[loc].ui.brand}`;
  return `<!doctype html>
<html lang="${SITE.locales[loc].htmlLang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${esc(fullTitle)}</title>
  <meta name="description" content="${esc(description)}">
  <link rel="canonical" href="${canonical}">
  ${alternates}
  <meta property="og:type" content="website">
  <meta property="og:title" content="${esc(fullTitle)}">
  <meta property="og:description" content="${esc(description)}">
  <meta property="og:url" content="${canonical}">
  <meta property="og:locale" content="${loc === 'es' ? 'es_419' : 'pt_BR'}">
  <meta name="theme-color" content="#050559">
  <link rel="icon" href="${favicon}">
  <link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="${BASE}/assets/css/help.css">
  ${ld}
</head>
<body class="${bodyClass}" data-locale="${loc}" data-seg="${SEG[loc]}" data-base="${BASE}" data-search-index="${BASE}/assets/search-${SEG[loc]}.json" data-l-done="${esc(L.statusDone)}" data-l-pending="${esc(L.statusPending)}" data-l-mark="${esc(L.markDone)}" data-l-marked="${esc(L.markedDone)}" data-l-correct="${esc(L.quizCorrect)}" data-l-incorrect="${esc(L.quizIncorrect)}" data-l-select="${esc(L.quizSelectOne)}" data-l-empty="${esc(L.searchEmpty)}" data-l-searching="${esc(LABELS_.searching)}" data-l-results="${esc(LABELS_.resultsWord)}" data-l-transcript-empty="${esc(LABELS_.transcriptEmpty)}" data-l-transcript-loading="${esc(LABELS_.transcriptLoading)}" data-l-of="${esc(LABELS_.progressOf)}" data-l-lesson="${esc(LABELS_.lessonOf)}" data-l-intro="${esc(L.searchIntro)}">
  ${header(loc, page, eq)}
  <main id="main" tabindex="-1">
    ${body}
  </main>
  ${footer(loc)}
  <script src="${BASE}/assets/js/help.js" defer></script>
</body>
</html>`;
}

const crumbs = (loc, items) => `<nav class="crumbs" aria-label="Ruta de navegación"><ol>${[[urlFor(loc), t(loc).crumbHome], ...items].map(([href, label], i, arr) => (i === arr.length - 1 ? `<li aria-current="page">${esc(label)}</li>` : `<li><a href="${href}">${esc(label)}</a></li>`)).join('')}</ol></nav>`;
// Mapa URL canónica -> URLs equivalentes por idioma (para el sitemap con alternates)
const ALTS = new Map();

const roleChip = (loc, roleId) => `<span class="chip">${esc(CONTENT[loc].roles[roleId] ? t(loc).roleNames[roleId] : roleId)}</span>`;
const levelLabel = (loc, lv) => t(loc).levelNames[lv] ?? lv;

// -------- Páginas --------
function homePage(loc) {
  const c = CONTENT[loc]; const L = t(loc); const ix = indexFor(loc); const h = c.home;
  const page = { type: 'home' };
  const roleButtons = SITE.roleIds.map((id) => `<button type="button" class="role-btn" data-role-btn="${id}" aria-pressed="false">${esc(L.roleNames[id])}</button>`).join('');
  const rolePanels = SITE.roleIds.map((id) => `<p class="role-panel" data-role-panel="${id}" hidden><strong>${esc(c.roles[id].name)}.</strong> ${esc(c.roles[id].description)} <a class="inline-link" href="${ix.routesUrl()}#${id}">${esc(L.roleCta)} ${icon.arrowR}</a></p>`).join('');
  const courseCards = c.courses.map((co) => `
    <article class="card course-card" data-course-card data-roles="${co.roles.join(' ')}">
      <p class="card-kicker">${esc(L.courseWord)} · ${esc(levelLabel(loc, co.level))}</p>
      <h3><a href="${ix.courseUrl(co)}">${esc(co.title)}</a></h3>
      <p>${esc(co.summary)}</p>
      <p class="meta-row"><span>${esc(co.duration)}</span><span>${co.lessons.length} ${esc(L.lessonsCount)}</span></p>
      <div class="chips">${co.roles.map((r) => roleChip(loc, r)).join('')}</div>
    </article>`).join('');
  const sectionCards = SITE.sectionIds.map((id) => {
    const s = c.sections[id];
    return `<a class="card section-card" href="${ix.sectionUrl(id)}"><h3>${esc(s.name)}</h3><p>${esc(s.short)}</p><span class="card-link">${esc(L.sectionWord)} ${icon.arrowR}</span></a>`;
  }).join('');
  const countryCards = c.countries.map((k) => `<a class="card country-card" href="${ix.countriesUrl()}#${k.code}"><h3>${esc(k.name)}</h3><p>${esc(k.levels)}</p><p class="muted">${esc(L.countryScale)}: ${esc(k.grading.scale)}</p></a>`).join('');
  const faqItems = c.faq.slice(0, 4).map((f) => `<details class="faq-item"><summary>${esc(f.q)}</summary><p>${esc(f.a)}</p></details>`).join('');
  const stats = h.stats.map((s) => `<li><strong>${esc(s.value)}</strong><span>${esc(s.label)}</span></li>`).join('');
  const body = `
  <section class="hero">
    <div class="container hero-grid">
      <div>
        <p class="kicker">${esc(h.heroKicker)}</p>
        <h1>${esc(h.heroTitle)}</h1>
        <p class="lead">${esc(h.heroText)}</p>
        <form class="hero-search" action="${ix.searchUrl()}" method="get" role="search">
          <label class="sr-only" for="q-hero">${esc(L.search)}</label>
          <input id="q-hero" name="q" type="search" minlength="2" placeholder="${esc(L.searchPlaceholder)}" autocomplete="off" required>
          <button class="btn btn-primary" type="submit">${icon.search} ${esc(L.searchButton)}</button>
        </form>
        <div class="hero-ctas">
          <a class="btn btn-ghost" href="#cursos">${esc(h.heroCta)} ${icon.arrowR}</a>
          <a class="btn btn-ghost" href="${ix.sectionUrl('cursos')}">${esc(h.heroCtaSecondary)}</a>
        </div>
      </div>
      <ul class="hero-stats" aria-label="${esc(h.coursesTitle)}">${stats}</ul>
    </div>
  </section>

  <section class="band" id="rol" aria-labelledby="rol-h">
    <div class="container">
      <h2 id="rol-h">${esc(L.roleLabel)}</h2>
      <p class="muted">${esc(h.roleIntro)}</p>
      <div class="role-picker" role="group" aria-label="${esc(L.roleLabel)}">
        <button type="button" class="role-btn is-active" data-role-btn="all" aria-pressed="true">${esc(L.allRoles)}</button>
        ${roleButtons}
      </div>
      <div class="role-panels" aria-live="polite">
        <p class="role-panel-hint" data-role-hint>${esc(L.rolePanelHint)}</p>
        ${rolePanels}
      </div>
    </div>
  </section>

  <section class="container section" id="cursos" aria-labelledby="cursos-h">
    <div class="section-head">
      <div><h2 id="cursos-h">${esc(h.coursesTitle)}</h2><p class="muted">${esc(h.coursesText)}</p></div>
      <a class="inline-link" href="${ix.routesUrl()}">${esc(L.seeAllRoutes)} ${icon.arrowR}</a>
    </div>
    <div class="grid grid-courses" data-course-grid>${courseCards}</div>
    <p class="empty-filter" data-empty-filter hidden>${esc(L.rolePanelHint)}</p>
  </section>

  <section class="container section" id="secciones" aria-labelledby="sec-h">
    <div class="section-head">
      <div><h2 id="sec-h">${esc(h.sectionsTitle)}</h2><p class="muted">${esc(h.sectionsText)}</p></div>
    </div>
    <div class="grid grid-sections">${sectionCards}</div>
  </section>

  <section class="container section" id="paises" aria-labelledby="pa-h">
    <div class="section-head">
      <div><h2 id="pa-h">${esc(h.countriesTitle)}</h2><p class="muted">${esc(h.countriesText)}</p></div>
      <a class="inline-link" href="${ix.countriesUrl()}">${esc(L.seeAllCountries)} ${icon.arrowR}</a>
    </div>
    <div class="grid grid-3">${countryCards}</div>
  </section>

  <section class="container section" id="faq" aria-labelledby="faq-h">
    <div class="section-head">
      <div><h2 id="faq-h">${esc(h.faqTitle)}</h2></div>
      <a class="inline-link" href="${ix.faqUrl()}">${esc(L.seeAllFaq)} ${icon.arrowR}</a>
    </div>
    <div class="faq-list">${faqItems}</div>
  </section>`;
  const jsonLd = [{
    '@context': 'https://schema.org', '@type': 'ItemList', name: h.coursesTitle,
    itemListElement: c.courses.map((co, i) => ({ '@type': 'ListItem', position: i + 1, url: absUrl(ix.courseUrl(co)), name: co.title })),
  }];
  return { url: ix.homeUrl(), html: layout({ loc, title: h.title, description: h.description, page, body, jsonLd, bodyClass: 'page-home' }) };
}

function coursePage(loc, co) {
  const c = CONTENT[loc]; const L = t(loc); const ix = indexFor(loc);
  const page = { type: 'course', course: co };
  const first = co.lessons[0];
  const lessonRows = co.lessons.map((l) => `
    <li class="lesson-row" data-lesson-row="${l.id}">
      <a href="${ix.lessonUrl(co, l)}">
        <span class="num">${esc(l.id)}</span>
        <span class="lesson-title">${esc(l.title)}<span class="lesson-summary">${esc(l.summary)}</span></span>
        <span class="dur">${esc(l.duration)}</span>
        <span class="status" data-status="${l.id}">${esc(L.statusPending)}</span>
      </a>
    </li>`).join('');
  const recommended = SITE.roleIds.filter((r) => co.roles.includes(r)).map((r) => roleChip(loc, r)).join('');
  const body = `
  ${crumbs(loc, [[ix.homeUrl() + '#cursos', L.nav.courses], [null, co.title]])}
  <header class="page-hero">
    <div class="container">
      <p class="kicker">${esc(L.courseWord)} · ${esc(levelLabel(loc, co.level))}</p>
      <h1>${esc(co.title)}</h1>
      <p class="lead">${esc(co.summary)}</p>
      <dl class="facts">
        <div><dt>${esc(L.durationLabel)}</dt><dd>${esc(co.duration)}</dd></div>
        <div><dt>${esc(L.levelLabel)}</dt><dd>${esc(levelLabel(loc, co.level))}</dd></div>
        <div><dt>${esc(L.lessonsTitle)}</dt><dd>${co.lessons.length}</dd></div>
        <div><dt>${esc(L.audienceLabel)}</dt><dd>${esc(co.audience.join(', '))}</dd></div>
      </dl>
      <div class="progress" data-course-progress="${co.id}">
        <p class="progress-label"><span>${esc(L.progressLabel)}</span><span><span data-progress-count>0</span> ${esc(L.progressOf)} ${co.lessons.length}</span></p>
        <div class="bar" role="progressbar" aria-valuemin="0" aria-valuemax="${co.lessons.length}" aria-valuenow="0" aria-label="${esc(L.progressLabel)}"><span data-progress-bar style="width:0%"></span></div>
      </div>
      <p class="cta-row"><a class="btn btn-primary" href="${ix.lessonUrl(co, first)}">${esc(L.courseStart)} ${icon.arrowR}</a></p>
    </div>
  </header>
  <div class="container two-col">
    <section class="content-block">
      <h2>${esc(L.objectivesTitle)}</h2>
      <ul class="checks">${co.objectives.map((o) => `<li>${icon.check}<span>${esc(o)}</span></li>`).join('')}</ul>
      <h2>${esc(L.lessonsTitle)}</h2>
      <ol class="lesson-list">${lessonRows}</ol>
    </section>
    <aside class="side">
      <div class="card">
        <h3>${esc(L.audienceLabel)}</h3>
        <p>${esc(co.audience.join(' · '))}</p>
        <h3>${esc(L.recommendedFor)}</h3>
        <div class="chips">${recommended}</div>
      </div>
    </aside>
  </div>`;
  const jsonLd = [{ '@context': 'https://schema.org', '@type': 'Course', name: co.title, description: co.summary, inLanguage: SITE.locales[loc].htmlLang, provider: { '@type': 'Organization', name: c.ui.brand }, hasCourseInstance: { '@type': 'CourseInstance', courseMode: 'online' } }];
  return { url: ix.courseUrl(co), html: layout({ loc, title: co.title, description: co.summary, page, body, jsonLd, bodyClass: 'page-course' }) };
}

async function lessonPage(loc, co, l, hasVideo) {
  const c = CONTENT[loc]; const L = t(loc); const ix = indexFor(loc);
  const page = { type: 'lesson', course: co, lesson: l };
  const idx = co.lessons.findIndex((x) => x.id === l.id);
  const prev = co.lessons[idx - 1]; const next = co.lessons[idx + 1];
  const rel = lessonVideoRel(loc, l.id);
  const videoBlock = hasVideo ? `
    <div class="video-box">
      <video id="lesson-video" controls preload="metadata" playsinline aria-describedby="video-help" src="${BASE}/${rel}.mp4">
        <track kind="subtitles" srclang="${SITE.locales[loc].htmlLang}" label="${esc(SITE.locales[loc].label)}" src="${BASE}/${rel}.vtt">
        ${esc(c.ui.videoTitle)}
      </video>
    </div>
    <div class="video-tools">
      <button type="button" class="btn btn-small" data-subs-toggle="lesson-video" aria-pressed="false" data-on="${esc(c.ui.subtitlesOn)}" data-off="${esc(c.ui.subtitlesOff)}">${esc(c.ui.subtitlesOn)}</button>
      <p id="video-help" class="muted small">${esc(L.subsHelp)}</p>
    </div>
    <details class="transcript" data-transcript="${BASE}/${rel}.vtt">
      <summary>${esc(c.ui.transcriptTitle)}</summary>
      <div class="transcript-body" data-transcript-body><p class="muted">${esc(L.transcriptLoading)}</p></div>
    </details>` : `
    <div class="video-pending" role="note">
      <span class="play-badge" aria-hidden="true">${icon.play}</span>
      <p>${esc(c.ui.videoPending)}</p>
    </div>`;
  const quiz = l.quiz.map((q, qi) => `
    <fieldset class="question" data-question data-answer="${q.answer}" data-explain="${esc(q.explain)}">
      <legend><span class="q-num">${qi + 1}</span> ${esc(q.q)}</legend>
      <div class="options">
        ${q.options.map((o, oi) => `<label class="option"><input type="radio" name="q-${l.id}-${qi}" value="${oi}"><span>${esc(o)}</span></label>`).join('')}
      </div>
      <div class="q-actions"><button type="button" class="btn btn-small" data-quiz-check>${esc(c.ui.quizCheck)}</button></div>
      <p class="feedback" role="status" aria-live="polite" data-feedback></p>
    </fieldset>`).join('');
  const relatedSections = SITE.sectionIds.filter((sid) => c.sections[sid].lessons.includes(l.id));
  const body = `
  ${crumbs(loc, [[ix.homeUrl() + '#cursos', L.nav.courses], [ix.courseUrl(co), co.title], [null, l.title]])}
  <article class="lesson" data-lesson-id="${l.id}" data-course-id="${co.id}">
    <header class="page-hero small">
      <div class="container">
        <p class="kicker">${esc(L.lessonOf)} ${esc(l.id)} · <a href="${ix.courseUrl(co)}">${esc(co.title)}</a></p>
        <h1>${esc(l.title)}</h1>
        <p class="lead">${esc(l.summary)}</p>
        <dl class="facts compact">
          <div><dt>${esc(L.durationLabel)}</dt><dd>${esc(l.duration)}</dd></div>
          <div><dt>${esc(L.levelLabel)}</dt><dd>${esc(levelLabel(loc, co.level))}</dd></div>
        </dl>
      </div>
    </header>
    <div class="container lesson-grid">
      <div class="lesson-main">
        <section class="block objectives-block" aria-labelledby="obj-${l.id}">
          <h2 id="obj-${l.id}">${esc(L.objectivesTitle)}</h2>
          <ul class="checks">${l.objectives.map((o) => `<li>${icon.check}<span>${esc(o)}</span></li>`).join('')}</ul>
        </section>
        <section class="block video-block" aria-labelledby="vid-${l.id}">
          <h2 id="vid-${l.id}">${esc(c.ui.videoTitle)}</h2>
          ${videoBlock}
        </section>
        <section class="block" aria-labelledby="steps-${l.id}">
          <h2 id="steps-${l.id}">${esc(L.stepsTitle)}</h2>
          <ol class="steps">${l.steps.map((s) => `<li><h3>${esc(s.t)}</h3><p>${esc(s.b)}</p></li>`).join('')}</ol>
        </section>
        <section class="tip-box" aria-labelledby="tips-${l.id}">
          <h2 id="tips-${l.id}">${esc(L.tipsTitle)}</h2>
          <ul>${l.tips.map((tp) => `<li>${esc(tp)}</li>`).join('')}</ul>
        </section>
        <section class="block quiz" data-quiz aria-labelledby="quiz-${l.id}">
          <h2 id="quiz-${l.id}">${esc(c.ui.quizTitle)}</h2>
          ${quiz}
        </section>
        <div class="complete-row">
          <button type="button" class="btn btn-primary" data-complete data-lesson="${l.id}" data-course="${co.id}" aria-pressed="false">${esc(L.markDone)}</button>
        </div>
        <nav class="pager" aria-label="Navegación entre lecciones">
          ${prev ? `<a class="pager-link prev" href="${ix.lessonUrl(co, prev)}">${icon.arrowL}<span><small>${esc(c.ui.prev)}</small>${esc(prev.title)}</span></a>` : `<a class="pager-link prev" href="${ix.courseUrl(co)}">${icon.arrowL}<span><small>${esc(L.backToCourse)}</small>${esc(co.title)}</span></a>`}
          ${next ? `<a class="pager-link next" href="${ix.lessonUrl(co, next)}"><span><small>${esc(c.ui.next)}</small>${esc(next.title)}</span>${icon.arrowR}</a>` : `<a class="pager-link next" href="${ix.courseUrl(co)}"><span><small>${esc(L.backToCourse)}</small>${esc(co.title)}</span>${icon.arrowR}</a>`}
        </nav>
      </div>
      <aside class="side">
        <div class="card">
          <h3>${esc(L.lessonsTitle)}</h3>
          <ol class="mini-list">${co.lessons.map((x) => `<li class="${x.id === l.id ? 'is-current' : ''}" data-mini-row="${x.id}"><a href="${ix.lessonUrl(co, x)}" ${x.id === l.id ? 'aria-current="page"' : ''}><span class="num">${esc(x.id)}</span> ${esc(x.title)}</a></li>`).join('')}</ol>
        </div>
        ${relatedSections.length ? `<div class="card">
          <h3>${esc(c.ui.relatedSections)}</h3>
          <ul class="plain-list">${relatedSections.map((sid) => `<li><a href="${ix.sectionUrl(sid)}">${esc(c.sections[sid].name)}</a></li>`).join('')}</ul>
        </div>` : ''}
      </aside>
    </div>
  </article>`;
  const jsonLd = [{
    '@context': 'https://schema.org', '@type': 'BreadcrumbList',
    itemListElement: [
      { '@type': 'ListItem', position: 1, name: L.crumbHome, item: absUrl(ix.homeUrl()) },
      { '@type': 'ListItem', position: 2, name: co.title, item: absUrl(ix.courseUrl(co)) },
      { '@type': 'ListItem', position: 3, name: l.title, item: absUrl(ix.lessonUrl(co, l)) },
    ],
  }];
  return { url: ix.lessonUrl(co, l), html: layout({ loc, title: `${l.title} — ${co.title}`, description: l.summary, page, body, jsonLd, bodyClass: 'page-lesson' }) };
}

function sectionPage(loc, sid) {
  const c = CONTENT[loc]; const L = t(loc); const ix = indexFor(loc); const s = c.sections[sid];
  const page = { type: 'section', sectionId: sid };
  const lessonLinks = s.lessons.map((lid) => {
    const co = c.courses.find((x) => x.lessons.some((y) => y.id === lid));
    const l = co.lessons.find((y) => y.id === lid);
    return `<li><a href="${ix.lessonUrl(co, l)}"><span class="num">${esc(l.id)}</span> ${esc(l.title)}</a><span class="muted small">${esc(co.title)}</span></li>`;
  }).join('');
  const body = `
  ${crumbs(loc, [[ix.homeUrl() + '#secciones', L.nav.sections], [null, s.name]])}
  <header class="page-hero small">
    <div class="container">
      <p class="kicker">${esc(L.sectionWord)} · ${esc(c.ui.brand)}</p>
      <h1>${esc(s.name)}</h1>
      <p class="lead">${esc(s.short)}</p>
    </div>
  </header>
  <div class="container two-col">
    <section class="content-block">
      <p class="lead-body">${esc(s.summary)}</p>
      <h2>${esc(L.sectionBasics)}</h2>
      <ol class="steps compact">${s.basics.map((b) => `<li><p>${esc(b)}</p></li>`).join('')}</ol>
      <h2>${esc(L.sectionWhen)}</h2>
      <ul class="checks">${s.whenToUse.map((w) => `<li>${icon.check}<span>${esc(w)}</span></li>`).join('')}</ul>
    </section>
    <aside class="side">
      <div class="card">
        <h3>${esc(L.sectionLessonsIntro)}</h3>
        <ul class="plain-list links">${lessonLinks}</ul>
      </div>
    </aside>
  </div>`;
  return { url: ix.sectionUrl(sid), html: layout({ loc, title: s.name, description: s.short, page, body, bodyClass: 'page-section' }) };
}

function sectionsIndexPage(loc) {
  // No hay página índice de secciones separada: la portada enlaza cada sección.
  // Se genera una página con las 8 secciones para la navegación del pie y el menú.
  const c = CONTENT[loc]; const L = t(loc); const ix = indexFor(loc);
  const page = { type: 'sections' };
  const cards = SITE.sectionIds.map((id) => `<a class="card section-card" href="${ix.sectionUrl(id)}"><h3>${esc(c.sections[id].name)}</h3><p>${esc(c.sections[id].short)}</p><span class="card-link">${esc(L.sectionWord)} ${icon.arrowR}</span></a>`).join('');
  const body = `
  ${crumbs(loc, [[null, L.nav.sections]])}
  <header class="page-hero small"><div class="container"><h1>${esc(L.nav.sections)}</h1><p class="lead">${esc(L.sectionsIntro)}</p></div></header>
  <div class="container section"><div class="grid grid-sections">${cards}</div></div>`;
  return { url: urlFor(loc, PATHS[loc].sections), html: layout({ loc, title: L.nav.sections, description: L.sectionsIntro, page, body, bodyClass: 'page-sections' }) };
}

function routesPage(loc) {
  const c = CONTENT[loc]; const L = t(loc); const ix = indexFor(loc);
  const page = { type: 'routes' };
  const blocks = SITE.roleIds.map((rid) => {
    const r = c.roles[rid];
    const items = r.lessons.map((lid, i) => {
      const co = c.courses.find((x) => x.lessons.some((y) => y.id === lid));
      const l = co.lessons.find((y) => y.id === lid);
      return `<li><span class="step-no">${i + 1}</span><a href="${ix.lessonUrl(co, l)}">${esc(l.title)}</a><span class="muted small">${esc(l.duration)} · ${esc(co.title)}</span></li>`;
    }).join('');
    return `<section class="route" id="${rid}" aria-labelledby="route-${rid}"><h2 id="route-${rid}">${esc(L.roleNames[rid])}</h2><p>${esc(r.description)}</p><ol class="route-list">${items}</ol></section>`;
  }).join('');
  const body = `
  ${crumbs(loc, [[null, L.nav.routes]])}
  <header class="page-hero small"><div class="container"><h1>${esc(L.rolesWord ?? c.ui.rolesWord)}</h1><p class="lead">${esc(L.routesIntro)}</p></div></header>
  <div class="container narrow">${blocks}</div>`;
  return { url: ix.routesUrl(), html: layout({ loc, title: c.ui.rolesWord, description: L.routesIntro, page, body, bodyClass: 'page-routes' }) };
}

function countriesPage(loc) {
  const c = CONTENT[loc]; const L = t(loc); const ix = indexFor(loc);
  const page = { type: 'countries' };
  const blocks = c.countries.map((k) => `
    <section class="country" id="${k.code}" aria-labelledby="c-${k.code}">
      <h2 id="c-${k.code}">${esc(k.name)}</h2>
      <dl class="facts stacked">
        <div><dt>${esc(L.countryLevels)}</dt><dd>${esc(k.levels)}</dd></div>
        <div><dt>${esc(L.countryCurriculum)}</dt><dd>${esc(k.curriculum)}</dd></div>
        <div><dt>${esc(L.countryScale)}</dt><dd>${esc(k.grading.scale)}</dd></div>
        <div><dt>${esc(L.countryPassing)}</dt><dd>${esc(k.grading.passing)}</dd></div>
        <div><dt>${esc(L.countryNote)}</dt><dd>${esc(k.grading.note)}</dd></div>
      </dl>
      <h3>${esc(L.countryExamples)}</h3>
      <ul class="checks">${k.examples.map((x) => `<li>${icon.check}<span>${esc(x)}</span></li>`).join('')}</ul>
    </section>`).join('');
  const body = `
  ${crumbs(loc, [[null, L.nav.countries]])}
  <header class="page-hero small"><div class="container"><h1>${esc(L.nav.countries)}</h1><p class="lead">${esc(L.countriesIntro)}</p></div></header>
  <div class="container narrow">${blocks}</div>`;
  return { url: ix.countriesUrl(), html: layout({ loc, title: L.nav.countries, description: L.countriesIntro, page, body, bodyClass: 'page-countries' }) };
}

function faqPage(loc) {
  const c = CONTENT[loc]; const L = t(loc); const ix = indexFor(loc);
  const page = { type: 'faq' };
  const items = c.faq.map((f) => `<details class="faq-item"><summary>${esc(f.q)}</summary><p>${esc(f.a)}</p></details>`).join('');
  const body = `
  ${crumbs(loc, [[null, L.nav.faq]])}
  <header class="page-hero small"><div class="container"><h1>${esc(L.nav.faq)}</h1><p class="lead">${esc(L.faqIntro)}</p></div></header>
  <div class="container narrow"><div class="faq-list">${items}</div></div>`;
  const jsonLd = [{ '@context': 'https://schema.org', '@type': 'FAQPage', mainEntity: c.faq.map((f) => ({ '@type': 'Question', name: f.q, acceptedAnswer: { '@type': 'Answer', text: f.a } })) }];
  return { url: ix.faqUrl(), html: layout({ loc, title: L.nav.faq, description: L.faqIntro, page, body, jsonLd, bodyClass: 'page-faq' }) };
}

function searchPage(loc) {
  const L = t(loc); const ix = indexFor(loc);
  const page = { type: 'search' };
  const body = `
  ${crumbs(loc, [[null, L.search]])}
  <header class="page-hero small"><div class="container">
    <h1>${esc(L.search)}</h1>
    <form class="search-page" action="${ix.searchUrl()}" method="get" role="search">
      <label class="sr-only" for="q-page">${esc(L.search)}</label>
      <input id="q-page" name="q" type="search" minlength="2" placeholder="${esc(L.searchPlaceholder)}" autocomplete="off" data-search-page>
      <button class="btn btn-primary" type="submit">${esc(L.searchButton)}</button>
    </form>
    <p class="muted" data-search-status aria-live="polite">${esc(L.searchIntro)}</p>
  </div></header>
  <div class="container narrow"><ul class="results" data-results></ul></div>`;
  return { url: ix.searchUrl(), html: layout({ loc, title: L.search, description: L.searchIntro, page, body, bodyClass: 'page-search' }) };
}

function rootPage() {
  const body = `
  <section class="chooser">
    <div class="container">
      <p class="kicker">${esc(CONTENT.es.ui.helpCenter)} · ${esc(CONTENT.es.ui.brand)}</p>
      <h1>${esc(LABELS.es.langChooserTitle)}</h1>
      <p class="lead">${esc(LABELS.es.langChooserText)}</p>
      <div class="chooser-grid">
        <a class="card lang-card" href="${urlFor('es')}" hreflang="es-419" lang="es"><span class="lang-flag">ES</span><strong>Español</strong><span class="muted">Latinoamérica · México, Chile</span></a>
        <a class="card lang-card" href="${urlFor('pt-BR')}" hreflang="pt-BR" lang="pt-BR"><span class="lang-flag">PT</span><strong>Português (Brasil)</strong><span class="muted">Brasil</span></a>
      </div>
    </div>
  </section>`;
  const html = `<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${esc(CONTENT.es.ui.helpCenter)} · ${esc(CONTENT.es.ui.brand)}</title>
  <meta name="description" content="${esc(CONTENT.es.home.description)}">
  <link rel="canonical" href="${absUrl(`${BASE}/`)}">
  <link rel="alternate" hreflang="es-419" href="${absUrl(urlFor('es'))}">
  <link rel="alternate" hreflang="pt-BR" href="${absUrl(urlFor('pt-BR'))}">
  <link rel="alternate" hreflang="x-default" href="${absUrl(`${BASE}/`)}">
  <link rel="icon" href="${favicon}">
  <link rel="stylesheet" href="${BASE}/assets/help.css">
  <script>
    (function () {
      try {
        var saved = localStorage.getItem('sa-help:lang');
        if (saved === 'es' || saved === 'pt-br') { location.replace('${BASE}/' + saved + '/'); return; }
      } catch (e) {}
      var nav = (navigator.language || 'es').toLowerCase();
      if (nav.indexOf('pt') === 0) location.replace('${BASE}/pt-br/');
    })();
  </script>
</head>
<body class="page-chooser" data-locale="es" data-base="${BASE}">
  <main id="main">${body}</main>
  <noscript><p class="container"><a href="${urlFor('es')}">Español</a> · <a href="${urlFor('pt-BR')}">Português (Brasil)</a></p></noscript>
</body>
</html>`;
  return html;
}

function notFoundPage() {
  const L = LABELS.es; const body = `
  <section class="chooser"><div class="container">
    <p class="kicker">404</p>
    <h1>${esc(CONTENT.es.ui.notFoundTitle)} · ${esc(CONTENT['pt-BR'].ui.notFoundTitle ?? 'Página não encontrada')}</h1>
    <p class="lead">${esc(CONTENT.es.ui.notFoundText)}</p>
    <p><a class="btn btn-primary" href="${urlFor('es')}">${esc(L.notFoundCta)}</a> <a class="btn btn-ghost" href="${urlFor('pt-BR')}">${esc(LABELS['pt-BR'].notFoundCtaPt)}</a></p>
  </div></section>`;
  return layout({ loc: 'es', title: 'Página no encontrada', description: CONTENT.es.ui.notFoundText, page: { type: 'home' }, body, bodyClass: 'page-404' });
}

// -------- Índice de búsqueda por idioma --------
const strip = (s) => String(s ?? '');
function searchIndex(loc) {
  const c = CONTENT[loc]; const L = t(loc); const ix = indexFor(loc); const entries = [];
  const add = (type, title, url, text, extra = {}) => entries.push({ type: L.searchTypes[type], title: strip(title), url, text: strip(text).slice(0, 1800), ...extra });
  for (const co of c.courses) {
    add('course', co.title, ix.courseUrl(co), `${co.summary} ${co.objectives.join(' ')} ${co.audience.join(' ')}`, { rank: 3 });
    for (const l of co.lessons) add('lesson', l.title, ix.lessonUrl(co, l), `${co.title}. ${l.summary} ${l.objectives.join(' ')} ${l.steps.map((s) => `${s.t}. ${s.b}`).join(' ')} ${l.tips.join(' ')}`, { rank: 2 });
  }
  for (const sid of SITE.sectionIds) {
    const s = c.sections[sid];
    add('section', s.name, ix.sectionUrl(sid), `${s.short} ${s.summary} ${s.whenToUse.join(' ')} ${s.basics.join(' ')}`, { rank: 3 });
  }
  for (const rid of SITE.roleIds) add('route', `${L.roleNames[rid]} · ${L.rolesWord ?? c.ui.rolesWord}`, `${ix.routesUrl()}#${rid}`, c.roles[rid].description, { rank: 1 });
  for (const f of c.faq) add('faq', f.q, `${ix.faqUrl()}`, f.a, { rank: 1 });
  for (const k of c.countries) add('country', `${k.name} · ${L.countryScale}`, `${ix.countriesUrl()}#${k.code}`, `${k.levels} ${k.curriculum} ${k.grading.scale} ${k.grading.passing} ${k.examples.join(' ')}`, { rank: 2 });
  return entries;
}

// -------- Build --------
async function write(rel, content) {
  const file = path.join(OUT, rel);
  await mkdir(path.dirname(file), { recursive: true });
  await writeFile(file, content);
}
const pageFile = (url) => {
  const rel = url.startsWith(BASE) ? url.slice(BASE.length) : url;
  return path.join(rel.replace(/\/$/, ''), 'index.html');
};

async function videoExists(loc, id) {
  const base = path.join(VIDEO_OUT, SEG[loc], lessonKey(id));
  try { await access(`${base}.mp4`); await access(`${base}.vtt`); return true; } catch { return false; }
}

async function main() {
  validate();
  await rm(path.join(ROOT, 'dist'), { recursive: true, force: true });
  await mkdir(OUT, { recursive: true });

  // Raíz de la ruta pública: chooser de idioma
  // Con base /ayuda, la raíz del dominio redirige al centro de ayuda.
  await mkdir(path.join(ROOT, 'dist'), { recursive: true });
  if (BASE) {
    await writeFile(path.join(ROOT, 'dist', 'index.html'), `<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=${BASE}/"><link rel="canonical" href="${absUrl(`${BASE}/`)}"><title>${esc(CONTENT.es.ui.brand)}</title><a href="${BASE}/">${esc(CONTENT.es.ui.helpCenter)}</a>\n`);
  }
  await write('index.html', rootPage());
  await write('404.html', notFoundPage());

  const urls = [];
  const missingVideos = [];
  for (const loc of LOCALES) {
    const c = CONTENT[loc];
    const ix = indexFor(loc);
    const pages = [];
    pages.push(homePage(loc));
    pages.push(sectionsIndexPage(loc));
    for (const co of c.courses) {
      pages.push(coursePage(loc, co));
      for (const l of co.lessons) {
        const has = await videoExists(loc, l.id);
        if (!has) missingVideos.push(`${loc} ${l.id} ${l.title}`);
        pages.push(await lessonPage(loc, co, l, has));
      }
    }
    for (const sid of SITE.sectionIds) pages.push(sectionPage(loc, sid));
    pages.push(routesPage(loc), countriesPage(loc), faqPage(loc), searchPage(loc));
    for (const p of pages) {
      await write(pageFile(p.url), p.html);
      urls.push(p.url);
    }
    await write(`assets/search-${SEG[loc]}.json`, JSON.stringify(searchIndex(loc)));
    void ix;
    // Videos publicados (si existen en video/out)
    const vdir = path.join(VIDEO_OUT, SEG[loc]);
    try {
      await mkdir(path.join(OUT, 'videos', SEG[loc]), { recursive: true });
      for (const f of await readdir(vdir)) {
        if (/\.(mp4|vtt)$/.test(f)) await cp(path.join(vdir, f), path.join(OUT, 'videos', SEG[loc], f));
      }
    } catch { /* sin videos todavía */ }
    void ix;
  }

  await cp(path.join(ROOT, 'assets'), path.join(OUT, 'assets'), { recursive: true });

  const today = new Date().toISOString().slice(0, 10);
  const sitemapEntries = urls.map((u) => {
    const eq = ALTS.get(u) ?? {};
    const links = [...LOCALES.map((o) => eq[o] && `    <xhtml:link rel="alternate" hreflang="${SITE.locales[o].hreflang}" href="${absUrl(eq[o])}"/>`), `    <xhtml:link rel="alternate" hreflang="x-default" href="${absUrl(`${BASE}/`)}"/>`].filter(Boolean);
    return `  <url>\n    <loc>${absUrl(u)}</loc>\n    <lastmod>${today}</lastmod>\n${links.join('\n')}\n  </url>`;
  });
  await write('sitemap.xml', `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n${sitemapEntries.join('\n')}\n</urlset>\n`);
  await write('robots.txt', `User-agent: *\nAllow: /\nSitemap: ${absUrl(`${BASE}/sitemap.xml`)}\n`);

  console.log(`✓ Páginas generadas: ${urls.length} (${LOCALES.join(' + ')})`);
  console.log(`✓ Salida: ${path.relative(ROOT, OUT) || '.'} (base ${BASE || '/'})`);
  console.log(`${missingVideos.length ? '⚠' : '✓'} Lecciones sin video publicado: ${missingVideos.length} de ${LOCALES.reduce((n, l) => n + CONTENT[l].courses.reduce((m, co) => m + co.lessons.length, 0), 0)}`);
}

await main();
