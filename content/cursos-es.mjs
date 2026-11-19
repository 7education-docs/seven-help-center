// Cursos, roles y secciones del centro de ayuda — Español (México, Chile).
// Sustituye a los campos courses, roles y sections de content/es.mjs en el build.
// Interfaz verificada en la cuenta demo (17-nov-2026). La herramienta Cursos está en beta.
export default {
  courses: [
    {
      id: 'primeros-pasos',
      slug: 'primeros-pasos',
      title: 'Primeros pasos con Seven Assistant',
      summary: 'Qué es Seven Assistant, cómo entrar, elegir el idioma y moverte por la barra lateral desde el primer día.',
      level: 'beginner',
      duration: '20 min',
      audience: ['Docentes', 'Coordinación académica', 'Jefatura de estudios y tutoría', 'Responsables de IT'],
      roles: ['docente', 'coordinacion', 'jefatura-tutoria', 'responsable-it'],
      objectives: ['Explicar qué hace Seven Assistant y qué no hace.', 'Cambiar el idioma de la interfaz.', 'Ubicar cada sección desde la barra lateral.'],
      lessons: [
        {
          id: '1.1', slug: 'que-es-seven-assistant', title: 'Qué es Seven Assistant', duration: '6 min',
          summary: 'La herramienta, para qué sirve y cómo se organiza en las áreas que usarás cada día.',
          objectives: ['Explicar la herramienta con tus palabras.', 'Distinguir las áreas principales de la plataforma.'],
          steps: [
            { t: 'Un asistente de trabajo docente', b: 'Seven Assistant te ayuda a planificar, crear materiales, redactar y revisar trabajos. Propone borradores; tú decides qué se usa con tus alumnos.' },
            { t: 'Las áreas principales', b: 'En la barra lateral verás Conversaciones, Cursos, Biblioteca y Plantillas. Cursos reúne tus cursos. Biblioteca guarda documentos, series de lecciones, tareas de corrección y fichas interactivas.' },
            { t: 'Qué esperar de la beta', b: 'La herramienta Cursos está en beta: algunas pantallas y opciones pueden cambiar. Esta ayuda se actualiza con cada cambio importante.' },
          ],
          tips: ['Empieza por una necesidad concreta: una clase de la próxima semana, una rúbrica o un examen.', 'Revisa cada resultado antes de compartirlo con alumnos o familias.'],
          quiz: [
            { q: '¿Cuál es la forma recomendada de usar lo que propone el asistente?', options: ['Publicarlo tal cual, porque ya está listo.', 'Revisarlo y adaptarlo a tu grupo antes de usarlo.', 'Usarlo solo si el asistente confirma que es correcto.'], answer: 1, explain: 'El asistente propone; tú validas el contenido según tu grupo, tu nivel y tu criterio.' },
          ],
        },
        {
          id: '1.2', slug: 'cuenta-idioma-y-perfil', title: 'Tu cuenta y el idioma de la interfaz', duration: '6 min',
          summary: 'Cómo encontrar el menú de cuenta, cambiar el idioma y revisar tu perfil.',
          objectives: ['Abrir el menú de cuenta.', 'Cambiar el idioma de la interfaz.'],
          steps: [
            { t: 'Abre el menú de cuenta', b: 'Pulsa el avatar con tus iniciales, en la parte inferior de la barra lateral. Ahí encontrarás Configuración e Idioma.' },
            { t: 'Elige el idioma', b: 'En Idioma, elige español o portugués de Brasil para la interfaz. Los textos que tú escribas se quedan en el idioma en que los creaste.' },
            { t: 'Revisa tu perfil', b: 'En Configuración, confirma tus datos y mantenlos al día si cambias de centro o de nivel.' },
          ],
          tips: ['Cierra sesión al terminar si usas un equipo compartido.'],
          quiz: [
            { q: '¿Dónde cambias el idioma de la interfaz?', options: ['En la barra lateral, con el icono de Cursos.', 'En el menú de cuenta, dentro de Idioma.', 'En cada curso, en Configuración.'], answer: 1, explain: 'El idioma está en el menú de cuenta, no en la barra lateral ni dentro de cada curso.' },
          ],
        },
        {
          id: '1.3', slug: 'recorrido-por-la-interfaz', title: 'Recorrido por la interfaz', duration: '8 min',
          summary: 'Qué hay en cada área de la barra lateral y dónde se crea cada cosa.',
          objectives: ['Elegir el área correcta para cada tarea.', 'Localizar Cursos, Biblioteca y Plantillas.'],
          steps: [
            { t: 'Conversaciones', b: 'Es la página de inicio y el espacio para preguntar, pedir borradores e iterar con el asistente.' },
            { t: 'Cursos', b: 'Aquí creas cursos, te unes a uno o lo importas. La pestaña Plantillas muestra unidades didácticas adoptables.' },
            { t: 'Biblioteca', b: 'Aquí subes documentos y creas series de lecciones, tareas de corrección y fichas interactivas.' },
            { t: 'Plantillas', b: 'El icono de estrellas abre tus asistentes de IA, con instrucciones propias. No son las plantillas de curso.' },
          ],
          tips: ['Si no sabes dónde trabajar, pregúntate si el resultado será un material, un diálogo o un curso con alumnos.'],
          quiz: [
            { q: 'Quieres crear un curso con sus sesiones y materiales. ¿Dónde empiezas?', options: ['En Biblioteca, con Crear rápido.', 'En Cursos, con Crear curso.', 'En Plantillas, con Crear Plantilla.'], answer: 1, explain: 'Los cursos se crean en Cursos. Biblioteca guarda materiales sueltos, y Plantillas son asistentes de IA.' },
          ],
        },
      ],
    },
    {
      id: 'cursos-crear-organizar',
      slug: 'cursos-crear-organizar',
      title: 'Cursos: crear y organizar',
      summary: 'Cómo crear un curso con el asistente de tres pasos, organizar su contenido en secciones y elegir la vista que mejor se lea.',
      level: 'intermediate',
      duration: '45 min',
      audience: ['Docentes', 'Coordinación académica', 'Jefatura de estudios y tutoría'],
      roles: ['docente', 'coordinacion', 'jefatura-tutoria'],
      objectives: ['Crear un curso completo con el asistente.', 'Organizar el contenido en secciones con un orden claro.', 'Elegir la vista y la navegación del curso.', 'Reutilizar un curso con plantillas.'],
      lessons: [
        {
          id: '2.1', slug: 'que-es-un-curso', title: 'Qué es un curso en Seven Assistant', duration: '7 min',
          summary: 'Un curso reúne secciones, materiales y actividades para un grupo concreto, y se comparte con el alumnado.',
          objectives: ['Explicar qué contiene un curso.', 'Identificar las pestañas del curso.'],
          steps: [
            { t: 'Un curso para un grupo', b: 'Cada curso es para un grupo y una asignatura. Dentro hay secciones, materiales y actividades. El alumnado entra con un código o un enlace.' },
            { t: 'Las pestañas del curso', b: 'Vista general muestra el contenido. Citas gestiona las sesiones. Contenidos compartidos reúne lo que compartes. Participantes lista a quien forma parte. Configuración ajusta el curso.' },
            { t: 'Beta', b: 'La herramienta Cursos está en beta. Revisa las novedades antes de empezar un curso largo.' },
          ],
          tips: ['Crea el curso antes del inicio del periodo, para tener tiempo de revisarlo.'],
          quiz: [
            { q: '¿Qué contiene un curso?', options: ['Solo un título y una fecha.', 'Secciones, materiales y actividades para un grupo.', 'Únicamente las conversaciones del docente.'], answer: 1, explain: 'El curso se organiza en secciones con materiales y actividades para su grupo.' },
          ],
        },
        {
          id: '2.2', slug: 'crear-un-curso-con-el-asistente', title: 'Crear un curso con el asistente de tres pasos', duration: '10 min',
          summary: 'Datos básicos, contenido inicial y revisión: el recorrido completo de "Crear curso".',
          objectives: ['Completar los datos básicos del curso.', 'Elegir el contenido inicial.', 'Revisar antes de crear.'],
          steps: [
            { t: 'Paso 1: Datos básicos', b: 'En Cursos, pulsa Crear curso. Escribe el nombre del curso, la asignatura, la clase o curso escolar y una descripción. Puedes añadir una portada.' },
            { t: 'Paso 2: Elegir contenido', b: 'Elige cómo empezar: Vacío, Todas las plantillas, Copiar o Planificar con IA. Con Vacío partes de cero; con una plantilla partes de una unidad ya preparada.' },
            { t: 'Paso 3: Revisar y crear', b: 'Revisa los datos. Atrás te permite corregir antes de pulsar Crear.' },
          ],
          tips: ['Usa un nombre que identifique grupo y materia, por ejemplo "Matemáticas · 2.º secundaria".', 'Con Planificar con IA, pide la estructura por unidades y revísala antes de usarla.'],
          quiz: [
            { q: '¿Qué ofrece el paso "Elegir contenido"?', options: ['Solo una portada.', 'Vacío, Todas las plantillas, Copiar o Planificar con IA.', 'La lista de alumnos.'], answer: 1, explain: 'En este paso eliges desde dónde empieza el contenido del curso.' },
          ],
        },
        {
          id: '2.3', slug: 'secciones-y-orden', title: 'Secciones y orden del contenido', duration: '10 min',
          summary: 'Cómo crear secciones, cambiar su orden y dar a cada una un nombre que el alumnado entienda.',
          objectives: ['Crear una sección.', 'Ordenar el contenido.', 'Nombrar secciones y actividades con claridad.'],
          steps: [
            { t: 'La sección General', b: 'Al crear un curso aparece la sección General, con el botón Añadir actividad o material.' },
            { t: 'Crear secciones', b: 'Usa Añadir sección para crear más secciones, por ejemplo una por unidad o por semana.' },
            { t: 'Orden', b: 'Ordena las secciones de lo conocido a lo nuevo, y deja una sesión de repaso antes de cada evaluación.' },
            { t: 'Nombres claros', b: 'Usa títulos que digan lo que hará el alumnado: "Comparar fracciones con distinto denominador" es mejor que "Fracciones".' },
          ],
          tips: ['Una sección por unidad es fácil de seguir. Más de seis secciones suele ser demasiado para un curso.'],
          quiz: [
            { q: '¿Qué botón usas para crear una nueva sección?', options: ['Añadir sección.', 'Crear curso.', 'Generar nuevo código.'], answer: 0, explain: 'Añadir sección crea una sección nueva dentro del curso.' },
          ],
        },
        {
          id: '2.4', slug: 'vistas-y-navegacion', title: 'Vistas del curso y navegación entre contenidos', duration: '8 min',
          summary: 'Lista, mosaicos y secciones como mosaicos: cuándo conviene cada vista y cómo activar la navegación entre contenidos.',
          objectives: ['Elegir la vista del curso.', 'Activar la navegación entre contenidos.'],
          steps: [
            { t: 'Lista', b: 'Muestra títulos y tipos, uno debajo de otro. Es la vista más compacta.' },
            { t: 'Lista con vista previa', b: 'Muestra las primeras líneas de cada contenido. Útil para revisar sin abrir.' },
            { t: 'Mosaicos y secciones como mosaicos', b: 'Mosaicos muestra los contenidos como tarjetas. Secciones como mosaicos muestra cada sección con su propia página.' },
            { t: 'Contenido anterior y siguiente', b: 'Si la activas en Configuración, cada página de contenido termina con enlaces al anterior y al siguiente.' },
          ],
          tips: ['Para el alumnado en secundaria, Lista con vista previa suele ser la más clara.', 'Usa "Ver como estudiante" para comprobar cómo se ve el curso sin cambiar nada.'],
          quiz: [
            { q: '¿Qué vista muestra cada sección con su propia página?', options: ['Lista.', 'Mosaicos.', 'Secciones como mosaicos.'], answer: 2, explain: 'Secciones como mosaicos lleva a una página para cada sección.' },
          ],
        },
        {
          id: '2.5', slug: 'plantillas-copiar-e-importar', title: 'Plantillas de curso, copiar e importar', duration: '10 min',
          summary: 'Cómo adoptar una unidad didáctica de Plantillas, cómo copiar un curso y cómo importarlo desde un archivo.',
          objectives: ['Adoptar una plantilla de curso.', 'Importar un curso desde un archivo.'],
          steps: [
            { t: 'Plantillas de curso', b: 'En Cursos, abre la pestaña Plantillas. Filtra por país, materia, curso o tipo de centro, y pulsa Adoptar en la unidad que necesites.' },
            { t: 'Limitaciones actuales', b: 'Las plantillas actuales son unidades de España, Alemania y Suiza. Adóptala y adáptala a tu currículo, sin darla por válida tal cual.' },
            { t: 'Copiar al crear', b: 'En el paso Elegir contenido de Crear curso, la opción Copiar reutiliza un curso que ya tienes.' },
            { t: 'Importar un curso', b: 'En Cursos, Importar curso recibe un archivo del curso y lo añade a tu lista.' },
          ],
          tips: ['Antes de adoptar una plantilla, revisa las fechas y los nombres de las actividades.'],
          quiz: [
            { q: '¿Dónde están las plantillas de curso?', options: ['En Plantillas, el icono de estrellas.', 'En Cursos, en la pestaña Plantillas.', 'En Biblioteca, con Crear rápido.'], answer: 1, explain: 'Las plantillas de curso están dentro de Cursos. El icono de estrellas son asistentes de IA.' },
          ],
        },
      ],
    },
    {
      id: 'cursos-actividades',
      slug: 'cursos-actividades',
      title: 'Cursos: actividades y materiales',
      summary: 'Los tipos de actividad y material de un curso, cuándo usar cada uno y cómo elegir según el objetivo.',
      level: 'intermediate',
      duration: '50 min',
      audience: ['Docentes', 'Coordinación académica'],
      roles: ['docente', 'coordinacion'],
      objectives: ['Distinguir material, actividad y evaluación.', 'Usar cada tipo de actividad con sentido pedagógico.', 'Elegir el tipo adecuado para cada objetivo.'],
      lessons: [
        {
          id: '3.1', slug: 'material-y-texto', title: 'Material y texto', duration: '8 min',
          summary: 'Materiales de lectura, archivos y vídeos para acompañar la clase, sin evaluación.',
          objectives: ['Subir un material a una sección.', 'Escribir un texto de lectura en el propio curso.'],
          steps: [
            { t: 'Material', b: 'En una sección, Añadir actividad o material, y elige Material: puede ser un archivo, un vídeo o un cuestionario H5P.' },
            { t: 'Texto', b: 'Elige Texto para un material de lectura que se abre en su propia página.' },
            { t: 'Cuándo usarlos', b: 'Son para acompañar la clase: lecturas, esquemas o vídeos. No se califican.' },
          ],
          tips: ['Dale a cada material un título que diga para qué sirve: "Lectura previa · ciclo del agua".'],
          quiz: [
            { q: '¿Qué tipo es para una lectura que se abre en su propia página?', options: ['Nota.', 'Texto.', 'Entrega.'], answer: 1, explain: 'Texto crea un material de lectura en su propia página.' },
          ],
        },
        {
          id: '3.2', slug: 'ficha-de-trabajo-y-unidad', title: 'Ficha de trabajo y unidad didáctica', duration: '10 min',
          summary: 'La ficha de trabajo para practicar y la unidad didáctica para llevar una unidad completa al curso.',
          objectives: ['Añadir una ficha de trabajo.', 'Añadir una unidad didáctica completa.'],
          steps: [
            { t: 'Ficha de trabajo', b: 'Elige Ficha de trabajo para añadir una hoja de ejercicios al curso. Sirve para práctica en clase o en casa.' },
            { t: 'Unidad didáctica', b: 'Elige Unidad didáctica para añadir una unidad completa, con su contenido, a la sección.' },
            { t: 'Revisión', b: 'Después de añadirlas, revisa que los títulos y el orden tengan sentido para el alumnado.' },
          ],
          tips: ['Usa la ficha de trabajo para práctica y la unidad para planificar un bloque entero.'],
          quiz: [
            { q: '¿Para qué sirve una ficha de trabajo dentro del curso?', options: ['Para cobrar una cuota.', 'Para practicar con ejercicios.', 'Para crear el curso.'], answer: 1, explain: 'La ficha de trabajo es un material de práctica con ejercicios.' },
          ],
        },
        {
          id: '3.3', slug: 'tarea-con-comentarios-y-entrega', title: 'Tarea con comentarios y entrega', duration: '12 min',
          summary: 'Cuándo usar una tarea con comentarios y cuándo una entrega, y cómo recibir el trabajo del alumnado.',
          objectives: ['Diferenciar tarea con comentarios y entrega.', 'Configurar la fecha y la hora de entrega.'],
          steps: [
            { t: 'Tarea con comentarios', b: 'Es una tarea que puede recibir comentarios de la IA, según su configuración. Úsala para trabajos que quieres revisar con retroalimentación.' },
            { t: 'Entrega', b: 'El alumnado sube archivos en una entrega. Tiene un título, una descripción, una fecha y una hora de entrega.' },
            { t: 'Fecha y hora', b: 'Define la fecha y la hora límite al crear la entrega. Revísalas antes de publicar.' },
            { t: 'Cuándo usar cuál', b: 'Usa una entrega cuando hay un archivo que recibir. Usa una tarea con comentarios cuando quieres retroalimentación sobre el trabajo.' },
          ],
          tips: ['Escribe en la descripción qué debe entregar el alumnado y en qué formato.'],
          quiz: [
            { q: '¿Qué tipo recibe archivos del alumnado?', options: ['Nota.', 'Entrega.', 'Texto.'], answer: 1, explain: 'La entrega es el tipo pensado para que el alumnado suba archivos.' },
          ],
        },
        {
          id: '3.4', slug: 'agente-enlace-y-nota', title: 'Agente de IA, enlace y nota', duration: '10 min',
          summary: 'Un agente de IA para el alumnado, un enlace a un recurso externo y una nota breve dentro de la sección.',
          objectives: ['Crear un agente de IA para el curso.', 'Añadir un enlace y una nota.'],
          steps: [
            { t: 'Agente de IA', b: 'Elige Agente de IA para poner a disposición del alumnado un asistente con instrucciones tuyas. Escribe su nombre y sus instrucciones.' },
            { t: 'Enlace', b: 'Elige Enlace para apuntar a una página web. Escribe el texto que verá el alumnado y la dirección.' },
            { t: 'Nota', b: 'Elige Nota para un texto breve directamente en la sección, por ejemplo un aviso o una instrucción.' },
          ],
          tips: ['Un agente de IA para el alumnado debe tener instrucciones claras: qué ayuda ofrecer y qué no debe resolver directamente.'],
          quiz: [
            { q: '¿Qué tipo añade un texto breve directamente en la sección?', options: ['Enlace.', 'Nota.', 'Agente de IA.'], answer: 1, explain: 'La nota es un texto breve dentro de la sección.' },
          ],
        },
        {
          id: '3.5', slug: 'elegir-el-tipo-de-actividad', title: 'Cómo elegir el tipo de actividad', duration: '8 min',
          summary: 'Una guía para decidir entre material, práctica, tarea y entrega según el objetivo que quieres comprobar.',
          objectives: ['Elegir el tipo según el objetivo.', 'Evitar usar una entrega para lo que es práctica.'],
          steps: [
            { t: 'Quiero que el alumnado lea o vea algo', b: 'Material o Texto.' },
            { t: 'Quiero que practique', b: 'Ficha de trabajo.' },
            { t: 'Quiero que me entregue un archivo', b: 'Entrega.' },
            { t: 'Quiero retroalimentación sobre su trabajo', b: 'Tarea con comentarios.' },
            { t: 'Quiero un asistente para sus dudas', b: 'Agente de IA, con instrucciones claras.' },
          ],
          tips: ['Si la actividad no se califica ni se corrige, probablemente es práctica o material.'],
          quiz: [
            { q: 'Quieres que el alumnado practique ejercicios. ¿Qué tipo eliges?', options: ['Entrega.', 'Ficha de trabajo.', 'Enlace.'], answer: 1, explain: 'La ficha de trabajo es el tipo pensado para practicar.' },
          ],
        },
      ],
    },
    {
      id: 'cursos-compartir-seguimiento',
      slug: 'cursos-compartir-seguimiento',
      title: 'Cursos: compartir y seguimiento',
      summary: 'Cómo invitar al alumnado con código o enlace, qué puede hacer con la IA, cómo ver el curso como estudiante y cómo hacer seguimiento.',
      level: 'intermediate',
      duration: '40 min',
      audience: ['Docentes', 'Coordinación académica', 'Jefatura de estudios y tutoría', 'Responsables de IT'],
      roles: ['docente', 'coordinacion', 'jefatura-tutoria', 'responsable-it'],
      objectives: ['Invitar al alumnado con código o enlace.', 'Decidir el uso de la IA por parte del alumnado.', 'Revisar el curso como lo ve el alumnado.', 'Hacer seguimiento con participantes y citas.'],
      lessons: [
        {
          id: '4.1', slug: 'codigo-y-enlace-de-inscripcion', title: 'Código y enlace de inscripción', duration: '8 min',
          summary: 'Cómo compartir un curso con el alumnado y cuándo conviene generar un código nuevo.',
          objectives: ['Compartir el código y el enlace.', 'Generar un código nuevo si hace falta.'],
          steps: [
            { t: 'El código', b: 'En la vista general del curso aparece el código de inscripción. El alumnado lo escribe en Unirse a un curso.' },
            { t: 'El enlace público', b: 'El enlace de inscripción deja entrar a quien lo tenga, sin cuenta, con solo un nombre.' },
            { t: 'Generar un código nuevo', b: 'Si el enlace se filtra o cambia el grupo, pulsa Generar nuevo código. El enlace anterior deja de servir.' },
          ],
          tips: ['Comparte el enlace solo con el grupo. Si es un curso de un colegio, revisa con la coordinación antes de publicarlo.'],
          quiz: [
            { q: 'El enlace se ha filtrado a personas que no son del grupo. ¿Qué haces?', options: ['Nada: el enlace no se puede cambiar.', 'Pulsar Generar nuevo código.', 'Borrar el curso.'], answer: 1, explain: 'Generar nuevo código sustituye el acceso anterior sin borrar el curso.' },
          ],
        },
        {
          id: '4.2', slug: 'unirse-a-un-curso', title: 'Unirse a un curso (vista del alumnado)', duration: '6 min',
          summary: 'Lo que ve el alumnado al unirse con un código y cómo comprobarlo desde la vista de estudiante.',
          objectives: ['Explicar al alumnado cómo unirse.', 'Comprobar el curso con la vista de estudiante.'],
          steps: [
            { t: 'Unirse a un curso', b: 'El alumnado entra en Cursos y elige Unirse a un curso. Escribe el código de inscripción.' },
            { t: 'Vista de estudiante', b: 'Con Ver como estudiante ves el curso como lo ve el alumnado. Aparece el aviso "Aquí no se cambia nada".' },
            { t: 'Salir de la vista', b: 'Pulsa Salir de la vista para volver a tu vista de docente.' },
          ],
          tips: ['Haz la prueba con la vista de estudiante antes de la primera clase.'],
          quiz: [
            { q: '¿Qué te permite comprobar la vista de estudiante?', options: ['Cómo se ve el curso para el alumnado, sin cambiar nada.', 'Las notas de cada alumno.', 'El código de otro curso.'], answer: 0, explain: 'La vista de estudiante muestra el curso como lo ve el alumnado, sin cambiar nada.' },
          ],
        },
        {
          id: '4.3', slug: 'ia-para-el-alumnado', title: 'IA para el alumnado y Tutor de IA', duration: '10 min',
          summary: 'Cómo activar la IA para el alumnado y qué hace el Tutor de IA: pistas y preguntas, no soluciones completas.',
          objectives: ['Activar o desactivar la IA para el alumnado.', 'Explicar qué hace el Tutor de IA.'],
          steps: [
            { t: 'IA para el alumnado', b: 'Es un conmutador del curso. Si está activo, el alumnado puede preguntar a la IA sobre los contenidos del curso.' },
            { t: 'Lo que siempre puede usar el profesorado', b: 'El profesorado puede usar la IA del curso aunque el alumnado no la tenga activa.' },
            { t: 'Tutor de IA', b: 'El Tutor de IA da pistas y hace preguntas, pero no da soluciones completas. Es útil para que el alumnado razone.' },
          ],
          tips: ['Explica al alumnado para qué sirve el tutor y qué tipo de ayuda puede esperar.', 'Revisa algunas conversaciones del alumnado para detectar dudas comunes.'],
          quiz: [
            { q: '¿Qué da el Tutor de IA al alumnado?', options: ['La solución completa del ejercicio.', 'Pistas y preguntas, sin solución completa.', 'La nota del trabajo.'], answer: 1, explain: 'El Tutor de IA está pensado para guiar el razonamiento, no para dar respuestas completas.' },
          ],
        },
        {
          id: '4.4', slug: 'participantes-contenidos-y-citas', title: 'Participantes, contenidos compartidos y citas', duration: '12 min',
          summary: 'Seguimiento del curso: quién participa, qué materiales compartes y cómo organizar las citas con el grupo.',
          objectives: ['Revisar los participantes del curso.', 'Gestionar contenidos compartidos.', 'Crear una cita del curso.'],
          steps: [
            { t: 'Participantes', b: 'La pestaña Participantes muestra quién forma parte del curso. Revísala al empezar y al terminar.' },
            { t: 'Contenidos compartidos', b: 'La pestaña Contenidos compartidos reúne lo que compartes. Desde Añadir puedes incluir materiales.' },
            { t: 'Citas', b: 'La pestaña Citas muestra las próximas. Crear cita añade una sesión con su fecha, para que el grupo la vea en el curso.' },
          ],
          tips: ['Revisa los participantes cada semana durante las primeras semanas del curso.'],
          quiz: [
            { q: '¿Dónde organizas las sesiones con fecha?', options: ['En Participantes.', 'En Citas.', 'En Configuración del menú de cuenta.'], answer: 1, explain: 'Las citas del curso se gestionan en la pestaña Citas.' },
          ],
        },
      ],
    },
    {
      id: 'biblioteca-asistente',
      slug: 'biblioteca-asistente',
      title: 'Conversaciones, Biblioteca y Plantillas',
      summary: 'Cómo preguntar al asistente, subir documentos, crear series de lecciones, fichas interactivas, tareas de corrección y asistentes de IA.',
      level: 'intermediate',
      duration: '55 min',
      audience: ['Docentes', 'Coordinación académica', 'Jefatura de estudios y tutoría'],
      roles: ['docente', 'coordinacion', 'jefatura-tutoria'],
      objectives: ['Usar Conversaciones y sus herramientas.', 'Subir documentos y crear series de lecciones.', 'Crear fichas interactivas y tareas de corrección.', 'Crear asistentes de IA en Plantillas.'],
      lessons: [
        {
          id: '5.1', slug: 'conversaciones-y-herramientas', title: 'Conversaciones y herramientas del asistente', duration: '10 min',
          summary: 'La página de inicio, el campo de escritura, el modo Dinámico y las herramientas del asistente.',
          objectives: ['Escribir una petición con contexto.', 'Usar una herramienta del asistente.', 'Regenerar una respuesta.'],
          steps: [
            { t: 'La página de inicio', b: 'Conversaciones es la página de inicio. Escribe en el campo "Pregunta cualquier cosa" y pulsa enviar.' },
            { t: 'Las herramientas', b: 'Con el botón + puedes usar herramientas como Serie de clases, Ficha de trabajo, Diferenciación, Corrección o Texto de audición.' },
            { t: 'Contexto', b: 'Indica país, nivel, grado, materia y tiempo. Con ese contexto, la respuesta encaja con tu grupo.' },
            { t: 'Regenerar', b: 'Si una respuesta no te convence, puedes regenerarla. El asistente no siempre acierta: revisa siempre el resultado.' },
          ],
          tips: ['Usa la herramienta adecuada antes que una pregunta larga: Serie de clases para planificar, Ficha de trabajo para practicar.'],
          quiz: [
            { q: '¿Qué herramienta del asistente sirve para planificar una secuencia de clases?', options: ['Serie de clases.', 'Texto de audición.', 'Búsqueda web.'], answer: 0, explain: 'Serie de clases está pensada para planificar clases y secuencias.' },
          ],
        },
        {
          id: '5.2', slug: 'biblioteca-documentos-y-series', title: 'Biblioteca: documentos y series de lecciones', duration: '12 min',
          summary: 'Subir documentos a Biblioteca y crear una serie de lecciones con su tema, asignatura, curso e idioma.',
          objectives: ['Subir un documento.', 'Crear una serie de lecciones.'],
          steps: [
            { t: 'Biblioteca', b: 'Entra en Biblioteca. Crear rápido muestra Subir documento, Serie de lecciones, Tarea de corrección y feedback y Ficha interactiva.' },
            { t: 'Subir documento', b: 'Pulsa Subir documento. Admite PDF, vídeo o página web. Los documentos aparecen en Mi biblioteca.' },
            { t: 'Serie de lecciones', b: 'Pulsa Serie de lecciones y después Crear. Rellena Tema, que es obligatorio, y Asignatura, Curso, Idioma y Descripción. También puedes usar Generar con IA.' },
            { t: 'Revisión', b: 'Revisa la serie antes de usarla: que las sesiones tengan sentido y que la evaluación esté marcada.' },
          ],
          tips: ['Usa un tema concreto: "Proporcionalidad directa · 2.º secundaria" da mejores series que "Matemáticas".'],
          quiz: [
            { q: '¿Qué campo es obligatorio al crear una serie de lecciones?', options: ['Descripción.', 'Tema.', 'Idioma.'], answer: 1, explain: 'El tema es el único campo marcado como obligatorio.' },
          ],
        },
        {
          id: '5.3', slug: 'fichas-interactivas', title: 'Fichas interactivas: crear hoja de trabajo', duration: '12 min',
          summary: 'El asistente de tres pasos para crear una ficha interactiva: contexto, fuentes y análisis con ajustes.',
          objectives: ['Configurar el contexto de la ficha.', 'Elegir la extensión y la densidad del texto.', 'Revisar la ficha antes de usarla.'],
          steps: [
            { t: 'Crear hoja de trabajo', b: 'En Biblioteca, pulsa Ficha interactiva. Se abre Crear hoja de trabajo, en tres pasos: Contexto, Fuentes y Análisis y ajuste.' },
            { t: 'Contexto', b: 'Indica Tema, Asignatura, Nivel escolar, Nivel de dificultad, Idioma y la extensión: prueba corta, hoja de ejercicios, material de apoyo o examen.' },
            { t: 'Fuentes', b: 'Indica de dónde sale el contenido de la ficha.' },
            { t: 'Análisis y ajuste', b: 'Revisa el número de ejercicios y la densidad del texto: compacto, equilibrado o detallado. Después genera la ficha.' },
          ],
          tips: ['Para niños pequeños o alumnado con apoyo, usa densidad compacta y un nivel de dificultad bajo.'],
          quiz: [
            { q: '¿Cuál es el primer paso de Crear hoja de trabajo?', options: ['Contexto.', 'Análisis y ajuste.', 'Fuentes.'], answer: 0, explain: 'El primer paso es Contexto, donde defines el tema, la asignatura y el nivel.' },
          ],
        },
        {
          id: '5.4', slug: 'tareas-de-correccion-y-feedback', title: 'Tareas de corrección y feedback', duration: '12 min',
          summary: 'Crear una tarea de corrección y feedback desde Biblioteca, con criterios claros y revisión de la propuesta.',
          objectives: ['Crear una tarea de corrección.', 'Definir criterios observables.', 'Revisar la corrección antes de cerrarla.'],
          steps: [
            { t: 'Tarea de corrección y feedback', b: 'En Biblioteca, pulsa Tarea de corrección y feedback. Crear crea una tarea y Generar con IA la propone a partir de tu petición.' },
            { t: 'Criterios', b: 'Escribe criterios que se puedan comprobar en el trabajo: "Argumenta con al menos dos evidencias" es mejor que "buena redacción".' },
            { t: 'Corrección', b: 'La plataforma puede corregir con comentarios por criterio. Revisa cada comentario antes de dar la nota.' },
            { t: 'Calibrar', b: 'Compara la propuesta con dos o tres trabajos corregidos por ti. Así ajustas los criterios antes de corregir al grupo.' },
          ],
          tips: ['Revisa personalmente los casos límite antes de cerrar las notas.'],
          quiz: [
            { q: '¿Qué conviene hacer antes de corregir a todo el grupo?', options: ['Publicar las notas.', 'Calibrar con algunos trabajos de distinto nivel.', 'Borrar los criterios.'], answer: 1, explain: 'Calibrar evita que la misma escala se aplique de forma distinta en cada trabajo.' },
          ],
        },
        {
          id: '5.5', slug: 'plantillas-de-asistente', title: 'Plantillas: crear tu asistente de IA', duration: '10 min',
          summary: 'Plantillas es la sección de asistentes de IA con instrucciones propias. Aquí aprendes a crear uno.',
          objectives: ['Distinguir asistentes de IA y plantillas de curso.', 'Crear un asistente con sus instrucciones.'],
          steps: [
            { t: 'Qué es una plantilla de asistente', b: 'Es un asistente de IA con instrucciones propias, para repetir un encargo en tus clases.' },
            { t: 'Crear Plantilla', b: 'En Plantillas, pulsa Crear Plantilla. La pantalla vacía muestra Crear Plantilla o Nuevo Plantilla si ya tienes alguna.' },
            { t: 'Instrucciones', b: 'Describe el papel del asistente, el tipo de respuesta y lo que no debe hacer. Cuanto más concretas, más útil es.' },
            { t: 'Revisión', b: 'Prueba el asistente con una petición real y ajusta las instrucciones si la respuesta no encaja.' },
          ],
          tips: ['No confundas este asistente con las plantillas de curso de Cursos → Plantillas.'],
          quiz: [
            { q: '¿Qué crea el botón Crear Plantilla?', options: ['Un curso completo.', 'Un asistente de IA con instrucciones propias.', 'Una lista de alumnos.'], answer: 1, explain: 'En Plantillas se crean asistentes de IA con instrucciones propias.' },
          ],
        },
      ],
    },
    {
      id: 'administracion-it',
      slug: 'administracion-it',
      title: 'Administración para responsables de IT',
      summary: 'Organiza el centro, gestiona participantes y carpetas compartidas, y revisa seguridad y privacidad. Este curso no trata de crear contenidos.',
      level: 'advanced',
      duration: '40 min',
      audience: ['Responsables de sistemas IT', 'Coordinación académica'],
      roles: ['responsable-it', 'coordinacion'],
      objectives: ['Organizar el centro y los planes de estudio.', 'Gestionar participantes y permisos.', 'Gestionar carpetas compartidas.', 'Revisar seguridad, privacidad y ubicación de datos.'],
      lessons: [
        {
          id: '6.1', slug: 'organizacion-y-planes-de-estudio', title: 'Organización del centro y planes de estudio', duration: '10 min',
          summary: 'Cómo estructurar los cursos del centro para que sean fáciles de encontrar y de gobernar.',
          objectives: ['Definir un modelo de organización.', 'Acordar nombres comunes de asignatura y curso escolar.'],
          steps: [
            { t: 'Modelo de organización', b: 'Cada curso tiene una asignatura y una clase o curso escolar, que se rellenan al crear el curso.' },
            { t: 'Nombres comunes', b: 'Antes de que los docentes creen cursos, acuerda las asignaturas y los cursos escolares del centro, para usar los mismos nombres.' },
            { t: 'Convención de títulos', b: 'Define un formato común, por ejemplo "Matemáticas · 2.º secundaria · 2026-2027".' },
            { t: 'Revisión anual', b: 'Al cerrar cada año escolar, revisa los cursos y reorganiza los nombres para el siguiente.' },
          ],
          tips: ['Documenta la convención en un único lugar y compártela con coordinación y docentes.'],
          quiz: [
            { q: '¿Qué campos se rellenan al crear un curso y ayudan a organizar el centro?', options: ['Asignatura y clase o curso escolar.', 'Solo el color de la portada.', 'La contraseña del grupo.'], answer: 0, explain: 'La asignatura y la clase o curso escolar son la base de la organización del centro.' },
          ],
        },
        {
          id: '6.2', slug: 'participantes-y-permisos', title: 'Participantes y permisos', duration: '10 min',
          summary: 'Quién participa en cada curso y qué necesita cada persona, aplicando el mínimo necesario.',
          objectives: ['Aplicar el mínimo privilegio.', 'Revisar los participantes de un curso.', 'Mantener altas, bajas y revisiones.'],
          steps: [
            { t: 'Mínimo privilegio', b: 'Da a cada persona los permisos necesarios para su función, y nada más.' },
            { t: 'Participantes del curso', b: 'La pestaña Participantes de cada curso muestra quién forma parte. Revísala al empezar y al terminar el curso.' },
            { t: 'Altas y bajas', b: 'Cuando una persona entra o sale del centro, actualiza su acceso el mismo día.' },
            { t: 'Revisión periódica', b: 'Revisa cada trimestre los participantes y las carpetas compartidas con dirección.' },
          ],
          tips: ['Evita cuentas compartidas entre varias personas: pierdes trazabilidad.'],
          quiz: [
            { q: '¿Qué principio guía la asignación de permisos?', options: ['Dar acceso total a todos.', 'El mínimo necesario para cada función.', 'Dar permisos solo a dirección.'], answer: 1, explain: 'Limitar los permisos a lo necesario reduce el impacto de un error o de una cuenta comprometida.' },
          ],
        },
        {
          id: '6.3', slug: 'carpetas-compartidas-y-token', title: 'Carpetas compartidas y acceso con token', duration: '8 min',
          summary: 'Cómo crear una carpeta compartida y cómo unirse a una con un token de acceso.',
          objectives: ['Crear una carpeta compartida.', 'Unirse a una carpeta con token.'],
          steps: [
            { t: 'Gestionar carpetas compartidas', b: 'Está en el menú de cuenta. Desde ahí creas una carpeta compartida con Nueva carpeta.' },
            { t: 'Unirse con token', b: 'Si te han dado un token de acceso, escríbelo en Unirse a carpeta con token de acceso y pulsa Unirse.' },
            { t: 'Revisar el acceso', b: 'Comprueba periódicamente quién está en cada carpeta y retira el acceso a quien ya no debe tenerlo.' },
          ],
          tips: ['No compartas un token por canales públicos: trátalo como una contraseña.'],
          quiz: [
            { q: 'Te han dado un token de acceso a una carpeta. ¿Dónde lo escribes?', options: ['En Unirse a carpeta con token de acceso.', 'En el campo de búsqueda de Biblioteca.', 'En la vista general del curso.'], answer: 0, explain: 'Los tokens se usan en Unirse a carpeta con token de acceso, en el menú de cuenta.' },
          ],
        },
        {
          id: '6.4', slug: 'seguridad-privacidad-y-datos', title: 'Seguridad, privacidad y ubicación de datos', duration: '12 min',
          summary: 'Qué debes poder responder sobre seguridad y privacidad, y cómo documentarlo para dirección y familias.',
          objectives: ['Responder las preguntas básicas sobre datos.', 'Minimizar datos personales de alumnos.', 'Tener un procedimiento ante incidentes.'],
          steps: [
            { t: 'Preguntas básicas', b: '¿Dónde se alojan los datos? ¿Quién puede acceder? ¿Cómo se protegen? ¿Cómo se eliminan? ¿Qué datos personales se tratan?' },
            { t: 'Documentación oficial', b: 'Consulta la documentación de seguridad y privacidad publicada por Seven Assistant, y guarda la versión vigente en la carpeta de cumplimiento de tu centro.' },
            { t: 'Minimiza datos', b: 'Usa identificadores internos en lugar de nombres completos cuando sea posible, y define quién puede exportar datos.' },
            { t: 'Cumplimiento local', b: 'Brasil (LGPD), México (LFPDPPP) y Chile (su normativa de datos personales, en actualización) tienen requisitos propios. Consulta con el área jurídica.' },
            { t: 'Incidentes', b: 'Define a quién avisar si una cuenta se compromete y en cuánto tiempo.' },
          ],
          tips: ['Documenta una vez y revisa cada año: una ficha de una página es más útil que una búsqueda en plena crisis.'],
          quiz: [
            { q: '¿Qué práctica reduce más el riesgo con datos de alumnos?', options: ['Usar nombres completos para facilitar búsquedas.', 'Minimizar datos y usar identificadores internos.', 'Compartir la contraseña de administración.'], answer: 1, explain: 'Cuantos menos datos identificables circulen, menor es el impacto de un incidente.' },
          ],
        },
      ],
    },
  ],
  roles: {
    docente: { name: 'Docente', description: 'Planifica, crea cursos y materiales, y corrige con criterios claros. Tu recorrido combina cursos, conversaciones, biblioteca y evaluación.', lessons: ['1.1', '1.2', '1.3', '2.2', '3.5', '4.1', '5.1', '5.3', '5.4'] },
    coordinacion: { name: 'Coordinación académica', description: 'Supervisa cursos, planes y escalas del nivel. Tu recorrido incluye diseño de cursos, participantes y organización.', lessons: ['1.1', '1.2', '2.1', '2.4', '4.4', '5.2', '6.1', '6.2'] },
    'jefatura-tutoria': { name: 'Jefatura de estudios y tutoría', description: 'Da seguimiento a grupos y evaluaciones, y acompaña al profesorado. Tu recorrido incluye IA para el alumnado, participantes y corrección.', lessons: ['1.1', '1.3', '4.3', '4.4', '5.1', '5.4'] },
    'responsable-it': { name: 'Responsable de sistemas IT', description: 'Organiza el centro, gestiona participantes y carpetas compartidas, y revisa seguridad y privacidad. No necesitas crear contenidos para este recorrido.', lessons: ['1.1', '1.2', '4.4', '6.1', '6.2', '6.3', '6.4'] },
  },
  sections: {
    cursos: { name: 'Cursos', short: 'Crea cursos, organiza su contenido y compártelos con el alumnado.', summary: 'Cursos es la herramienta para crear un curso completo: datos básicos, secciones, materiales y actividades, y compartirlo con el alumnado. Está en beta.', whenToUse: ['Cuando planificas una unidad o un trimestre con un grupo.', 'Cuando quieres que el alumnado entre a un curso con código o enlace.', 'Cuando necesitas ver el seguimiento del grupo en participantes y citas.'], basics: ['Ubicación: barra lateral, icono Cursos.', 'Crea el curso con el asistente de tres pasos.', 'Organiza el curso en secciones y añade actividades o materiales.', 'Comparte con código o enlace.'], lessons: ['2.1', '2.2', '2.3', '2.4', '2.5', '3.5', '4.1', '4.4'] },
    conversaciones: { name: 'Conversaciones', short: 'Pregunta, pide borradores e itera con el asistente.', summary: 'Conversaciones es la página de inicio y el espacio para dialogar con el asistente. Las herramientas del botón + te ayudan a planificar, practicar y corregir.', whenToUse: ['Para pensar una clase o buscar ideas de actividades.', 'Para revisar un texto que tú escribiste.', 'Para preparar comunicaciones a las familias.'], basics: ['Ubicación: página de inicio (icono de chat).', 'Da contexto: país, nivel, grado, materia y tiempo.', 'Usa el botón + para herramientas como Serie de clases.', 'Regenera una respuesta si no te convence.'], lessons: ['5.1'] },
    documentos: { name: 'Documentos', short: 'Sube documentos y organízalos en Biblioteca.', summary: 'Los documentos se guardan en Biblioteca, en Mi biblioteca. Puedes subir PDF, vídeos o páginas web.', whenToUse: ['Cuando el material debe quedar guardado para usarlo después.', 'Cuando otra persona necesita leer el material.'], basics: ['Ubicación: Biblioteca, Mi biblioteca.', 'Sube con Subir documento: PDF, vídeo o página web.', 'Nombra los archivos con materia, grupo y fecha.'], lessons: ['5.2'] },
    'series-de-lecciones': { name: 'Series de lecciones', short: 'Crea secuencias de sesiones con progresión y evaluación.', summary: 'Una serie de lecciones agrupa varias sesiones con un mismo objetivo. Se crea desde Biblioteca, con Tema, Asignatura, Curso, Idioma y Descripción.', whenToUse: ['Para una secuencia de 4 a 10 sesiones sobre un mismo tema.', 'Para adaptar la misma progresión a varios grupos.'], basics: ['Ubicación: Biblioteca, Serie de lecciones.', 'Rellena Tema (obligatorio) y el resto de campos, o usa Generar con IA.', 'Ordena las sesiones de lo sencillo a lo complejo.', 'Indica en la descripción dónde están las evaluaciones.'], lessons: ['5.2'] },
    'tareas-de-correccion': { name: 'Tarea de corrección y feedback', short: 'Corrige trabajos con criterios y retroalimentación.', summary: 'La tarea de corrección y feedback se crea desde Biblioteca. Defines criterios, calibras con algunos trabajos y revisas la propuesta antes de cerrar las notas.', whenToUse: ['Para redacciones, problemas o proyectos con varios criterios.', 'Cuando quieres retroalimentación específica para cada alumno.'], basics: ['Ubicación: Biblioteca, Tarea de corrección y feedback.', 'Define criterios observables.', 'Calibra con trabajos de distinto nivel antes de corregir todo.', 'Revisa la retroalimentación antes de publicarla.'], lessons: ['5.4'] },
    'fichas-interactivas': { name: 'Fichas interactivas', short: 'Crea hojas de trabajo con contexto, fuentes y ajustes.', summary: 'Las fichas interactivas se crean desde Biblioteca con Crear hoja de trabajo, en tres pasos: Contexto, Fuentes y Análisis y ajuste.', whenToUse: ['Para práctica en clase o en casa.', 'Para repasar antes de una evaluación.', 'Para atender ritmos distintos.'], basics: ['Ubicación: Biblioteca, Ficha interactiva.', 'Configura Contexto, Fuentes y Análisis y ajuste.', 'Empieza con una extensión corta.', 'Revisa la ficha antes de compartirla.'], lessons: ['5.3'] },
    plantillas: { name: 'Plantillas', short: 'Asistentes de IA con instrucciones propias, y plantillas de curso.', summary: 'Plantillas es la sección de asistentes de IA con instrucciones propias. Las plantillas de curso están dentro de Cursos.', whenToUse: ['Cuando repites un mismo encargo cada semana.', 'Cuando quieres adoptar una unidad didáctica ya preparada.'], basics: ['Asistentes de IA: icono de estrellas; Crear Plantilla define sus instrucciones.', 'Plantillas de curso: Cursos, pestaña Plantillas.', 'Nombra cada plantilla con tipo y nivel.'], lessons: ['2.5', '5.5'] },
    configuracion: { name: 'Configuración', short: 'Idioma de la interfaz y preferencias de tu cuenta.', summary: 'Configuración y el idioma están en el menú de cuenta, con el avatar de tu cuenta, en la parte inferior de la barra lateral.', whenToUse: ['Al empezar a usar la plataforma.', 'Cuando cambias de nivel o de centro.', 'Cuando otra persona necesita trabajar en su idioma.'], basics: ['Ubicación: menú de cuenta (avatar, abajo a la izquierda).', 'Idioma: en el mismo menú.', 'Mantén tu perfil actualizado.'], lessons: ['1.2'] },
  },
};
