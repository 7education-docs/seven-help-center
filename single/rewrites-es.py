#!/usr/bin/env python3
"""Reescritura de artículos en español: qué es, para qué sirve, cuándo usarlo y qué gana el colegio.

Cada artículo conserva el número de pasos y su orden (las capturas numeradas dependen de ello).
Los pasos explican para qué sirve cada pieza, no dónde está el botón. Se aplica en merge-published.py.
"""

REWRITES = {
    "que-es": {
        "answer": "Seven Assistant es un asistente de IA para planificar clases, crear materiales, redactar y revisar trabajos. Sirve cuando necesitas preparar algo rápido (una clase de la semana que viene, una rúbrica, una evaluación) y prefieres partir de un borrador en lugar de empezar de cero. Propone; tú decides qué usas con tu alumnado.",
        "steps": [
            {"t": "Lo que puedes hacer", "b": "Conversar con el asistente y, a partir de ahí, crear cursos con secciones y actividades, guardar materiales en la Biblioteca, preparar series de lecciones, fichas interactivas y tareas de corrección. Es el punto de partida de casi todo el trabajo."},
            {"t": "Lo que no hace", "b": "No sustituye tu criterio profesional. Revisa siempre lo que propone antes de compartirlo con alumnos o familias: la IA puede equivocarse en datos, fechas o niveles."},
            {"t": "Conversaciones", "b": "Es la página de inicio. Úsala para preguntas rápidas y para pedir ideas o borradores antes de llevarlos a un curso."},
            {"t": "Cursos", "b": "Aquí creas cursos, te unes a uno como alumno o importas uno que ya tienes. Un curso reúne todo lo que trabajas con un grupo en un mismo sitio."},
            {"t": "Biblioteca", "b": "Guarda documentos, series de lecciones, fichas interactivas y tareas de corrección para reutilizarlos en varios cursos y en otros años."},
            {"t": "Plantillas", "b": "Icono de estrellas. Son asistentes de IA con instrucciones propias: úsalos cuando repites el mismo tipo de tarea y quieres que siempre salga con el mismo criterio."},
            {"t": "Menú de cuenta", "b": "Pulsa el avatar de abajo para acceder a Configuración, al idioma y a las carpetas compartidas del centro."},
        ],
        "tips": ["Empieza por una necesidad concreta: una clase de la próxima semana, una rúbrica o una evaluación. Con un objetivo claro, la primera respuesta ya es útil."],
    },
    "que-es-un-curso-ayuda": {
        "answer": "La vista general es la pantalla principal de un curso. Desde aquí invitas al alumnado, ves las secciones con su contenido y la próxima cita, y compruebas qué ve tu grupo. Conviene mirarla antes de cada clase, porque resume el estado del curso de un vistazo.",
        "steps": [
            {"t": "Invitar al alumnado", "b": "Aquí tienes el código de inscripción con un botón para copiarlo. Es la forma más rápida de que el grupo entre el primer día, sin tener que buscar el curso."},
            {"t": "Próxima cita", "b": "Muestra la siguiente sesión del curso. Te recuerda qué toca en la próxima clase; si no aparece ninguna, el curso aún no tiene sesiones planificadas."},
            {"t": "Secciones", "b": "Cada sección agrupa un bloque del curso, como una unidad o un trimestre. Ábrela para ver sus materiales y actividades; el número de entradas te dice cuánto contenido tiene cada bloque."},
            {"t": "Entradas ocultas", "b": "Una entrada marcada como «Oculto» no la ve el alumnado. Úsalo para preparar material antes de publicarlo, o para dejar lista la semana siguiente sin que se vea todavía."},
            {"t": "Pestañas del curso", "b": "Vista general, Citas, Contenidos compartidos, Participantes y Configuración. Cada pestaña responde a una tarea distinta: planificar, revisar materiales, gestionar el grupo o ajustar el curso. «Ver como estudiante» está arriba a la derecha."},
        ],
        "tips": ["Revisa la vista general antes de cada clase para comprobar qué ve el alumnado."],
    },
    "secciones": {
        "answer": "Una sección agrupa el contenido de un curso en un bloque, por ejemplo una unidad didáctica. Sirve para que el alumnado encuentre cada tema en su sitio y para reorganizar el curso por bloques sin mezclar materiales. Úsala cuando quieres dividir el curso por unidades o trimestres y que el alumnado vea en orden qué tiene que hacer en cada bloque.",
        "steps": [
            {"t": "Localiza las secciones", "b": "Son el esqueleto del curso: cada tarjeta numerada es un bloque. Te permite ver de un vistazo qué unidades tienes creadas y cuánto contenido hay en cada una."},
            {"t": "Añade una sección", "b": "Crea una sección por cada tema nuevo. Es mejor tener varias cortas que una larga: el alumnado sabe dónde buscar cada cosa."},
            {"t": "Gestiona una sección", "b": "Desde el menú (…) accedes a las opciones de esa sección. Revísalas al reorganizar el curso al empezar un trimestre."},
        ],
        "tips": ["Pon un nombre que describa el bloque: «La célula, unidad de los seres vivos» informa mejor que «Tema 1»."],
    },
    "actividades": {
        "answer": "Dentro de una sección, «Añadir actividad o material» es el punto de entrada para todo lo que el alumnado ve o hace: materiales para leer, fichas para practicar, entregas, tareas corregidas y agentes de IA. Conviene elegir el tipo según lo que quieres que pase después, no según el que te suene más.",
        "steps": [
            {"t": "Abre la sección", "b": "Pulsa «Añadir actividad o material» al final de la sección donde quieres colocarla. Así la actividad queda junto al tema al que pertenece."},
            {"t": "Elige el tipo", "b": "Material, Texto, Enlace, Nota, Ficha de trabajo, Tarea con comentarios, Entrega, Unidad didáctica, Agente de IA y Crear con IA. Cada uno pide algo distinto al alumnado: leer, practicar, entregar o recibir una devolutiva."},
            {"t": "Completa el formulario", "b": "Cada tipo tiene su propio formulario. La actividad aparece en la sección cuando pulsas «Añadir»; ponle un título que el alumnado entienda sin contexto."},
        ],
        "tips": ["Si el alumnado debe entregar un archivo, usa Entrega. Si debe practicar, usa Ficha de trabajo."],
    },
    "tipo-de-actividad": {
        "answer": "Hay cinco tipos de actividad: material para leer o ver, ficha para practicar, entrega para recibir un archivo, tarea con comentarios para devolver una corrección y agente de IA para resolver dudas. Elige según lo que quieres comprobar y lo que vas a recibir de vuelta, porque así evitas crear algo que no te sirve.",
        "steps": [
            {"t": "Quiero que lean o vean algo", "b": "Material o Texto. Úsalo para contenido que el alumnado consulta antes o después de la clase: apuntes, vídeos o lecturas."},
            {"t": "Quiero que practiquen", "b": "Ficha de trabajo. Ideal para ejercicios que el alumnado resuelve por su cuenta y que luego repasas en clase."},
            {"t": "Quiero que me entreguen un archivo", "b": "Entrega. Sirve cuando necesitas recibir un trabajo (un PDF o un documento) con fecha límite."},
            {"t": "Quiero devolutiva sobre su trabajo", "b": "Tarea con comentarios. Úsala cuando quieres corregir y devolver comentarios sobre un trabajo, no solo recibirlo."},
            {"t": "Quiero un asistente para sus dudas", "b": "Agente de IA, con instrucciones claras. Sirve para resolver dudas fuera de clase; las instrucciones deciden si da pistas o soluciones, así que define bien ese límite."},
        ],
    },
    "tarea-con-comentarios": {
        "answer": "La tarea se elige de la Biblioteca y el curso recibe una copia: los cambios posteriores en la Biblioteca no modifican lo que ya tiene el curso. Sirve para reutilizar la misma tarea de corrección en varios grupos sin que un cambio hecho para uno afecte a los demás.",
        "steps": [
            {"t": "Pulsa Añadir actividad o material", "b": "Al final de la sección. Hazlo en la sección donde el alumnado debe encontrar la tarea, justo cuando toca hacerla."},
            {"t": "Elige Tarea con comentarios", "b": "Se abre «Añadir a «nombre de la sección»». Comprueba que es la sección correcta antes de continuar."},
            {"t": "Pulsa Elegir de la biblioteca", "b": "Aparecen las tareas que ya tienes creadas. Si todavía no tienes ninguna, verás «Su biblioteca aún no tiene nada de este tipo»: primero hay que crearla en la Biblioteca."},
            {"t": "Selecciona la tarea y pulsa Añadir", "b": "La tarea aparece en la sección con su tipo y el curso recibe su copia. Si después cambias la tarea en la Biblioteca, el curso conserva la versión que añadiste."},
        ],
        "tips": ["Crea primero la tarea en Biblioteca (ver el artículo de corrección)."],
    },
    "vistas-del-curso": {
        "answer": "La vista del curso cambia cómo se muestran las secciones y los contenidos: en lista, con vista previa o en mosaicos. Sirve para que el curso se lea como lo necesitas al preparar la clase y para que el alumnado encuentre con facilidad lo que busca.",
        "steps": [
            {"t": "Lista", "b": "Títulos y tipos, uno debajo de otro. Es la más compacta: útil cuando el curso tiene muchos contenidos y quieres verlos todos de un vistazo."},
            {"t": "Lista con vista previa", "b": "Muestra las primeras líneas de cada contenido. Es la más clara para el alumnado, porque se entiende de qué trata cada entrada sin abrirla."},
            {"t": "Mosaicos", "b": "Cada sección muestra sus contenidos como tarjetas. Va bien en cursos con materiales muy visuales, como portadas o imágenes."},
            {"t": "Secciones como mosaicos", "b": "Cada sección tiene su propia página. Es útil cuando cada tema es largo y quieres que el alumnado entre en un bloque cada vez."},
            {"t": "Navegación entre contenidos", "b": "Si la activas en Configuración, cada contenido enlaza con el anterior y el siguiente. Sirve para leer un tema de principio a fin sin volver a la vista general."},
        ],
        "tips": ["Para el alumnado, Lista con vista previa suele ser la más clara."],
    },
    "unirse-curso": {
        "answer": "Puedes entrar en un curso de tres formas: con el código de inscripción y tu cuenta, con el enlace del curso sin cuenta, o aceptando una invitación por correo. Sirve para llegar al curso de tu clase sin depender de correos ni de buscar nada.",
        "steps": [
            {"t": "Con código y cuenta", "b": "Es la opción habitual en el centro: inicia sesión, entra en Cursos, pulsa «Unirse a un curso» y escribe el código que te dio tu docente. No tienes que escribir tu nombre, porque se usa el de tu cuenta."},
            {"t": "Con el enlace, sin cuenta", "b": "Útil si todavía no tienes cuenta o si el curso es puntual. Abre el enlace, escribe tu nombre y la primera letra de tu apellido, y pulsa «Unirse a un curso». Tu docente te verá en la lista de participantes."},
            {"t": "Con una invitación por correo", "b": "Abre la invitación que llegó a tu correo y acepta con la cuenta a la que llegó. Si no la encuentras, pide a tu docente que la envíe de nuevo."},
        ],
        "tips": ["Si ya tienes un código de acceso personal de este curso, pulsa «Tengo un código de acceso» en la página del enlace."],
    },
    "ia-alumnado": {
        "answer": "En Configuración → IA en el curso decides si el alumnado puede usar la IA, cómo responde y cuántos mensajes puede enviar. Sirve para que la IA ayude a aprender sin dar la respuesta hecha: el ajuste por defecto es un tutor que guía con pistas.",
        "steps": [
            {"t": "Activa o desactiva la IA", "b": "El conmutador «IA para el alumnado» enciende o apaga la IA del curso. Apágala en semanas de examen o cuando una actividad debe hacerse sin ayuda."},
            {"t": "Elige cómo responde", "b": "Tutor de IA (por defecto): da pistas y hace preguntas, sin soluciones completas; es la opción que más ayuda a aprender. Solo contenidos del curso: responde solo con el material del curso. Libre: también responde fuera del curso."},
            {"t": "Elige las funciones", "b": "Generar imágenes y Búsqueda web vienen desactivadas, y Adjuntar archivos viene activada. Déjalas así salvo que una actividad necesite una de ellas de forma explícita."},
            {"t": "Limita los mensajes", "b": "«Mensajes por estudiante y día» tiene 50 por defecto. Bájalo si ves que el alumnado pregunta todo sin pensar antes."},
            {"t": "IA para invitados", "b": "Se aplica a quienes se unieron con el enlace público. Viene desactivada: actívala solo si esas personas deben usar la IA del curso."},
            {"t": "Pausar la IA", "b": "Al final de la página puedes pausar la IA del curso. Úsalo cuando haga falta cortar el acceso de forma temporal, por ejemplo durante un examen."},
        ],
        "tips": ["El profesorado siempre puede usar la IA del curso, aunque el alumnado no la tenga activa."],
    },
    "agente-de-ia": {
        "answer": "Un agente de IA es un asistente para el alumnado, con un nombre y unas instrucciones tuyas. Sirve para que el alumnado tenga ayuda disponible fuera de clase, siempre con las reglas que tú defines: qué ayuda da y qué no.",
        "steps": [
            {"t": "Elige Agente de IA", "b": "En «Añadir actividad o material». Ponlo en la sección del tema al que corresponde, para que el alumnado lo encuentre en el momento de la duda."},
            {"t": "Escribe el título", "b": "Por ejemplo, «Ayudante de la célula». Un nombre claro le dice al alumnado para qué sirve sin que tengas que explicárselo."},
            {"t": "Escribe las instrucciones", "b": "Campo «Instrucciones para la IA (opcional)». Por ejemplo: «Responde con pistas y preguntas. No des la solución completa de los ejercicios.» Aquí decides el papel del agente; es el paso más importante."},
            {"t": "Pulsa Añadir", "b": "El agente aparece en la sección. Pruébalo antes de compartirlo: haz la pregunta que haría un alumno y comprueba que la respuesta encaja con lo que quieres."},
        ],
        "tips": ["Las instrucciones son lo más importante: define qué ayuda da el agente y qué no."],
    },
    "participantes-citas": {
        "answer": "En la pestaña Citas creas las sesiones con fecha y hora. Cada cita aparece en «Próximas» con su horario, su lugar y su título. Sirve para que el alumnado sepa cuándo y dónde es cada sesión sin depender de un mensaje.",
        "steps": [
            {"t": "Abre la pestaña Citas", "b": "Aquí planificas el calendario del curso. Si todavía no tiene citas, verás «Este curso aún no tiene citas»."},
            {"t": "Pulsa Crear cita", "b": "Campos Título, Fecha, Desde, Hasta, Lugar (opcional) y Nota (opcional). Pon siempre hora de inicio y de fin, para que el alumnado sepa cuánto dura cada sesión."},
            {"t": "Rellena el formulario", "b": "Por ejemplo: Título «Laboratorio: observar células de cebolla», Fecha 24/11, Desde 09:00, Hasta 09:50, Lugar «Laboratorio de Ciencias». Un título que diga qué se hace en la sesión es más útil que «Clase 3»."},
            {"t": "Pulsa Guardar", "b": "La cita aparece en «Próximas» con el día, el horario, el título y el lugar. Revisa la fecha, sobre todo si repites sesiones en semanas distintas."},
        ],
        "tips": ["Usa la Nota para el material que el alumnado debe traer, por ejemplo «Traer el microscopio óptico y una cebolla»."],
    },
    "configuracion-del-curso": {
        "answer": "La pestaña Configuración reúne los ajustes del curso: general, portada, visualización, código de inscripción, IA, exportación y archivado. Sirve para dejar el curso listo para tu grupo y revisarlo al empezar cada trimestre o al cerrar el curso.",
        "steps": [
            {"t": "General", "b": "Nombre, Asignatura, Clase o curso escolar y Descripción. Son los datos que identifican el curso en tu lista y en la del centro, así que mantenlos con el formato que acordéis. Pulsa «Aplicar cambios» para guardarlos."},
            {"t": "Portada", "b": "La imagen que se ve en el curso, en la lista de cursos y en la página de inscripción. Una portada reconocible ayuda a encontrar el curso correcto entre varios."},
            {"t": "Visualización", "b": "Activa o desactiva «Contenido anterior y siguiente» y elige la vista de la vista general: Lista, Lista con vista previa, Mosaicos o Secciones como mosaicos. Con esto decides cómo lee el alumnado el curso."},
            {"t": "Código de inscripción", "b": "El código, el enlace público (desactivado por defecto) y «Generar nuevo código». Genera un código nuevo si se ha compartido fuera de la clase, y desactiva el enlace público cuando termine la inscripción."},
            {"t": "IA en el curso", "b": "Qué puede hacer el alumnado con la IA. Antes de decidir, lee el artículo «IA para el alumnado y el Tutor de IA»."},
            {"t": "Exportación y archivado", "b": "Exportar el curso o archivarlo y salir. Antes de archivar, revisa que no lo necesitas para otro grupo, y haz una copia de seguridad si quieres conservarlo."},
        ],
        "tips": ["«Eliminar curso» no aparece en los pasos normales: úsalo solo si estás seguro, porque no tiene vuelta atrás."],
    },
    "hacer-pregunta": {
        "answer": "Escribe en el campo de Conversaciones y envía. Sirve para obtener una primera versión de lo que necesitas (una explicación, un ejercicio, un esquema) y ajustarla a tu grupo. Cuanto más contexto des, menos tendrás que reescribir.",
        "steps": [
            {"t": "Escribe en el campo", "b": "Está en la página de inicio, con el texto «Pregunta cualquier cosa». Empieza por lo que quieres conseguir: «Necesito…» o «Prepárame…» funcionan mejor que una pregunta vaga."},
            {"t": "Da contexto", "b": "Indica país, nivel, grado, materia, número de alumnos y tiempo. Así la respuesta encaja con tu grupo y no con un alumnado genérico."},
            {"t": "Envía", "b": "Revisa la respuesta antes de usarla: el asistente propone y tú decides, sobre todo si contiene datos, fechas o cifras."},
        ],
        "tips": ["Pide algo concreto: «Diseña cuatro problemas de proporcionalidad para 2.º de secundaria» funciona mejor que «ayúdame con fracciones»."],
    },
    "herramientas-asistente": {
        "answer": "El icono de martillo abre las Plantillas de Seven Assistant: herramientas como Diferenciación, Materiales, Deberes o Texto de audición. Sirve para que el asistente trabaje con un objetivo concreto, y eso da respuestas más útiles que una petición general.",
        "steps": [
            {"t": "Pulsa el icono de martillo", "b": "Está en la barra de herramientas del campo de escritura. Úsalo cuando la petición tiene un tipo de tarea claro, en lugar de escribir desde cero."},
            {"t": "Elige la herramienta", "b": "Diferenciación para niveles de dificultad, Materiales para organizar tus recursos, Deberes para apoyo con tareas y Texto de audición para generar audio o transcribir vídeos. Elige según lo que vas a hacer con el resultado."},
            {"t": "Modo de conversación", "b": "El botón Dinámico cambia el modo: Estándar, Crear imágenes, Búsqueda web, Gestionar biblioteca, Crear H5P, Leer en voz alta, Gestionar tareas o Secuencia didáctica. El modo define qué puede hacer el asistente en esa conversación."},
            {"t": "Escribe tu petición", "b": "Describe el tema y el grupo. Con la herramienta y el modo ya elegidos, el contexto que añades es lo que mejora la respuesta."},
        ],
    },
    "regenerar-respuesta": {
        "answer": "Regenerar una respuesta pide al asistente que vuelva a contestar a la misma pregunta. Úsala cuando la respuesta es floja, genérica, demasiado larga o no sigue el formato que necesitas, sin tener que reescribir la pregunta desde cero. Si la nueva respuesta tampoco convence, vuelve a regenerarla.",
        "steps": [
            {"t": "Pulsa regenerar", "b": "Está debajo de la respuesta. Úsalo cuando la base es buena pero no es lo que necesitas: no tienes que repetir todo el contexto."},
            {"t": "Cambia la petición si hace falta", "b": "Si la respuesta sigue sin encajar, no basta con regenerar: precisa el contexto o el formato. Por ejemplo, «en formato de tabla, para 30 minutos de clase»."},
        ],
        "tips": ["Cambia una cosa a la vez al pedir ajustes: así sabes qué ha mejorado."],
    },
    "subir-documento": {
        "answer": "Subir un documento a Mi biblioteca sirve para que la IA pueda usarlo como contexto: un PDF de tu libro, un vídeo o una página web. Cuando el documento está en «Listo», puedes pedir al asistente que trabaje con él en lugar de copiar y pegar fragmentos.",
        "steps": [
            {"t": "Abre Mi biblioteca", "b": "Icono de cuadrícula en la barra lateral. Aquí están todos tus documentos: los que subes tú y los que reutilizas en varias clases."},
            {"t": "Pulsa Contenido", "b": "Botón azul de la parte superior. Se despliega un menú con las formas de añadir material."},
            {"t": "Elige qué añadir", "b": "Subir archivos para un PDF o un vídeo de tu ordenador. Añadir página web para una dirección, por ejemplo un artículo de Wikipedia: útil cuando el material ya está en internet y no quieres descargarlo."},
            {"t": "Espera a que esté Listo", "b": "Mientras aparece «Preparando…», el documento se procesa. No lo uses en una conversación hasta que aparezca «Listo», porque la IA aún no tendría el contenido."},
            {"t": "Revísalo", "b": "Ábrelo para comprobar que el contenido es el correcto. Desde ahí puedes editar el resumen o abrir la página original."},
        ],
        "tips": [
            "Pon a cada archivo un nombre que identifique materia, grupo y fecha. Así lo encontrarás después con el buscador de Mi biblioteca («Buscar documentos…»).",
            "Si empiezas desde la portada de Biblioteca, la tarjeta Subir documento te lleva a Mi biblioteca, donde está el botón Contenido.",
        ],
    },
    "buscar-contenido": {
        "steps": [
            {"t": "Escribe en Buscar en todo el contenido", "b": "Aparecen los documentos, series y fichas que coinciden con tu búsqueda. Úsalo antes de crear algo nuevo, para no duplicar un material que ya tienes."},
        ],
    },
    "serie-de-lecciones": {
        "answer": "Una serie de lecciones es una secuencia de sesiones sobre un tema, con su progresión y su evaluación. Sirve para planificar un tema completo de una vez, en lugar de preparar cada clase por separado, y para reutilizarla el año siguiente.",
        "steps": [
            {"t": "Abre Biblioteca → Serie de lecciones", "b": "Desde aquí puedes crear una serie a mano o generarla con IA. Elige según cuánto quieras partir de cero."},
            {"t": "Pulsa Crear", "b": "Se abre «Crear serie de lecciones». Ten a mano el tema, el curso y las sesiones que quieres cubrir, porque el formulario se rellena mejor con esa información delante."},
            {"t": "Rellena el formulario", "b": "Por ejemplo: Tema «Niveles de organización de los seres vivos», Asignatura «Biología y Geología», Curso «1.º ESO», Idioma Español y una Descripción con las sesiones previstas. Cuanta más información des, más ajustada a tu grupo sale la serie."},
            {"t": "Pulsa Crear", "b": "La serie queda guardada en tu lista de la Biblioteca, lista para revisarla y ajustarla."},
        ],
        "tips": ["Describe las sesiones y la evaluación en la Descripción: así la serie es útil para programar."],
    },
    "ficha-interactiva": {
        "answer": "En Biblioteca → Ficha interactiva se abre «Crear hoja de trabajo», un asistente de tres pasos: Contexto, Fuentes y Análisis y ajuste. Sirve para generar una hoja de práctica o de examen a medida de tu grupo, con la extensión, la dificultad y la densidad que necesitas.",
        "steps": [
            {"t": "Paso 1: Contexto", "b": "Tema (obligatorio), Asignatura, Nivel escolar, Nivel de dificultad (Medio por defecto), Idioma y Extensión: Prueba corta, Hoja de ejercicios, Material de apoyo o Examen. Elige la extensión según para qué la vas a usar: una prueba corta no se parece a un material de apoyo."},
            {"t": "Paso 2: Fuentes", "b": "Documentos de contexto: «Desde la biblioteca» o «Buscar contenido». Si añades tus propios documentos, la ficha se apoya en tu material y no solo en lo que sabe el asistente. El indicador muestra cuántos tokens de contexto usa la ficha."},
            {"t": "Paso 3: Análisis y ajuste", "b": "Ajusta el número de ejercicios y la densidad del texto (Compacto, Equilibrado o Detallado) antes de generar. Hacerlo aquí evita tener que regenerar después."},
            {"t": "Pulsa Continuar hasta el final", "b": "«Continuar» avanza de paso. No puedes avanzar sin rellenar el Tema, así que es lo primero que debes definir."},
            {"t": "Pulsa Generar", "b": "En la esquina superior derecha, pulsa «Generar». Aparece «Generando hoja de trabajo…»: en ese momento la ficha se crea de verdad."},
            {"t": "Espera el resultado", "b": "La generación tarda entre 1 y 3 minutos. No cierres la página mientras espera."},
            {"t": "Comprueba la ficha", "b": "Revisa el título, los bloques de ejercicios y las respuestas correctas. Si aparece un aviso de verificación, revisa esas respuestas antes de repartir la ficha: la IA también puede equivocarse aquí."},
        ],
        "tips": ["Para apoyo, densidad compacta y dificultad baja. Para examen, densidad equilibrada."],
    },
    "ficha-de-trabajo-curso": {
        "steps": [
            {"t": "Añade la ficha en la sección", "b": "Pulsa «Añadir actividad o material» y elige Ficha de trabajo. Colócala justo después de la explicación del tema, para que el alumnado la haga mientras lo tiene fresco."},
        ],
    },
}
