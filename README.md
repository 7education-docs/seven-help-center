# Seven Assistant · Centro de ayuda (es / pt-BR)

Centro de ayuda público y bilingüe para docentes, coordinaciones académicas, jefaturas de estudio, tutorías y responsables de sistemas IT de colegios de México, Chile y Brasil.

- **Español (Latinoamérica):** `https://sevenai.es/ayuda/es/`
- **Português (Brasil):** `https://sevenai.es/ayuda/pt-br/`
- Raíz `https://sevenai.es/ayuda/`: selector de idioma (recuerda la elección y, si el navegador está en portugués, redirige).

## Estado (lo que está hecho y lo que falta)

| Área | Estado |
|---|---|
| Centro de ayuda (ES + PT-BR), 86 páginas generadas más la raíz de selección de idioma | **Hecho**. Build verificado en navegador: sin errores de consola, sin desbordamiento horizontal a 390 px, quiz, progreso, filtro por rol y búsqueda probados. |
| 6 cursos, 23 lecciones con pasos, consejos y preguntas de repaso (ES y PT-BR) | **Hecho**, pendiente de revisión de pedagogía y de validación de interfaz (ver abajo). |
| 8 secciones de referencia (Cursos, Conversaciones, Documentos, Series de lecciones, Tareas de corrección, Fichas interactivas, Plantillas, Configuración) | **Hecho** |
| Rutas por rol (docente, coordinación, jefatura/tutoría, responsable IT), escalas y currículos de México, Chile y Brasil, FAQ | **Hecho** |
| Vídeo tutoriales (MP4 + subtítulos activables) | **Pipeline listo y probado con una página de prueba. Vídeos reales NO generados**: ver bloqueo. |
| Capturas de pantalla de la plataforma | **No hechas**: requieren acceso a sevenai.es. |
| Plataforma de socios y Seven Code | Fuera de alcance, como se pidió. |

### Bloqueo de red (lo más importante)
Desde este entorno la política de red **bloquea** `sevenai.es` (CONNECT 403), `brand.7education.com` (no resuelve) y también `google.com`. Por eso:
1. **No he podido entrar en la cuenta demo.** Ningún vídeo ni captura salen de la plataforma real; no he inventado ninguna pantalla.
2. **No he podido leer la guía de marca** de Seven Education. La identidad visual del sitio es provisional: colores y tipografía están en los tokens de `assets/css/help.css` (`:root`) para sustituirlos por los oficiales.
3. Los nombres de botones de la interfaz están descritos por **intención** (por ejemplo, "entra en la sección Cursos"), no por etiqueta exacta, hasta validarlos en la cuenta demo.

Para desbloquearlo: en la configuración del entorno, añadir `sevenai.es` (y `brand.7education.com` si se quiere revisar la marca) a los dominios permitidos. Después, grabar las lecciones con el pipeline de `video/README.md`.

### Revisión pendiente antes de publicar
- **Validar contra la cuenta demo** cada paso de las lecciones (etiquetas y flujos). Las lecciones de administración (curso 6) describen funciones que todavía no he visto; marcarlas como pendientes hasta comprobarlas.
- **Pedagogía y traducción:** el portugués lo tradujo un agente y ha sido revisado solo por verificación de estructura. Conviene una revisión nativa de pt-BR. En los ejemplos de Brasil se usan series y nombres brasileños (8.º ano, BNCC, escala 0–10).
- **Escalas y leyes:** las escalas (México 5–10 con 6 de aprobación; Chile 1,0–7,0 con 4,0; Brasil 0–10 con media habitual de 6,0) y las referencias legales (LGPD, LFPDPPP, normativa chilena en actualización) son orientativas; el sitio lo dice en la propia página. Confirmar con el área jurídica.
- **Voz:** la narración usa Kokoro (voces `ef_dora` y `pf_dora`). Yo no puedo escuchar el audio: he verificado que se genera, la duración y los subtítulos, pero **la naturalidad hay que comprobarla de oído** antes de publicar.

## Decisiones tomadas
- **Sitio estático sin dependencias** (Node 22 + HTML/CSS/JS). Se publica como carpeta `dist/` bajo `/ayuda`. Motivo: SEO sólido, funciona sin servidor y no requiere cuentas de terceros.
- **URLs separadas por idioma** (`/ayuda/es/` y `/ayuda/pt-br/`) con `hreflang` y `sitemap.xml` con alternativas. Los IDs de cursos, lecciones y secciones son comunes, así que el selector de idioma apunta a la página equivalente.
- **Público y sin login**: todo el contenido es abierto; el progreso se guarda solo en el navegador del visitante (`localStorage`, con fallback si está bloqueado).
- **Vídeo con subtítulos activables** (pista WebVTT del reproductor, botón propio sincronizado con el control CC del navegador) y **transcripción interactiva**: cada línea salta al momento del vídeo.
- **Búsqueda** en el propio cliente (índice por idioma, insensible a tildes y acentos) con sugerencias en cabecera, página de resultados y atajo `/`.
- **Seis cursos**: 1 Primeros pasos, 2 Diseño y gestión de cursos, 3 Conversaciones, 4 Documentos y series de lecciones, 5 Corrección, fichas interactivas y plantillas, 6 Administración para responsables de IT (sin creación de contenido, con planes de estudio, roles, seguridad y privacidad, y compartición).
- **Audiencia:** español neutro para México y Chile (tuteo), y portugués de Brasil ("você").

## Estructura
```
content/
  config.mjs      URLs, idiomas, IDs de secciones, roles y cursos
  es.mjs          contenido en español (cursos, lecciones, secciones, países, FAQ)
  pt-BR.mjs       contenido en portugués de Brasil (mismos IDs y estructura; validado)
  labels.mjs      textos de página en ambos idiomas
scripts/build.mjs Generador estático: valida paridad entre idiomas, genera páginas, búsqueda y sitemap
assets/css/help.css · assets/js/help.js
video/            Pipeline de vídeo (grabación, narración, ensamblado, subtítulos). Ver video/README.md
dist/             Salida generada (no se versiona)
```

## Comandos
```bash
npm run build          # genera dist/ayuda/... (base /ayuda, para producción)
npm run build:local    # genera dist/ desde la raíz (para probar en local)
npm run serve          # sirve dist/ en http://localhost:8080 (con build:local)
```

## Añadir o cambiar contenido
1. Edita `content/es.mjs` **y** `content/pt-BR.mjs` con los mismos IDs, el mismo orden y los mismos índices de respuesta en los cuestionarios. El build se detiene si no coinciden.
2. Regenera con `npm run build`. El build avisa de las lecciones sin vídeo publicado.
3. Para un vídeo nuevo, coloca `<lección>.mp4` y `<lección>.vtt` en `video/out/es/` o `video/out/pt-br/` (por ejemplo `1-1.mp4`); el build lo incorpora.

## Próximos pasos sugeridos
1. Autorizar `sevenai.es` en el entorno y validar la cuenta demo: confirmar etiquetas y flujos.
2. Escribir los guiones de las 23 lecciones (plantilla en `video/scenes/_plantilla.json`) y grabar ES y PT.
3. Revisión nativa de pt-BR y de la pedagogía; prueba de audición de la voz.
4. Decidir el alojamiento definitivo bajo `sevenai.es/ayuda` y la marca oficial (tokens CSS).
5. Por seguridad: las credenciales de la cuenta demo se compartieron en esta conversación. Conviene cambiarlas después de la sesión de grabación. No se han escrito en ningún archivo.
