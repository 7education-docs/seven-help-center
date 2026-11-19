# Validación de la interfaz de Seven Assistant (cuenta demo, solo lectura)

Fecha: 2026-11-17. Revisado con sesión iniciada en sevenai.es/educa, sin crear, editar ni borrar datos.

## Estructura real del menú (barra lateral, solo iconos)
| Sección (aria-label) | URL | Contenido observado |
|---|---|---|
| Conversaciones | /educa | Chat con el asistente; tarjetas "Series de lecciones", "Tareas de feedback", "Cursos" en la portada |
| Cursos | /educa/courses | Pestañas "Mis cursos" y "Plantillas"; botones "Unirse a un curso", "Importar curso", "Crear curso" |
| Biblioteca | /educa/library | "Crear rápido": "Subir documento", "Serie de lecciones", "Generar con IA", "Ficha interactiva"; buscador "Buscar en todo el contenido" |
| Plantillas | /educa/ai-agents | Lista de plantillas (asistentes de IA); botones "Nuevo Plantilla" y "Crear Plantilla" |

Menú de cuenta (avatar "HC"): Aviso legal, Privacidad, Términos de servicio, Licencias, **Configuración**, **Idioma**, Canjear un cupón, **Gestionar tareas**, **Gestionar carpetas compartidas**, ¿Qué hay de nuevo?, Iniciar tutorial, Ayuda, Sitio web, Comentarios, Cerrar sesión.

## Diferencias con el contenido escrito
- La sección se llama **"Tareas de feedback"** (no "Tareas de corrección"); aparece como tarjeta en la portada.
- **Documentos, Series de lecciones y Fichas interactivas** no son secciones propias del menú: se crean desde **Biblioteca** ("Crear rápido").
- **"Plantillas"** del menú son asistentes de IA (`/educa/ai-agents`), no modelos de documento. Las plantillas de curso están dentro de **Cursos → Plantillas**.
- **Configuración** y **Idioma** están en el menú de cuenta, no en la barra lateral.
- Hay textos con error de concordancia en la interfaz ("Nuevo Plantilla"); se graban tal cual, pero hay que tenerlo en cuenta en los guiones.
- La cuenta ya tiene un curso ("Ecuaciones de…") que no se ha tocado.

## Pendiente antes de grabar
- Reescribir los pasos de `content/es.mjs` y `content/pt-BR.mjs` con estos nombres (secciones 4 y 5 sobre todo).
- Validar el flujo de creación de curso y de tarea de feedback con un usuario que pueda crear contenido sin afectar a datos reales (cuenta de pruebas dedicada).
- Revisar en el idioma portugués (Idioma en el menú de cuenta) la traducción de cada nombre de sección.
- Capturas de referencia: `scratchpad/explore/*.png` (no se versionan).

## Flujos recorridos en la cuenta demo (con creación de contenido de prueba)
- **Crear curso** (Cursos → Crear curso): asistente de 3 pasos: *Datos básicos* (Nombre del curso, Asignatura, Clase o curso escolar, Descripción, Portada) → *Elegir contenido* (Vacío, Todas las plantillas, Copiar, Planificar con IA) → *Revisar y crear* (Atrás, Crear).
- **Curso creado**: pestañas Vista general, Citas, Contenidos compartidos, Participantes, Configuración. Invitación al alumnado por código o enlace. Estructura por **secciones** (por defecto "General") con el botón "Añadir actividad o material".
- **Añadir a «General»** ofrece: Crear con IA, Material (archivo, vídeo o cuestionario H5P), Texto, Ficha de trabajo, Tarea con comentarios, Entrega, Unidad didáctica, Agente de IA, Enlace, Nota.
- **Biblioteca → Crear rápido**: Subir documento (PDF, vídeo o página web), Serie de lecciones (Generar con IA), **Tarea de corrección y feedback** (Para sus alumnos), Ficha interactiva (Beta, con ayuda de IA).
- **Herramientas de IA en Conversaciones** (lista del menú del compositor): Smart, Serie de clases, Ficha de trabajo, H5P, Diferenciación, Deberes, Imagen, Corrección, Texto de audición, Búsqueda web.
- **Menú de cuenta**: Configuración, Idioma, Gestionar tareas, Gestionar carpetas compartidas.

## Prueba de grabación
- Lección 1.3 grabada en la app real a partir de la sesión guardada: `video/review/es/1-3.mp4` (38 s, 9 subtítulos). Verificada la alineación de escenas con fotogramas. **No publicada**: su texto debe corregirse antes (ver las diferencias de arriba).

## Datos de la cuenta demo
- Se ha creado un curso de prueba: **"Prueba Help Center (borrar después)"**. No lo he borrado porque no borro nada en la cuenta; conviene eliminarlo a mano.
- La sesión guardada (`video/work/auth-demo.json`) da acceso a la cuenta: bórrala al terminar.

## Exploración ampliada (cuenta demo, 17-nov-2026)

