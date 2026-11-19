#!/usr/bin/env python3
"""Segunda parte de la reescritura en español (ver rewrites-es.py). Mismo número de pasos que la fuente."""

REWRITES_2 = {
    "tarea-correccion-biblioteca": {
        "answer": "En Biblioteca → Tarea de corrección y feedback creas una tarea con su rigor, sus criterios con puntos y una solución modelo que el alumnado no ve. Sirve para corregir siempre con la misma vara de medir y para devolver una retroalimentación explicada, no solo una nota.",
        "steps": [
            {"t": "Abre Biblioteca → Tarea de corrección y feedback", "b": "Pulsa «Crear». Hazla en la Biblioteca para poder usarla después en varios cursos sin volver a escribirla."},
            {"t": "Rellena los datos generales", "b": "Título, Rigor de la calificación (Equilibrado por defecto), Subidas máximas (1 por defecto) y Descripción de la tarea. La descripción es lo que lee el alumnado: di con claridad qué se pide y para qué."},
            {"t": "Añade la solución modelo", "b": "El campo «Solución modelo» queda oculto para los estudiantes. Escribe aquí cómo sería un trabajo excelente: es la referencia con la que se compara cada entrega."},
            {"t": "Añade los criterios", "b": "Pulsa + en «Criterios de calificación». Cada criterio tiene una Descripción y unos Ptos. (10 por defecto); los puntos deben estar entre 0,5 y 1000, en pasos de medio punto. Un criterio bien escrito es lo que hace la corrección justa y repetible."},
            {"t": "Pulsa Crear", "b": "La tarea aparece en la lista de Tareas de corrección y feedback, lista para asignarla en un curso."},
            {"t": "Revisa las entregas", "b": "Pulsa la tarea para ver los criterios y el enlace de acceso. Cuando entreguen, pulsa una nota para ver el texto del alumnado, la puntuación de cada criterio y su comentario: el comentario es lo que el alumnado usa para mejorar."},
        ],
        "tips": ["Si escribes texto en el campo de puntos, el formulario no se guarda: verás el aviso «Entre 0,5 y 1000 puntos» en rojo.", "Calibra con tres trabajos antes de corregir al grupo."],
    },
    "plantillas-vs-asistentes": {
        "steps": [
            {"t": "Plantillas de curso", "b": "Están en Cursos, en la pestaña Plantillas. Sirven para empezar una unidad sin construirla desde cero; después la adaptas a tu grupo."},
            {"t": "Asistentes de IA", "b": "Están en Plantillas (icono de estrellas). Sirven para las tareas que repites: el asistente aplica siempre tus instrucciones, así que el resultado sale con tu criterio."},
        ],
    },
    "crear-asistente": {
        "answer": "En Plantillas, «Crear Plantilla» abre un formulario con Nombre e Instrucción. Un asistente sirve para tareas que repites, como corregir redacciones o preparar guías de laboratorio, siempre con las mismas reglas. Al guardar, queda disponible en tu lista.",
        "steps": [
            {"t": "Abre Plantillas", "b": "Icono de estrellas en la barra lateral. Aquí están tus asistentes: los que creas tú y los que vas reutilizando."},
            {"t": "Pulsa Crear Plantilla", "b": "Campos Nombre e Instrucción. La instrucción es el texto que define cómo trabaja el asistente cada vez; suele empezar por «Eres un asistente útil…»."},
            {"t": "Rellena el formulario", "b": "Ejemplo: Nombre «Guía de laboratorio · 1.º ESO» e instrucción con el papel del asistente, los pasos que debe seguir y lo que no debe hacer. Cuanto más concreta la instrucción, más se parecerá el resultado a lo que harías tú."},
            {"t": "Pulsa Guardar", "b": "La plantilla aparece en la lista de Plantillas, lista para usarla cuando la necesites."},
            {"t": "Pruébalo en un chat", "b": "En la tarjeta del asistente, pulsa el icono de chat («Iniciar un chat con esta plantilla») y haz una pregunta real. Si la respuesta es demasiado completa o se aleja de lo que necesitas, vuelve a la instrucción y hazla más precisa."},
        ],
        "tips": ["Escribe el nombre con tipo y nivel para encontrarlo después."],
    },
    "idioma": {
        "steps": [
            {"t": "Abre el menú de cuenta", "b": "Pulsa el avatar de abajo a la izquierda. Cambiar el idioma no afecta al contenido de tus cursos ni de tu Biblioteca."},
            {"t": "Pulsa Idioma", "b": "Elige el idioma de la interfaz. Si la pantalla no cambia, consulta «No cambia el idioma de la interfaz»."},
        ],
        "tips": ["Los textos que escribes tú se quedan en el idioma en que los creaste."],
    },
    "menu-de-cuenta": {
        "steps": [
            {"t": "Pulsa el avatar", "b": "Abajo a la izquierda, con tus iniciales. Es el acceso a lo que es tuyo y no del curso: tu configuración, tu idioma y tus carpetas compartidas."},
            {"t": "Elige la opción", "b": "Configuración (datos de tu cuenta), Idioma, Gestionar tareas, Gestionar carpetas compartidas, ¿Qué hay de nuevo?, Ayuda o Cerrar sesión. «¿Qué hay de nuevo?» es el sitio para ver los cambios de la herramienta, sobre todo mientras está en beta."},
        ],
        "tips": ["Cierra sesión si usas un equipo compartido."],
    },
    "carpetas-compartidas": {
        "answer": "En el menú de cuenta, Gestionar carpetas compartidas permite crear una carpeta nueva o unirte a una con un token. Sirve para que varios docentes del mismo departamento o centro compartan materiales en un único lugar, sin enviarse archivos por correo.",
        "steps": [
            {"t": "Abre el menú de cuenta", "b": "Pulsa el avatar de abajo a la izquierda y elige Gestionar carpetas compartidas. Desde aquí llegas a las carpetas que has creado y a las que te has unido."},
            {"t": "Pulsa Nueva carpeta", "b": "Aparecen los campos de nombre y descripción, con Cancelar y Guardar. La descripción ayuda a tus compañeros a saber qué encontrarán dentro."},
            {"t": "Rellena y guarda", "b": "Ejemplo: nombre «Departamento de Biología · materiales», descripción con el contenido de la carpeta. Pulsa Guardar. Un nombre con el departamento evita confundir carpetas parecidas."},
            {"t": "Unirte con un token", "b": "Si te dan un token, escríbelo en el campo de la parte superior y pulsa Unirse. Así entras en la carpeta de tu departamento sin que tengan que añadirte a mano."},
        ],
        "tips": ["Trata el token como una contraseña: no lo publiques."],
    },
    "participantes-permisos": {
        "answer": "En Participantes ves quién tiene acceso al curso, separado en docentes y estudiantes. Las invitaciones que aún no se han aceptado aparecen como «Invitado». Sirve para saber en cualquier momento quién puede ver el curso y detectar accesos que no deberían existir.",
        "steps": [
            {"t": "Abre Participantes", "b": "Verás el buscador, el botón «Invitar a personas» y los filtros Todos, Docentes y Estudiantes, cada uno con su número. Filtrar por Docentes te ayuda a revisar quién colabora en el curso."},
            {"t": "Distingue los roles", "b": "Cada persona aparece como Docente o Estudiante. «Usted» marca tu propio perfil. Revisa los roles cuando alguien colabore en el curso, para que cada persona tenga el acceso que le corresponde."},
            {"t": "Comprueba las invitaciones pendientes", "b": "En «Invitaciones» aparecen las personas invitadas por correo, con su rol y la etiqueta «Invitado», hasta que aceptan. Si alguien lleva mucho tiempo como invitado, quizá el correo no llegó: reenvíalo."},
        ],
        "tips": ["Para invitar a alguien, consulta «Invitar al alumnado»: allí están las tres formas de entrar."],
    },
    "organizacion-centro": {
        "steps": [
            {"t": "Acuerda las asignaturas y los cursos escolares", "b": "Usa los mismos nombres en los campos Asignatura y Clase o curso escolar. Si cada docente escribe «Mates», «Matemáticas» o «MAT», los cursos no se agrupan ni se encuentran juntos."},
            {"t": "Define un formato para los títulos", "b": "Por ejemplo «Matemáticas · 2.º secundaria · 2026-2027». Un formato fijo permite buscar un curso o ver todos los de un departamento de un vistazo."},
            {"t": "Revisa cada año", "b": "Al cerrar el año, reorganiza los nombres para el siguiente. Así los cursos antiguos no se mezclan con los nuevos."},
        ],
        "tips": ["Documenta la convención en un único lugar y compártela con coordinación."],
    },
    "seguridad-datos": {
        "answer": "Tus datos se alojan en Alemania, cumplimos el RGPD, no entrenamos la IA con tus datos y contamos con certificaciones ISO 27001, 9001 y 14001. Sirve para responder a la dirección, a las familias o al área jurídica del centro sobre dónde están los datos y quién los trata.",
        "steps": [
            {"t": "Lo que garantizamos", "b": "Datos alojados en Alemania, cumplimiento del RGPD y ninguna IA entrenada con tus datos. Certificaciones ISO 27001, 9001 y 14001. Son los puntos que un centro suele preguntar antes de usar una herramienta con datos del alumnado."},
            {"t": "Preguntas que debes poder responder", "b": "¿Dónde se alojan los datos? ¿Quién puede acceder? ¿Cómo se protegen? ¿Cómo se eliminan? ¿Qué datos personales se tratan? Si tienes estas respuestas claras, puedes explicar el uso a familias y dirección sin improvisar."},
            {"t": "Documentación oficial", "b": "Para la documentación completa, solicítala a través de 7education.com indicando el nombre de tu centro. Pídela antes de la reunión con la dirección, no después."},
            {"t": "Minimiza los datos de alumnos", "b": "Usa identificadores internos en lugar de nombres completos cuando sea posible. Así, si un documento sale del centro, no expone a nadie."},
            {"t": "Cumplimiento local", "b": "Brasil (LGPD), México (LFPDPPP) y Chile (su normativa de datos personales, en actualización) tienen requisitos propios. Si tu centro está en esos países, consulta con el área jurídica."},
        ],
        "tips": ["Define a quién avisar si una cuenta se compromete y en cuánto tiempo."],
    },
    "no-encuentro-seccion": {
        "steps": [
            {"t": "Revisa la barra lateral", "b": "Conversaciones, Cursos, Biblioteca y Plantillas son las cuatro áreas principales. Si lo que buscas no encaja en ninguna, pasa al siguiente paso."},
            {"t": "Busca en Biblioteca", "b": "Series, fichas y tareas se crean desde la Biblioteca. Si las buscas en Cursos no las encontrarás, aunque luego las uses dentro de un curso."},
            {"t": "Revisa el menú de cuenta", "b": "Configuración, Idioma y carpetas compartidas están ahí. Son ajustes de tu cuenta, no de un curso concreto."},
        ],
    },
    "codigo-filtrado": {
        "steps": [
            {"t": "Abre Configuración → Código de inscripción", "b": "Está en la pestaña Configuración del curso. Ahí ves el código vigente y el estado del enlace público: compruébalo antes de cambiar nada."},
            {"t": "Pulsa Generar nuevo código", "b": "Comparte el nuevo código solo con tu grupo, por un canal que controles, como la plataforma del centro o un correo a la clase."},
            {"t": "Revisa el enlace público", "b": "Si el enlace está activo y no lo necesitas, desactiva «Enlace público de inscripción». Un enlace abierto permite entrar a cualquiera que lo tenga, así que es lo primero que conviene cerrar."},
        ],
        "tips": ["Si necesitas que alguien concreto entre, compártelo solo con esa persona."],
    },
    "alumnado-no-entra": {
        "steps": [
            {"t": "Comprueba el código", "b": "Revisa la vista general del curso. Si el código cambió, comparte el nuevo: el antiguo no sirve para entrar."},
            {"t": "Revisa la forma de entrar", "b": "Deben usar «Unirse a un curso» dentro de Cursos. Quien intenta entrar por otro camino, por ejemplo con un enlace antiguo, puede no ver el curso."},
            {"t": "Prueba la vista de estudiante", "b": "Así compruebas cómo ve el curso el alumnado y si el problema está en el curso o en la forma de entrar."},
        ],
        "tips": ["Comprueba la vista de estudiante antes de compartir el código con el grupo."],
    },
    "respuesta-no-correcta": {
        "steps": [
            {"t": "Revisa los datos", "b": "Contrasta cifras, fechas y datos antes de usarlos en clase. El asistente redacta con seguridad aunque se equivoque, así que la comprobación la haces tú."},
            {"t": "Precisa el contexto", "b": "Indica grupo, nivel, país y formato. Muchas respuestas equivocadas o fuera de lugar se deben a un contexto que faltaba."},
            {"t": "Regenera", "b": "Usa la opción de regenerar la respuesta. Si el problema es el contexto, regenerar sin precisarlo dará otra respuesta igual de genérica."},
        ],
        "tips": ["No uses en clase un dato de la respuesta sin contrastarlo antes.", "Cambia una cosa a la vez al pedir ajustes."],
    },
    "beta": {
        "steps": [
            {"t": "Qué hacer", "b": "Si algo no coincide con esta ayuda, revisa la versión de la ayuda y las novedades desde el menú de cuenta. Así sabes si el cambio es reciente o si el artículo está desactualizado, y puedes reportarlo con esa información."},
        ],
    },
    "idioma-no-cambia": {
        "steps": [
            {"t": "Abre el menú de cuenta y pulsa Idioma", "b": "Vuelve a elegir el idioma y comprueba que queda marcado en tu cuenta."},
            {"t": "Recarga la página", "b": "Así se aplica el cambio en toda la interfaz. Hazlo también si cambias de idioma en otro equipo y ves la pantalla antigua."},
        ],
    },
    "conversacion-modos": {
        "steps": [
            {"t": "Abre el selector Dinámico", "b": "Está junto al campo de escritura. El modo se elige antes de escribir, porque decide qué puede hacer el asistente con tu petición."},
            {"t": "Elige el modo", "b": "Estándar, Crear imágenes, Búsqueda web, Gestionar biblioteca, Crear H5P, Leer en voz alta, Gestionar tareas o Secuencia didáctica. Cada modo está pensado para un tipo de tarea: elige el que coincide con lo que vas a hacer con el resultado."},
            {"t": "Escribe tu petición", "b": "Describe el tema, el grupo y el formato que quieres. Con el modo adecuado, esa descripción es lo que determina la calidad del resultado."},
        ],
        "tips": ["Para buscar información actual, usa Búsqueda web; para planificar una secuencia, Secuencia didáctica."],
    },
    "conversacion-contexto": {
        "steps": [
            {"t": "Indica etapa y grado", "b": "Por ejemplo, 2.º de secundaria o 1.º de bachillerato. Con la etapa, el asistente ajusta el nivel del vocabulario y de los ejercicios."},
            {"t": "Indica país y escala si la necesitas", "b": "Así la rúbrica sale en la escala correcta. Si la escala cambia de un país a otro, sin este dato la calificación no te servirá."},
            {"t": "Indica tiempo y formato", "b": "Una sesión de 50 minutos, una guía de una página o una tabla. Con el tiempo y el formato, el material sale con la extensión que vas a poder usar."},
            {"t": "Pide un criterio de revisión", "b": "Por ejemplo, «indica qué parte puede confundir a un alumno de 12 años». Así obtienes también una lista de los puntos que conviene revisar antes de usar el material."},
        ],
        "tips": ["Ejemplo: «Actúa como docente de matemáticas de secundaria en México. Prepara una guía de una página sobre proporcionalidad, con cinco problemas.»"],
    },
    "documentos-nombres": {
        "steps": [
            {"t": "Usa un formato fijo", "b": "Materia · grupo · fecha · versión, por ejemplo «Matemáticas · 2.º secundaria · 2026-11 · v2». Con el mismo formato siempre, ordenar y buscar funciona sin pensar."},
            {"t": "Sube la nueva versión", "b": "No sustituyas el nombre: súbela con la versión nueva. Así la versión anterior sigue disponible si la necesitas para comparar."},
            {"t": "Conserva la anterior solo si la necesitas", "b": "Guardar todas las versiones llena la Biblioteca de duplicados. Aparta o borra las que ya no sirven, para que la vigente sea la que encuentras."},
        ],
        "tips": ["Revisa cada año qué documentos siguen vigentes."],
    },
    "serie-campos": {
        "steps": [
            {"t": "Tema", "b": "El objetivo concreto de la serie, por ejemplo «Introducción al cálculo integral». Cuanto más concreto sea, más preciso será el contenido: «Matemáticas» sería demasiado amplio."},
            {"t": "Asignatura y Curso", "b": "Para encontrarla y ordenarla. El campo Curso admite ejemplos como «4.º de ESO»; escríbelo como lo usa tu centro para que coincida con tus otros materiales."},
            {"t": "Idioma", "b": "Español por defecto. Cámbialo si la serie es para otro grupo que trabaja en otro idioma."},
            {"t": "Descripción", "b": "Objetivos, contenido y sesiones previstas. Es el campo que más cambia el resultado: cuanto más concreto, mejor se ajusta la serie a tu grupo."},
        ],
        "tips": ["Cuanto más concreta sea la descripción, mejor encajará la serie con tu grupo."],
    },
    "serie-ajustar": {
        "steps": [
            {"t": "Revisa la progresión", "b": "Las sesiones deben ir de lo simple a lo complejo. Si una sesión usa un concepto que aún no ha aparecido, el alumnado se atascará: reordena ese punto antes de usar la serie."},
            {"t": "Pide cambios de uno en uno", "b": "Duración, nivel o evaluación, por separado. Así sabes qué cambio mejora la serie y cuál la empeora."},
            {"t": "Guarda la versión final", "b": "Súbela a Documentos para tenerla organizada. Una versión guardada es la que usarás el año siguiente sin volver a empezar."},
        ],
    },
    "tarea-criterios": {
        "steps": [
            {"t": "Un criterio por competencia", "b": "Por ejemplo, argumentación o resolución de problemas. Si un criterio mezcla dos competencias, no sabrás en cuál falla el alumnado."},
            {"t": "Describe qué debe verse", "b": "Lo que tiene que aparecer en el trabajo para cumplirlo. Escríbelo como algo que puedes comprobar mirando el papel, no como una impresión."},
            {"t": "Define niveles con tu escala", "b": "Consulta las escalas por país en Referencia. Así la nota de cada criterio significa lo mismo que en el resto de tu centro."},
        ],
        "tips": ["«Argumenta con al menos dos evidencias» es observable; «buena redacción» no."],
    },
    "tarea-calibrar": {
        "steps": [
            {"t": "Elige tres trabajos", "b": "Uno débil, uno medio y uno fuerte. Con tres niveles distintos ves si los criterios distinguen bien entre ellos."},
            {"t": "Compara con tu valoración", "b": "Revisa en qué criterios coincide y en cuáles no. Las diferencias te dicen dónde el criterio no es lo bastante claro."},
            {"t": "Ajusta los criterios", "b": "Si una diferencia se repite, el criterio probablemente no es claro. Reescríbelo con un ejemplo de lo que sí se cumple."},
            {"t": "Corrige el resto del grupo", "b": "Con los criterios ya ajustados, la corrección de los demás trabajos es más rápida y más justa."},
        ],
        "tips": ["Guarda los tres trabajos calibrados: te servirán de referencia si tienes dudas más adelante."],
    },
    "ficha-densidad": {
        "steps": [
            {"t": "Extensión", "b": "En Contexto: Prueba corta, Hoja de ejercicios, Material de apoyo o Examen. Debajo, el número de páginas (1 página por defecto). Una prueba corta y un material de apoyo necesitan extensiones muy distintas."},
            {"t": "Número de ejercicios", "b": "Automático por defecto. Desactiva el conmutador para elegir el número; el texto indica el tiempo aproximado. Así calculas si la ficha cabe en tu sesión antes de generarla."},
            {"t": "Densidad de texto", "b": "Compacto, Equilibrado (por defecto) o Detallado. Compacto cabe en menos papel y va bien para repasar; Detallado es mejor para quien necesita más explicación."},
        ],
        "tips": ["Revisa el número de ejercicios y el tiempo aproximado antes de generar."],
    },
    "ficha-revisar": {
        "steps": [
            {"t": "Resuelve dos ejercicios", "b": "Tú mismo, como lo haría un alumno. Así detectas enunciados ambiguos o respuestas erróneas antes de que lo haga el grupo."},
            {"t": "Comprueba el nivel y el idioma", "b": "Que sean los de tu grupo. Una ficha bien planteada pero de otro nivel no sirve para la clase."},
            {"t": "Úsala en un curso", "b": "Con «Añadir actividad o material», elige Ficha de trabajo. Ponla en el tema que corresponde, para que tenga sentido en el momento de hacerla."},
        ],
    },
    "plantilla-nombrar": {
        "steps": [
            {"t": "Usa un nombre con tipo y nivel", "b": "Por ejemplo, «Guía de laboratorio · secundaria». Con ese nombre sabes para qué es el asistente sin abrirlo."},
            {"t": "Describe para qué sirve", "b": "Una frase en el propio asistente. Es lo que te recuerda, meses después, cuándo conviene usarlo."},
            {"t": "Revísalos cada trimestre", "b": "Quita los que ya no uses. Un listado corto es más fácil de usar que uno lleno de asistentes antiguos."},
        ],
    },
    "configuracion-cuenta": {
        "steps": [
            {"t": "Abre el menú de cuenta", "b": "Pulsa el avatar de abajo a la izquierda. Es el acceso a los ajustes que valen para todos tus cursos."},
            {"t": "Elige Configuración", "b": "Revisa tus datos y las opciones de la cuenta. Si buscas un ajuste de un curso concreto, no está aquí, sino dentro de ese curso."},
            {"t": "Vuelve a tu trabajo", "b": "Cuando termines, vuelve a Conversaciones o a Cursos."},
        ],
        "tips": ["No confundas Configuración de la cuenta (avatar) con Configuración del curso (dentro de Cursos)."],
    },
    "agregar-material-archivo": {
        "steps": [
            {"t": "Elige Material", "b": "En «Añadir actividad o material». Usa Material para cualquier archivo que el alumnado solo debe consultar, sin entregar nada."},
            {"t": "Pulsa Subir archivo", "b": "Selecciona el archivo en tu equipo. Ejemplo: «ficha-apoyo-celula.pdf». Antes de subirlo, comprueba que es la versión vigente (ver Nombrar y actualizar versiones)."},
            {"t": "Escribe el título", "b": "Ejemplo: «Ficha de apoyo: partes de la célula». Un buen título dice qué contiene y para qué sesión sirve."},
            {"t": "Pulsa Añadir", "b": "El material aparece en la sección. Si quieres que no lo vean aún, déjalo oculto y muéstralo el día de la clase."},
        ],
        "tips": ["En el título, di lo que contiene y no solo el nombre del archivo: «Ficha de apoyo: partes de la célula» se entiende mejor que «Doc1»."],
    },
    "visibilidad-entradas": {
        "steps": [
            {"t": "Identifica las entradas ocultas", "b": "En la vista general, la etiqueta «Oculto» aparece en la entrada. Revísalas antes de cada clase: una entrada oculta que olvidas puede dejar al grupo sin material."},
            {"t": "Cambia la visibilidad", "b": "Abre el menú (…) de la entrada para cambiar si está oculta o visible. Hazlo el día que quieres que el grupo lo vea, no antes."},
            {"t": "Comprueba con «Ver como estudiante»", "b": "Pulsa «Ver como estudiante». Aparece el aviso «Vista de estudiante. Aquí no se cambia nada» y ves el curso como lo ve el alumnado. Es la forma más fiable de confirmar lo que ve."},
            {"t": "Vuelve a tu vista", "b": "Pulsa «Salir de la vista». Así vuelves a editar el curso sin cambiar nada de lo que ya comprobaste."},
        ],
        "tips": ["Antes de una clase, comprueba con la vista de estudiante que no queda ningún material oculto que quieras mostrar."],
    },
    "entrega": {
        "steps": [
            {"t": "Elige Entrega", "b": "En «Añadir actividad o material» (la descripción de la opción es «El alumnado sube archivos»). Úsala cuando necesitas el trabajo como archivo, no como respuesta dentro de la plataforma."},
            {"t": "Rellena el formulario", "b": "Ejemplo: Título «Trabajo: célula animal y célula vegetal», Enunciado con lo que deben dibujar y comparar, Fecha 04/12, Hora 23:59. Un enunciado claro evita la mayoría de las dudas de última hora."},
            {"t": "Bloquea la IA si lo necesitas", "b": "«Bloquear la IA hasta la fecha límite» solo funciona con fecha de entrega. Actívalo en trabajos que el alumnado debe hacer por su cuenta."},
            {"t": "Pulsa Añadir", "b": "La entrega aparece en la sección. Comprueba la fecha y la hora antes de publicarla: un error ahí decide si el alumnado llega a tiempo."},
        ],
    },
    "invitar-alumnado": {
        "steps": [
            {"t": "Código de inscripción (con cuenta)", "b": "Copia el código en la vista general (tarjeta «Invitar al alumnado») o en Configuración → Código de inscripción. El alumnado, con sesión iniciada, lo escribe en Cursos → «Unirse a un curso». No pide nombre: usa el de su cuenta. Es la opción recomendada cuando el alumnado tiene cuenta."},
            {"t": "Enlace público (sin cuenta)", "b": "En Configuración → Código de inscripción, activa «Enlace público de inscripción» y comparte el enlace. El alumnado lo abre, escribe su nombre y la primera letra de su apellido, y pulsa «Unirse a un curso». Úsalo para actividades puntuales o para personas sin cuenta."},
            {"t": "Invitación por correo (con cuenta)", "b": "En Participantes, pulsa «Invitar a personas», elige «Invitar por correo electrónico», escribe el correo y el rol, y pulsa Invitar. La persona acepta con su cuenta; mientras tanto aparece como «Invitado». Sirve para añadir a alguien concreto, como un colaborador."},
        ],
        "tips": [
            "Con el enlace público activado, cualquier persona que lo tenga puede entrar: desactívalo cuando termine la inscripción.",
            "Invitar por correo envía una invitación real: revisa bien la dirección antes de pulsar Invitar.",
        ],
    },
    "contenidos-compartidos": {
        "steps": [
            {"t": "Abre la pestaña", "b": "Cada sección aparece como una carpeta con su número de entradas. Es la vista para revisar el material del curso sin entrar sección por sección."},
            {"t": "Filtra por tipo", "b": "Todos, Material, Entrega, Enlace y Nota. Filtra por Entrega cuando quieras ver de un vistazo los trabajos recibidos."},
            {"t": "Busca o cambia la vista", "b": "El campo «Buscar contenidos» filtra por nombre; los iconos cambian entre lista y mosaico. Úsalo para encontrar un material concreto en un curso largo."},
            {"t": "Añade contenido", "b": "El botón «Añadir» crea un contenido nuevo. Para materiales que el alumnado debe ver en un tema concreto, es más claro crearlos dentro de su sección."},
        ],
        "tips": ["Usa esta pestaña para revisar de un vistazo todas las entregas del curso."],
    },
    "exportar-curso": {
        "steps": [
            {"t": "Abre Configuración → Exportación", "b": "La sección está en el menú de la pestaña Configuración. Exporta antes de archivar: el archivo es tu copia si necesitas el curso más adelante."},
            {"t": "Elige el formato", "b": "Exportar como ZIP, Exportar como IMS Common Cartridge o Exportar como copia de seguridad de Moodle (.mbz). Elige Moodle si lo vas a usar allí, e IMS si la otra herramienta lo pide."},
        ],
        "tips": ["Haz una copia de seguridad al terminar el curso, antes de archivarlo."],
    },
    "enlace-y-nota": {
        "steps": [
            {"t": "Enlace", "b": "En «Añadir actividad o material», elige Enlace. Escribe el título y la dirección (URL). Ejemplo: «Microscopio óptico (referencia)». Comprueba que la web sigue activa: un enlace roto se nota en clase."},
            {"t": "Nota", "b": "Elige Nota y escribe el texto. Ejemplo: «Recuerda: el aumento total es el producto del aumento del objetivo por el del ocular.» Úsala para lo que el alumnado debe tener a la vista, sin abrir nada más."},
            {"t": "Pulsa Añadir", "b": "El enlace o la nota aparece en la sección. Si la nota es larga, mírala en «Ver como estudiante» para comprobar cómo se lee."},
        ],
        "tips": ["Usa una nota para lo que hay que recordar y un enlace para lo que hay que consultar."],
    },
    "texto-material": {
        "steps": [
            {"t": "Elige Material de lectura, en su propia página", "b": "En «Añadir actividad o material». Úsalo cuando el contenido es un texto que quieres explicar o desarrollar, no un archivo ya hecho."},
            {"t": "Escribe el título", "b": "Ejemplo: «Lectura: la teoría celular». El título anuncia la lectura y ayuda a encontrarla después."},
            {"t": "Escribe el texto", "b": "El editor tiene Deshacer, Rehacer, Título 2, Título 3, Negrita, Cursiva, Tachado, listas numeradas y con viñetas, e Insertar gráfico. Usa los títulos para dividir el texto: el alumnado se orienta mejor y puede volver a un apartado concreto."},
            {"t": "Pulsa Añadir", "b": "La lectura aparece en la sección con su tipo Texto. Ábrela una vez como estudiante para comprobar cómo se lee en pantalla."},
        ],
        "tips": ["Divide la lectura con Título 2 y Título 3 para que el alumnado la recorra mejor."],
    },
    "no-puedo-acceder": {
        "steps": [
            {"t": "Revisa el correo de acceso", "b": "Usa el correo con el que te dieron de alta en tu centro. Si el centro entra con una cuenta institucional, usa esa misma cuenta: con otra no verás tus cursos."},
            {"t": "Prueba en otro navegador o en incógnito", "b": "Cierra sesión, abre una ventana de incógnito y vuelve a entrar. Así descartas cookies y sesiones antiguas que pueden estar bloqueando el acceso."},
            {"t": "Restablece la contraseña", "b": "Si la contraseña no funciona, usa la opción de recuperación de contraseña de la página de inicio de sesión. Hazlo antes de pedir ayuda, porque es lo más rápido."},
            {"t": "Pide ayuda a quien administra el centro", "b": "Si sigues bloqueado, tu cuenta puede no estar activa o necesitar un acceso especial. Quien administra el centro puede revisarlo y dártelo: envíale el correo con el que intentas entrar y el mensaje de error."},
        ],
        "tips": [
            "Si no tienes correo de acceso, pide a tu coordinador o al administrador del centro que te envíe una invitación.",
            "Si tenías acceso y de repente lo has perdido, avisa al administrador: la configuración del centro pudo cambiar.",
        ],
    },
}