### Cursos
- **Vista general del curso**: vistas "Lista con vista previa", "Mosaicos" y "Secciones como mosaicos". Pestañas: Vista general, Citas, Contenidos compartidos, Participantes, Configuración, y "Ver como estudiante".
- **Invitación al alumnado**: código y enlace público de inscripción (quien tenga el enlace puede unirse sin cuenta con solo un nombre), con "Generar nuevo código".
- **IA para el alumnado**: conmutador "IA para el alumnado" (el alumnado puede preguntar a la IA sobre los contenidos del curso; el profesorado siempre puede usarla).
- **Contenidos compartidos**: pestaña con botón "Añadir" y secciones (p. ej. "General").
- **Plantillas de curso** (Cursos → Plantillas, beta): unidades didácticas adoptables como curso propio. Filtros: País (**Alemania, Suiza, España**), Materia (Biología y Geología, Lengua Castellana y Literatura, Matemáticas), Curso (1.º–4.º ESO), Tipo de centro (Colegio concertado, Colegio privado, IES). Hay 12 plantillas; ninguna para México, Chile o Brasil.

### Biblioteca
- **Mi biblioteca** (/educa/library/documents): columnas Contenido, Tipo, Fecha de modificación; vacía en la cuenta demo.
- **Serie de lecciones** (/educa/library/lesson-series): acciones "Generar con IA" y "Crear". Formulario "Crear serie de lecciones": Tema* (obligatorio), Asignatura, Curso, Idioma, Descripción.
- **Tareas de corrección y feedback** (/educa/library/feedback-tasks): "Generar con IA" y "Crear".
- **Ficha interactiva** = "Crear hoja de trabajo" (/educa/library/worksheets/create): asistente de 3 pasos *Contexto → Fuentes → Análisis y ajuste*. Campos: Tema*, Asignatura, Nivel escolar, Nivel de dificultad, Idioma, Extensión (Prueba corta, Hoja de ejercicios, Material de apoyo, Examen), páginas (1 página…), número de ejercicios (Automático), densidad de texto (Compacto, Equilibrado, Detallado), "Avanzado", "Instrucciones adicionales".

### Conversaciones
- Portada: saludo, compositor ("Pregunta cualquier cosa, usa / o @…"), selector de modo "Dinámico", tarjetas de Series de lecciones, Tareas de feedback, Cursos y Actividad.
- Herramientas del compositor: Smart, Serie de clases, Búsqueda web, Ficha de trabajo, H5P, Diferenciación, Deberes, Imagen, Corrección, Texto de audición.

### Plantillas (asistentes de IA)
- /educa/ai-agents: "Nuevo Plantilla" / "Crear Plantilla"; estado vacío "No se encontraron Plantillas" (sic).

### Menú de cuenta y carpetas
- Configuración, Idioma (no he leído sus opciones todavía), Gestionar tareas, Gestionar carpetas compartidas.
- **Carpetas compartidas**: "Unirse a carpeta con token de acceso" y "Nueva carpeta"; vacío en la cuenta demo.

### Pendiente de explorar
- Opciones exactas de Idioma (¿español y portugués de Brasil?) y cambio de idioma completo.
- Qué produce realmente la IA en una serie, una ficha o una tarea (requiere generar contenido de prueba).
- Participantes del curso y permisos por rol.

## Estado del contenido tras la corrección
- **Corregido (ES y PT-BR)**: 1.1 (funciones y menú), 1.2 (menú de cuenta e idioma), 1.3 (barra lateral, Cursos, Biblioteca, Plantillas, menú de cuenta; pregunta de repaso), 2.2 (asistente "Crear curso" y "Planificar con IA").
- **Pendiente**: 2.3 a 2.5, las secciones 3 a 6 (Conversaciones, Documentos, Series, Corrección, Fichas, Plantillas, IT), las páginas de sección y la página de rutas, que aún usan los nombres antiguos.
- **Traducción PT**: los nombres de la interfaz en portugués (p. ej. "Meus cursos", "Criar rápido", "Gerenciar pastas compartilhadas") son traducciones propias: la interfaz en portugués no se ha verificado todavía.
- **Vídeo 1.3**: `video/review/es/1-3.mp4` grabado antes de esta corrección. Su narración ya coincide con la interfaz real, pero conviene regrabarlo cuando se revise el texto.

## Corrección ampliada (17-nov-2026)
- Parches en `content/patches/ui-verificada.mjs`, aplicados por el generador: lecciones 2.3–6.4 (ES y PT-BR) y las páginas de sección de Cursos, Conversaciones, Documentos, Series, Tareas, Fichas, Plantillas y Configuración.
- Pendiente de verificar: permisos por rol (lección 6.2 se mantiene conservadora), nombres de la interfaz en portugués, y el texto de la plantilla de curso para Brasil, México y Chile, que no existe en la plataforma.
- Los vídeos siguen sin regrabar; la 1.3 de prueba se regrabará con estos textos.
