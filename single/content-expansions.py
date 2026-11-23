#!/usr/bin/env python3
"""Amplía los artículos más escuetos: qué es, cuándo usarlo, un ejemplo y consejos.

Se aplica sobre los datos publicados (merge-published.py). No toca los pasos: las capturas
numeradas dependen del número de pasos. Para cada artículo se reemplazan:
  answer   -> qué es, para qué sirve y cuándo usarlo (párrafo "En resumen")
  example  -> caso concreto ("Ejemplo")
  tips     -> consejos (si se indica; si no, se mantienen los actuales)
"""
import pathlib

CONTENT = {
    'es': {
        'buscar-contenido': dict(
            answer="El buscador de la Biblioteca encuentra documentos, series y fichas por su nombre. Úsalo cuando tienes muchos materiales guardados y quieres dar con uno concreto sin recorrer carpetas, por ejemplo para localizar una práctica de hace meses, comprobar si ya tienes una serie sobre un tema o encontrar el documento vigente entre varias versiones.",
            example="Vas a preparar la clase de fracciones y escribes 'fracciones' en el buscador: aparecen la serie de lecciones, dos fichas y un documento de repaso. Reutilizas la ficha del año pasado en lugar de crearla otra vez.",
            tips=["Busca con palabras del título: los términos de menos de dos letras no se tienen en cuenta.",
                  "Nombrar bien los materiales (ver Nombrar y actualizar versiones) hace que la búsqueda funcione mejor."]),
        'ficha-de-trabajo-curso': dict(
            answer="Una ficha de trabajo es una hoja de práctica que el alumnado resuelve dentro del curso. Sirve para que practique lo que acaba de ver, con ejercicios que tú preparas y con sus propias respuestas. Úsala después de explicar un concepto, como repaso antes de un examen o cuando quieres que se practique en casa con la misma hoja que se ha visto en clase.",
            example="Tras la clase de ecuaciones de primer grado, añades en la sección 'Álgebra' una ficha con cinco ejercicios graduados. El alumnado la resuelve en casa y, en la sesión siguiente, empiezas por los ejercicios que más les costaron.",
            tips=["Empieza con un ejercicio resuelto, sigue con ejercicios parecidos y termina con uno más difícil.",
                  "Revísala como la haría un alumno antes de añadirla (ver Revisar una ficha antes de usarla)."]),
        'idioma-no-cambia': dict(
            answer="Si la interfaz sigue en el idioma anterior después de elegir otro, lo más habitual es que la página abierta todavía no haya cargado el cambio. Revisa primero la elección en el menú de cuenta y después recarga la página, sobre todo si acabas de cambiar el idioma y la pantalla sigue igual, o si un compañero ve la interfaz en otro idioma y no sabe por qué.",
            example="Cambias la interfaz a portugués en tu portátil, pero la pestaña que tenías abierta sigue en español. Recargas la página y el cambio se aplica a toda la interfaz. Los textos que ya escribiste siguen en el idioma en que los creaste.",
            tips=["El cambio afecta a la interfaz, no a los textos que ya creaste."]),
        'beta': dict(
            answer="Cursos está en beta: es una versión que se sigue mejorando, así que sus pantallas y opciones pueden cambiar. Si una pantalla no coincide con esta ayuda o una opción ha cambiado de lugar o de nombre, no es un error tuyo. Consulta esta ayuda buscando el nombre de la acción o revisa las novedades en el menú de cuenta.",
            example="Buscas el botón de importar y no está donde lo muestra la ayuda. La pantalla ha cambiado durante la beta: busca la acción por su nombre en el buscador de la ayuda o mira las novedades en el menú de cuenta.",
            tips=["Cuando algo no coincida, guarda una captura de pantalla: ayuda a explicar el cambio a quien dé soporte."]),
        'idioma': dict(
            answer="Cambia el idioma de los menús y botones de Seven Assistant, entre español y portugués de Brasil, sin alterar el contenido que ya has creado. Úsalo cuando trabajas con colegas que usan otro idioma, cuando compartes equipo con alguien que prefiere otro idioma o cuando quieres que la interfaz coincida con los materiales que preparas.",
            example="Tú trabajas en español y una compañera de Brasil usa la misma herramienta. Cada una cambia el idioma en su propia cuenta: los menús se ven en su idioma y los cursos siguen en el idioma en que se crearon.",
            tips=["Los textos que escribes tú se quedan en el idioma en que los creaste."]),
        'plantilla-nombrar': dict(
            answer="Nombrar bien tus asistentes sirve para encontrarlos sin abrirlos uno a uno cuando tienes varios. Úsalo cuando tienes más de tres asistentes, cuando los compartes con otros docentes o cuando creas uno para una tarea que repites cada trimestre: un nombre con el tipo de tarea y el nivel te dice al momento para qué es cada uno.",
            example="Tienes un asistente que corrige redacciones de 1.º de ESO y otro que prepara guías de laboratorio para bachillerato. Con los nombres 'Redacción · 1.º ESO' y 'Guía de laboratorio · bachillerato' sabes cuál usar sin abrir ninguno."),
        'ficha-revisar': dict(
            answer="Revisar una ficha consiste en resolverla tú antes de que llegue al alumnado, para detectar ejercicios mal planteados, respuestas erróneas o un nivel que no es el de tu grupo. Hazlo cuando la hayas generado con el asistente, cuando vayas a usar una ficha de otro curso o cuando quieras asegurarte de que una práctica corresponde a lo visto antes de un examen.",
            example="Generas una ficha de 'Porcentajes' para 2.º de ESO. Al resolver el ejercicio 3 ves que el enunciado pide un cálculo que todavía no se ha explicado en clase. Lo cambias por un ejercicio parecido antes de compartirla.",
            tips=["Si tú tardas mucho más de lo que tardaría el alumnado, la ficha probablemente es demasiado difícil."]),
        'respuesta-no-correcta': dict(
            answer="El asistente puede dar datos equivocados o responder a otra pregunta. Sirve para saber cómo comprobar una respuesta antes de usarla en clase y cómo pedir una mejor. Revisa la respuesta cuando contenga cifras, fechas o citas que no sepas si son ciertas, cuando hable de otro nivel, país o formato, o cuando esté bien pero no sirva para tu grupo.",
            example="Pides un resumen de la Revolución francesa para 4.º de ESO y la respuesta incluye una fecha que no cuadra. La compruebas en tu libro de texto, pides que la corrija y añades 'alumnado de 14 años, resumen de 10 líneas'. La segunda respuesta sirve.",
            tips=["No uses en clase un dato de la respuesta sin contrastarlo antes.",
                  "Cambia una cosa a la vez al pedir ajustes."]),
        'configuracion-cuenta': dict(
            answer="Configuración reúne los ajustes generales de tu cuenta, no los de un curso concreto. Úsala cuando quieras revisar tus datos o cambiar un ajuste que afecta a toda tu cuenta; para cambiar algo de un curso, como el código de inscripción, usa la configuración de ese curso.",
            example="Si quieres cambiar el código de inscripción de un curso, eso está en la configuración de ese curso. Si quieres cambiar tus datos o el idioma de la interfaz, eso está en el menú de cuenta.",
            tips=["No confundas Configuración de la cuenta (avatar) con Configuración del curso (dentro de Cursos)."]),
        'serie-ajustar': dict(
            answer="Ajustar una serie es modificar una serie de lecciones que ya tienes para que encaje con tu grupo. Sirve cuando la primera versión tiene más sesiones de las que puedes dar, cuando el nivel no es el de tu grupo o cuando la evaluación no coincide con tu programación. Pide los cambios en una conversación y revisa la progresión antes de guardarla.",
            example="La serie de 'Fracciones' tiene doce sesiones y tú tienes ocho. En una conversación pides que la reduzca a ocho manteniendo la progresión, con la evaluación en la sesión 8. Revisas la progresión antes de guardarla."),
        'alumnado-no-entra': dict(
            answer="Cuando el alumnado no consigue entrar en el curso, casi siempre el problema está en el código o en el camino de entrada. Revisa esas dos cosas, en ese orden, si un grupo entero no puede entrar tras recibir el código, si un alumno dice que el código no funciona o si quieres ver cómo aparece el curso para el alumnado antes de la primera clase.",
            example="Al empezar el curso, cuatro alumnos escriben el código y reciben un error. En la vista general ves que el código que tienen es el anterior, porque generaste uno nuevo la semana pasada. Compartes el nuevo y todos entran sin problema.",
            tips=["Comprueba la vista de estudiante antes de compartir el código con el grupo."]),
        'plantillas-vs-asistentes': dict(
            answer="Las plantillas de curso son unidades didácticas listas para adoptar dentro de Cursos, mientras que los asistentes son plantillas de la barra lateral con instrucciones propias. Usa una plantilla de curso cuando quieras empezar con una unidad ya preparada, y un asistente de IA cuando quieras que la IA siga tus instrucciones para tus tareas.",
            example="Si necesitas una unidad sobre 'El agua' para un curso de 3.º de primaria, buscas en Cursos, en la pestaña Plantillas. Si quieres un asistente que corrija tus redacciones con tus criterios, lo creas en Plantillas (icono de estrellas) con tus instrucciones.",
            tips=["Si quieres contenido ya hecho, es una plantilla de curso; si quieres que la IA trabaje con tus instrucciones, es un asistente."]),
        'no-encuentro-seccion': dict(
            answer="Las áreas principales están siempre en la barra lateral, y lo que no aparece allí suele estar dentro de un curso, en la Biblioteca o en el menú de cuenta. Sirve para localizar rápido cada cosa: busca en la Biblioteca si buscas una serie, una ficha o una tarea, y en el menú de cuenta si buscas un ajuste general.",
            example="Quieres crear una serie de lecciones y no la encuentras en Cursos. Las series se crean desde la Biblioteca, así que vas allí y la creas desde ahí.",
            tips=["Si buscas un ajuste de un curso concreto, está dentro de ese curso, en Configuración."]),
        'codigo-filtrado': dict(
            answer="Si un código o enlace de inscripción ha llegado a personas que no deben entrar, sustitúyelo por uno nuevo y desactiva el enlace público si ya no lo necesitas. Hazlo cuando el código se haya compartido fuera de la clase o cuando un enlace público siga activo al terminar el curso, para que solo entre tu grupo.",
            example="Has compartido el código en un grupo de familias y alguien ajeno al curso lo ha usado. Generas un código nuevo, lo compartes solo con tu grupo y desactivas el enlace público si ya no lo necesitas.",
            tips=["Si necesitas que alguien concreto entre, compártelo solo con esa persona."]),
        'regenerar-respuesta': dict(
            answer="Regenerar una respuesta pide al asistente que vuelva a contestar a la misma pregunta. Úsala cuando la respuesta es floja, genérica, demasiado larga o no sigue el formato que necesitas, sin tener que reescribir la pregunta desde cero. Si la nueva respuesta tampoco convence, vuelve a regenerarla.",
            example="Pides una lista de actividades para 5.º de primaria y la primera es demasiado teórica. Regeneras la respuesta y obtienes otra propuesta más práctica; si no te convence, la regeneras otra vez."),
        'menu-de-cuenta': dict(
            answer="El menú de cuenta está en el avatar de la parte inferior izquierda, con tus iniciales, y sirve para ajustar tu cuenta, cambiar el idioma, gestionar tareas y carpetas compartidas, y cerrar sesión. Úsalo para cambiar el idioma, revisar tus tareas o carpetas compartidas, o cerrar sesión cuando estés en un equipo que no es tuyo.",
            example="Estás en un equipo del centro y terminas de trabajar. Abres el menú con tu avatar, eliges Cerrar sesión y tu cuenta queda protegida en ese equipo.",
            tips=["Cierra sesión si usas un equipo compartido."]),
        'tarea-calibrar': dict(
            answer="Calibrar es corregir unos pocos trabajos de distintos niveles y compararlos con la propuesta de corrección antes de corregir a todo el grupo, para que los criterios signifiquen lo mismo en todos los trabajos. Hazlo cuando acabas de escribir los criterios, cuando vas a corregir muchos trabajos seguidos o cuando varias personas corrigen la misma tarea.",
            example="Tienes 28 redacciones y los criterios de 'argumentación'. Corriges tres (una débil, una media y una fuerte). En dos de ellas no sabes si el criterio se cumple: reescribes el criterio con un ejemplo y corriges el resto del grupo con él.",
            tips=["Guarda los tres trabajos calibrados: te servirán de referencia si tienes dudas más adelante."]),
        'documentos-nombres': dict(
            answer="Un nombre con materia, grupo, fecha y versión deja claro qué documento está vigente cuando hay varias versiones en la Biblioteca. Úsalo al subir la versión corregida de una unidad, al compartir un documento con el departamento o al revisar la Biblioteca al empezar el curso, para no confundir una versión antigua con la actual.",
            example="Tienes 'Unidad 4 · v1' y 'Unidad 4 · v2'. Subes la versión corregida como 'Matemáticas · 2.º de ESO · 2026-11 · v2' y conservas la v1 solo si la necesitas para comparar. Así sabes cuál enviar al alumnado.",
            tips=["Revisa cada año qué documentos siguen vigentes."]),
        'exportar-curso': dict(
            answer="Exportar un curso guarda una copia completa de su contenido en un archivo, en el formato que necesite la otra herramienta. Úsalo para tener una copia de seguridad antes de archivar un curso, para llevarlo a Moodle (formato .mbz) o para reutilizarlo en otro sistema compatible con IMS Common Cartridge.",
            example="Terminas el curso de 4.º de ESO en junio. Lo exportas como copia de seguridad de Moodle (.mbz), lo guardas en la carpeta del centro y, si el año siguiente lo necesitas en Moodle, lo importas allí.",
            tips=["Haz una copia de seguridad al terminar el curso, antes de archivarlo."]),
        'tipo-de-actividad': dict(
            answer="Hay cinco tipos de actividad: material para leer o ver, ficha para practicar, entrega para recibir un archivo, tarea con comentarios para devolver una corrección y agente de IA para resolver dudas. Elige según lo que quieres comprobar y lo que vas a recibir de vuelta, porque así evitas crear algo que no te sirve.",
            example="Quieres comprobar si el alumnado ha entendido la fotosíntesis. Creas una ficha con tres ejercicios para practicar en casa. Si después quieres su texto escrito, añades una entrega; si quieres devolverle comentarios sobre ese texto, usas una tarea con comentarios."),
        'agregar-material-archivo': dict(
            answer="Un material con archivo es una pieza que el alumnado puede abrir dentro de la sección del curso, como un PDF, una presentación o cualquier documento que ya tengas. Úsalo para tener los recursos de clase en el mismo sitio donde el alumnado los busca, por ejemplo una ficha de apoyo junto a la actividad, y déjalo oculto hasta el día de la clase si hace falta.",
            example="El martes explicas la célula. Subes 'ficha-apoyo-celula.pdf' como material en la sección 'La célula' y lo dejas oculto. Al empezar la clase lo haces visible y el alumnado ya lo tiene en su curso.",
            tips=["En el título, di lo que contiene y no solo el nombre del archivo: 'Ficha de apoyo: partes de la célula' se entiende mejor que 'Doc1'."]),
        'enlace-y-nota': dict(
            answer="Un enlace y una nota son materiales ligeros dentro de la sección: el enlace lleva a una página web con un título, y la nota es un texto breve que el alumnado lee sin abrir nada más. Úsalos para dar una referencia que hay que consultar, para recordar una fórmula o un aviso, o para señalar una fecha sin crear una actividad.",
            example="En la sección de práctica de microscopía añades un enlace a una guía de uso del microscopio óptico y una nota: 'Recuerda: el aumento total es el producto del aumento del objetivo por el del ocular.' El alumnado tiene la referencia y la fórmula a la vista.",
            tips=["Usa una nota para lo que hay que recordar y un enlace para lo que hay que consultar."]),
        'organizacion-centro': dict(
            answer="Organizar los cursos del centro es acordar cómo se nombran (asignatura, clase o curso escolar y año) antes de crear muchos cursos, para que cualquier docente o coordinador reconozca cada curso sin preguntar. Hazlo al preparar los cursos del nuevo año o cuando coordinas a varios docentes que deben usar el mismo formato.",
            example="En un instituto con cinco profesores de Matemáticas, todos usan el formato 'Matemáticas · 2.º ESO · 2026-2027'. Así la coordinación ve de un vistazo qué curso corresponde a cada grupo y no se crean cursos repetidos."),
        'secciones': dict(
            answer="Una sección agrupa el contenido de un curso en un bloque, por ejemplo una unidad didáctica. Sirve para que el alumnado encuentre cada tema en su sitio y para reorganizar el curso por bloques sin mezclar materiales. Úsala cuando quieres dividir el curso por unidades o trimestres y que el alumnado vea en orden qué tiene que hacer en cada bloque.",
            example="En un curso de Historia creas una sección por tema: 'Revolución industrial', 'Imperialismo' y 'Primera Guerra Mundial'. Dentro de cada una añades el material, la ficha de práctica y la entrega, y el alumnado sabe en qué bloque está cada cosa."),
        'serie-campos': dict(
            answer="Una serie de lecciones se define con pocos campos: Tema es obligatorio y los demás ayudan a encontrarla y a que salga adaptada a tu grupo. Rellénalos bien desde el principio cuando vayas a crear una serie nueva, o cuando tienes muchas series y necesitas encontrarlas por asignatura o curso.",
            example="Para una serie de 'Introducción al cálculo integral' rellenas Tema, Asignatura 'Matemáticas', Curso '1.º de bachillerato' y, en Descripción, indicas que el alumnado ya conoce las derivadas. Con esos datos la serie sale a su nivel y después la encuentras por asignatura.",
            tips=["Cuanto más concreta sea la descripción, mejor encajará la serie con tu grupo."]),
        'tarea-criterios': dict(
            answer="Un criterio observable describe algo que puedes ver en el trabajo del alumnado, y sirve para corregir con la misma vara de medir y explicar la nota con claridad. Úsalo cuando vas a corregir un trabajo con varios aspectos que evaluar o cuando quieres que el alumnado entienda por qué ha obtenido cada nota.",
            example="En lugar de 'buena argumentación', el criterio dice 'Presenta al menos dos evidencias que apoyen su tesis'. Al corregir, la evidencia está o no está, y al devolver el trabajo puedes señalar exactamente qué falta."),
    },
    'pt-BR': {
        'buscar-contenido': dict(
            answer="O buscador da Biblioteca encontra documentos, séries e fichas pelo nome. Use quando tiver muitos materiais guardados e quiser achar um específico sem percorrer pastas, por exemplo para localizar uma prática feita meses atrás, conferir se já existe uma série sobre um tema ou encontrar o documento vigente entre várias versões.",
            example="Você vai preparar a aula de frações e escreve 'frações' no buscador: aparecem a série de aulas, duas fichas e um documento de revisão. Reaproveita a ficha do ano passado em vez de criá-la de novo.",
            tips=["Use palavras do título: termos com menos de duas letras não entram na busca.",
                  "Nomear bem os materiais (veja Nomear e atualizar versões) melhora os resultados."]),
        'ficha-de-trabajo-curso': dict(
            answer="Uma ficha de trabalho é uma folha de prática que o estudante resolve dentro do curso. Serve para que ele treine o que acabou de ver, com exercícios que você prepara e com as próprias respostas. Use depois de explicar um conceito, como revisão antes de uma prova ou quando quer que treinem em casa com a mesma folha vista em aula.",
            example="Depois da aula de equações do 1.º grau, você adiciona na seção 'Álgebra' uma ficha com cinco exercícios graduados. Os estudantes resolvem em casa e, na aula seguinte, você começa pelos exercícios que mais deram trabalho.",
            tips=["Comece com um exercício resolvido, siga com exercícios parecidos e termine com um mais difícil.",
                  "Revise a ficha como faria um estudante antes de adicioná-la (veja Revisar uma ficha antes de usar)."]),
        'idioma-no-cambia': dict(
            answer="Se a interface continua no idioma anterior depois de escolher outro, o mais comum é a página aberta ainda não ter carregado a mudança. Confira primeiro a escolha no menu da conta e depois recarregue a página, principalmente quando acabou de trocar o idioma e a tela continua igual, ou quando um colega vê a interface em outro idioma e não sabe por quê.",
            example="Você muda a interface para espanhol no notebook, mas a aba que já estava aberta continua em português. Recarregue a página e a mudança vale para toda a interface. Os textos que você já escreveu continuam no idioma em que foram criados.",
            tips=["A mudança afeta a interface, não os textos que você já criou."]),
        'beta': dict(
            answer="Cursos está em beta: é uma versão que continua sendo melhorada, por isso as telas e as opções podem mudar. Se uma tela não coincide com esta ajuda ou uma opção mudou de lugar ou de nome, não é um erro seu. Consulte a ajuda pelo nome da ação ou veja as novidades no menu da conta.",
            example="Você procura o botão de importar e ele não está onde a ajuda mostra. A tela mudou durante a fase beta: procure a ação pelo nome no buscador da ajuda ou veja as novidades no menu da conta.",
            tips=["Quando algo não coincidir, guarde uma captura de tela: ajuda a explicar a mudança para quem dá suporte."]),
        'idioma': dict(
            answer="Muda o idioma dos menus e botões do Seven Assistant, entre espanhol e português do Brasil, sem alterar o conteúdo que você já criou. Use quando trabalha com colegas que usam outro idioma, quando compartilha o computador com alguém que prefere outro idioma ou quando quer que a interface combine com os materiais que prepara.",
            example="Você trabalha em português e uma colega de Madrid usa a mesma ferramenta. Cada um muda o idioma na própria conta: os menus aparecem no idioma de cada um, e os cursos continuam no idioma em que foram criados.",
            tips=["Os textos que você escreve permanecem no idioma em que foram criados."]),
        'plantilla-nombrar': dict(
            answer="Dar bons nomes aos seus assistentes serve para encontrá-los sem abri-los um por um quando você tem vários. Use quando tiver mais de três assistentes, quando os compartilhar com outros docentes ou quando criar um para uma tarefa que repete todo trimestre: um nome com o tipo de tarefa e o nível mostra na hora para que serve cada um.",
            example="Você tem um assistente que corrige redações do 6.º ano e outro que prepara guias de laboratório para o ensino médio. Com os nomes 'Redação · 6.º ano' e 'Guia de laboratório · ensino médio' você sabe qual usar sem abrir nenhum."),
        'ficha-revisar': dict(
            answer="Revisar uma ficha é resolvê-la antes que ela chegue aos estudantes, para encontrar exercícios mal formulados, respostas erradas ou um nível que não é o da sua turma. Faça isso quando a ficha foi gerada pelo assistente, quando vai usar uma ficha de outro curso ou quando quer garantir que a prática corresponde ao que foi visto antes de uma prova.",
            example="Você gera uma ficha de 'Porcentagem' para o 7.º ano. Ao resolver o exercício 3, percebe que o enunciado pede um cálculo que ainda não foi explicado em aula. Troca por um exercício parecido antes de compartilhar.",
            tips=["Se você levar bem mais tempo do que levaria um estudante, a ficha provavelmente está difícil demais."]),
        'respuesta-no-correcta': dict(
            answer="O assistente pode dar dados errados ou responder a outra pergunta. Serve para saber como conferir uma resposta antes de usá-la em aula e como pedir uma melhor. Revise quando a resposta traz números, datas ou citações que você não sabe se são verdadeiros, quando fala de outro nível, país ou formato, ou quando está certa mas não serve para a sua turma.",
            example="Você pede um resumo da Revolução Francesa para o 9.º ano e a resposta inclui uma data que não bate com o livro. Confira a data no livro didático, peça a correção e acrescente 'alunos de 14 anos, resumo de 10 linhas'. A segunda resposta serve.",
            tips=["Não use em aula um dado da resposta sem conferi-lo antes.",
                  "Mude uma coisa de cada vez ao pedir ajustes."]),
        'configuracion-cuenta': dict(
            answer="Configurações reúne os ajustes gerais da sua conta, e não os de um curso específico. Use quando quiser revisar os seus dados ou mudar um ajuste que vale para toda a conta; para mudar algo de um curso, como o código de inscrição, use as Definições desse curso.",
            example="Se quer trocar o código de inscrição de um curso, isso fica nas definições desse curso. Se quer mudar o idioma da interface ou os seus dados, isso fica no menu da conta.",
            tips=["Não confunda Configurações da conta (avatar) com Definições do curso (dentro de Cursos)."]),
        'serie-ajustar': dict(
            answer="Ajustar uma série é modificar uma série de aulas que você já tem para que ela se encaixe na sua turma. Serve quando a primeira versão tem mais sessões do que você consegue dar, quando o nível não é o da sua turma ou quando a avaliação não coincide com o seu planejamento. Peça as mudanças em uma conversa e revise a progressão antes de guardar.",
            example="A série de 'Frações' tem doze sessões e você tem oito. Em uma conversa, peça que ela seja reduzida a oito, mantendo a progressão e com a avaliação na sessão 8. Revise a progressão antes de guardar."),
        'alumnado-no-entra': dict(
            answer="Quando o estudante não consegue entrar no curso, quase sempre o problema está no código ou no caminho de entrada. Revise essas duas coisas, nessa ordem, quando uma turma inteira não consegue entrar depois de receber o código, quando um estudante diz que o código não funciona ou quando quer ver como o curso aparece para ele antes da primeira aula.",
            example="No primeiro dia de aula, quatro estudantes digitam o código e recebem um erro. Na visão geral você vê que o código que eles têm é o antigo, porque gerou um novo na semana passada. Compartilhe o novo e todos conseguem entrar.",
            tips=["Confira a visão de estudante antes de compartilhar o código com a turma."]),
        'plantillas-vs-asistentes': dict(
            answer="Os modelos de curso são unidades didáticas prontas para adotar dentro de Cursos, enquanto os assistentes são modelos da barra lateral com instruções próprias. Use um modelo de curso quando quiser começar com uma unidade já pronta, e um assistente de IA quando quiser que a IA siga as suas instruções nas suas tarefas.",
            example="Se precisa de uma unidade sobre 'A água' para uma turma do 3.º ano, procure em Cursos, na aba Modelos. Se quer um assistente que corrija as suas redações com os seus critérios, crie-o em Modelos (ícone de estrelas) com as suas instruções.",
            tips=["Se quer um conteúdo já pronto, é um modelo de curso; se quer que a IA trabalhe com as suas instruções, é um assistente."]),
        'no-encuentro-seccion': dict(
            answer="As áreas principais estão sempre na barra lateral, e o que não aparece ali costuma estar dentro de um curso, na Biblioteca ou no menu da conta. Use esta ajuda para localizar cada coisa: procure na Biblioteca se busca uma série, uma ficha ou uma tarefa, e no menu da conta se busca um ajuste geral.",
            example="Você quer criar uma série de aulas e não a encontra em Cursos. As séries são criadas a partir da Biblioteca, então é lá que você a cria.",
            tips=["Se procura um ajuste de um curso específico, ele fica dentro desse curso, em Definições."]),
        'codigo-filtrado': dict(
            answer="Se um código ou link de inscrição chegou a pessoas que não deveriam entrar, substitua-o por um novo e desative o link público se não precisar mais dele. Faça isso quando o código foi compartilhado fora da turma ou quando um link público continua ativo depois do fim do curso, para que só entre a sua turma.",
            example="Você compartilhou o código em um grupo de famílias e alguém de fora da turma o usou. Gere um código novo, compartilhe-o apenas com a sua turma e desative o link público, se ele não for mais necessário.",
            tips=["Se precisar que alguém específico entre, compartilhe o código só com essa pessoa."]),
        'regenerar-respuesta': dict(
            answer="Gerar a resposta de novo pede ao assistente que responda outra vez à mesma pergunta. Use quando a resposta está fraca, genérica, longa demais ou fora do formato que você precisa, sem precisar reescrever a pergunta do zero. Se a nova resposta também não agradar, gere de novo.",
            example="Você pede uma lista de atividades para o 5.º ano e a primeira é teórica demais. Gera a resposta de novo e obtém outra proposta mais prática; se ainda não agradar, gera mais uma vez."),
        'menu-de-cuenta': dict(
            answer="O menu da conta fica no avatar, embaixo à esquerda, com as suas iniciais, e serve para ajustar a conta, trocar o idioma, gerenciar tarefas e pastas compartilhadas e encerrar a sessão. Use para mudar o idioma, revisar tarefas ou pastas compartilhadas, ou sair quando estiver em um computador que não é seu.",
            example="Você está em um computador da escola e terminou o trabalho. Abre o menu pelo avatar, escolhe Sair e a sua conta fica protegida nesse computador.",
            tips=["Encerre a sessão se usar um computador compartilhado."]),
        'tarea-calibrar': dict(
            answer="Calibrar é corrigir alguns trabalhos de níveis diferentes e compará-los com a proposta de correção antes de corrigir a turma inteira, para que os critérios signifiquem a mesma coisa em todos. Faça isso quando acabou de escrever os critérios, quando vai corrigir muitos trabalhos seguidos ou quando mais de uma pessoa corrige a mesma tarefa.",
            example="Você tem 28 redações e os critérios de 'argumentação'. Corrige três (uma fraca, uma média e uma forte). Em duas delas não sabe se o critério foi cumprido: reescreve o critério com um exemplo e corrige o restante da turma com ele.",
            tips=["Guarde os três trabalhos calibrados: eles servem de referência se você tiver dúvidas depois."]),
        'documentos-nombres': dict(
            answer="Um nome com disciplina, turma, data e versão deixa claro qual documento está vigente quando há várias versões na Biblioteca. Use ao enviar a versão corrigida de uma unidade, ao compartilhar um documento com o departamento ou ao revisar a Biblioteca no início do curso, para não confundir a versão antiga com a atual.",
            example="Você tem 'Unidade 4 · v1' e 'Unidade 4 · v2'. Envia a versão corrigida como 'Matemática · 8.º ano · 2026-11 · v2' e guarda a v1 só se precisar compará-las. Assim você sabe qual enviar aos estudantes.",
            tips=["Revise todo ano quais documentos ainda estão vigentes."]),
        'exportar-curso': dict(
            answer="Exportar um curso salva uma cópia completa do conteúdo em um arquivo, no formato que a outra ferramenta precisa. Use para ter uma cópia de segurança antes de arquivar um curso, para levá-lo ao Moodle (formato .mbz) ou para reaproveitá-lo em outro sistema compatível com IMS Common Cartridge.",
            example="Você termina o curso do 9.º ano em dezembro. Exporta como cópia de segurança do Moodle (.mbz), guarda o arquivo na pasta da escola e, se precisar dele no Moodle no ano seguinte, importa lá.",
            tips=["Faça uma cópia de segurança ao terminar o curso, antes de arquivá-lo."]),
        'tipo-de-actividad': dict(
            answer="Há cinco tipos de atividade: material para ler ou ver, ficha para praticar, entrega para receber um arquivo, tarefa com comentários para devolver uma correção e agente de IA para tirar dúvidas. Escolha de acordo com o que quer verificar e com o que vai receber de volta, assim você evita criar algo que não serve para o seu objetivo.",
            example="Você quer saber se a turma entendeu a fotossíntese. Cria uma ficha com três exercícios para treinar em casa. Se depois quiser o texto escrito deles, adiciona uma entrega; se quiser devolver comentários sobre o texto, usa uma tarefa com comentários."),
        'agregar-material-archivo': dict(
            answer="Um material com arquivo é uma peça que o estudante pode abrir dentro da seção do curso, como um PDF, uma apresentação ou qualquer documento que você já tenha. Use para deixar os recursos da aula onde os estudantes os procuram, por exemplo uma ficha de apoio junto da atividade, e deixe-o oculto até o dia da aula se for preciso.",
            example="Na terça você explica a célula. Envia 'ficha-apoio-celula.pdf' como material na seção 'A célula' e o deixa oculto. Quando começar a aula, torna o material visível e os estudantes já o têm no curso.",
            tips=["No título, diga o que o arquivo contém e não só o nome do arquivo: 'Ficha de apoio: partes da célula' é mais claro que 'Doc1'."]),
        'enlace-y-nota': dict(
            answer="Um link e uma nota são materiais leves dentro da seção: o link leva a uma página da web com um título, e a nota é um texto breve que o estudante lê sem abrir mais nada. Use para indicar uma referência que deve ser consultada, para lembrar uma fórmula ou um aviso ou para destacar um prazo sem criar uma atividade.",
            example="Na seção de prática de microscopia, você adiciona um link para um guia de uso do microscópio óptico e uma nota: 'Lembre-se: o aumento total é o produto do aumento da objetiva pelo da ocular.' O estudante tem a referência e a fórmula à vista.",
            tips=["Use uma nota para o que é preciso lembrar e um link para o que é preciso consultar."]),
        'organizacion-centro': dict(
            answer="Organizar os cursos da escola é combinar como eles são nomeados (disciplina, turma ou série e ano) antes de criar muitos cursos, para que qualquer docente ou coordenador reconheça cada curso sem perguntar. Faça isso ao preparar os cursos do novo ano letivo ou quando coordena vários docentes que devem usar o mesmo padrão.",
            example="Em uma escola com cinco professores de Matemática, todos usam o formato 'Matemática · 8.º ano · 2026'. Assim a coordenação vê de relance qual curso corresponde a cada turma e não se criam cursos repetidos."),
        'secciones': dict(
            answer="Uma seção agrupa o conteúdo de um curso em um bloco, por exemplo uma unidade didática. Serve para que o estudante encontre cada tema no lugar certo e para reorganizar o curso por blocos sem misturar materiais. Use quando quiser dividir o curso por unidades ou trimestres e que o estudante veja em ordem o que fazer em cada bloco.",
            example="Em um curso de História, você cria uma seção por tema: 'Revolução Industrial', 'Imperialismo' e 'Primeira Guerra Mundial'. Dentro de cada uma coloca o material, a ficha de prática e a entrega, e o estudante sabe em que bloco está cada coisa."),
        'serie-campos': dict(
            answer="Uma série de aulas é definida com poucos campos: Tema é obrigatório, e os demais ajudam a encontrá-la e a fazer com que ela saia adaptada à sua turma. Preencha-os bem desde o início ao criar uma série nova, ou quando tem muitas séries e precisa encontrá-las por disciplina ou curso.",
            example="Para uma série de 'Introdução ao cálculo integral', você preenche Tema, Disciplina 'Matemática', Curso '1.º ano do ensino médio' e, na Descrição, escreve que a turma já conhece derivadas. Com esses dados a série sai no nível certo, e depois você a encontra por disciplina.",
            tips=["Quanto mais concreta a descrição, melhor a série se encaixa na sua turma."]),
        'tarea-criterios': dict(
            answer="Um critério observável descreve algo que você consegue ver no trabalho do estudante, e serve para corrigir com a mesma régua e explicar a nota com clareza. Use quando for corrigir um trabalho com vários aspectos a avaliar ou quando quiser que o estudante entenda por que recebeu cada nota.",
            example="Em vez de 'boa argumentação', o critério diz 'Apresenta pelo menos duas evidências que sustentem a tese'. Ao corrigir, a evidência está ou não está, e ao devolver o trabalho você aponta exatamente o que falta."),
    },
}


def apply_content_overlay(merged: dict) -> None:
    """Aplica los textos ampliados a cada artículo publicado que exista en CONTENT."""
    for loc, items in CONTENT.items():
        for art in merged[loc]['articles']:
            new = items.get(art['id'])
            if not new:
                continue
            art['answer'] = new['answer']
            art['example'] = new.get('example', '')
            if 'tips' in new:
                art['tips'] = new['tips']


# ---------------------------------------------------------------------------
# Crear un curso: una sola guía. Absorbe "Importar un curso" y "Adoptar una plantilla de curso"
# (los pasos de esos artículos se añaden al final, con sus capturas, y sus URLs redirigen aquí).
# ---------------------------------------------------------------------------
GUIDE = {
    'es': dict(
        answer="Un curso reúne en un solo lugar lo que trabajas con un grupo: temas, materiales, actividades, citas y el código de entrada. Sirve para no repartir una asignatura entre carpetas, correos y chats. Puedes empezar desde cero, importar un curso que ya tienes o adoptar una plantilla.",
        example="En el colegio, un curso bien montado sirve para tres cosas: preparar una asignatura una sola vez y reutilizarla cada año, mantener el mismo formato de nombres en todo el departamento para encontrar cada curso sin preguntar, y que cada alumno llegue a su grupo desde el primer día con el código de su clase.",
        tips=["Usa un nombre que identifique grupo y asignatura, por ejemplo \"Matemáticas · 2.º secundaria\".",
              "Antes de la primera clase, abre el curso con \"Ver como estudiante\" para comprobar qué ve el alumnado.",
              "Revisa el curso importado antes de compartirlo, sobre todo las fechas y los datos que tengan que cambiar.",
              "Las plantillas actuales son de España, Alemania y Suiza. Revisa que encajen con el currículo de tu país antes de usarlas."],
        steps=[
            dict(t="Abre Cursos y pulsa Crear curso", b="Lo encontrarás en la parte superior derecha de la pantalla de cursos."),
            dict(t="Paso 1: Datos básicos", b="Escribe el nombre del curso, la asignatura, la clase o curso escolar y una descripción. Puedes añadir una portada."),
            dict(t="Paso 2: Elegir contenido", b="Vacío para empezar desde cero, Todas las plantillas para partir de una unidad preparada, Copiar para partir de un curso existente o Planificar con IA."),
            dict(t="Paso 3: Revisar y crear", b="Revisa los datos. Atrás te permite corregir algo antes de pulsar Crear."),
        ]),
    'pt-BR': dict(
        answer="Um curso reúne em um só lugar o que você trabalha com uma turma: temas, materiais, atividades, compromissos e o código de entrada. Serve para não espalhar uma disciplina entre pastas, e-mails e conversas. Você pode começar do zero, importar um curso que já tem ou adotar um modelo.",
        example="Na escola, um curso bem montado serve para três coisas: preparar uma disciplina uma vez só e reutilizá-la todo ano, manter o mesmo padrão de nomes em todo o departamento para encontrar cada curso sem perguntar, e fazer com que cada estudante chegue ao seu grupo desde o primeiro dia, com o código da sua turma.",
        tips=["Use um nome que identifique turma e disciplina, por exemplo \"Matemática · 8.º ano\".",
              "Antes da primeira aula, abra o curso com \"Ver como aluno\" para conferir o que os estudantes veem.",
              "Revise o curso importado antes de compartilhá-lo, principalmente as datas e os dados que precisam mudar.",
              "Os modelos atuais são da Espanha, da Alemanha e da Suíça. Confira se combinam com o currículo do seu país antes de usar."],
        steps=[
            dict(t="Abra Cursos e clique em Criar curso", b="Fica no canto superior direito da tela de cursos."),
            dict(t="Passo 1: Dados básicos", b="Escreva o nome do curso, a disciplina, a turma ou série e uma descrição. Você pode adicionar uma capa."),
            dict(t="Passo 2: Escolher conteúdo", b="Vazio para começar do zero, Todos os modelos para partir de uma unidade pronta, Copiar para partir de um curso existente ou Planejar com IA."),
            dict(t="Passo 3: Revisar e criar", b="Confira os dados. Voltar permite corrigir algo antes de clicar em Criar."),
        ]),
}
ABSORBED = ['importar-curso', 'plantillas-de-curso']   # se fusionan en crear-curso
KEEP = 'crear-curso'


def apply_course_merge(merged: dict) -> None:
    """Funde los artículos de importar y de plantillas en "Crear un curso" (después de numerar capturas)."""
    for loc, G in GUIDE.items():
        d = merged[loc]
        arts = {a['id']: a for a in d['articles']}
        keep = arts.get(KEEP)
        if keep is None:
            continue
        gone = [i for i in ABSORBED if i in arts]
        steps = [dict(t=s['t'], b=s['b']) for s in G['steps']]
        img = list(keep.get('img') or [])
        step_img = dict(keep.get('stepImg') or {})
        for gid in gone:                       # pasos y capturas de cada artículo absorbido, a continuación
            src = arts[gid]
            base = len(steps)
            for i, st in enumerate(src.get('steps') or []):
                steps.append({'t': st['t'], 'b': st['b']})
                k = (src.get('stepImg') or {}).get(str(i + 1))
                if k:
                    step_img[str(base + i + 1)] = k
            for k in src.get('img') or []:
                if k not in img:
                    img.append(k)
            keep['faqRelated'] = list(dict.fromkeys((keep.get('faqRelated') or []) + (src.get('faqRelated') or [])))
        steps = _apply_guide_steps(loc, steps)
        keep.update(answer=G['answer'], example=G['example'], tips=G['tips'], steps=steps, img=img, stepImg=step_img)
        d['articles'] = [a for a in d['articles'] if a['id'] not in gone]
        d.setdefault('aliases', {})
        for gid in gone:
            d['aliases'][gid] = KEEP           # enlaces antiguos → la guía
        for a in d['articles']:                # referencias relacionadas
            for field in ('related', 'faqRelated'):
                if a.get(field):
                    a[field] = [i for i in dict.fromkeys(KEEP if i in gone else i for i in a[field]) if i != a['id']]
        for g in d.get('courseGroups') or []:  # quitar los absorbidos de los grupos de cursos
            g['ids'] = [i for i in g['ids'] if i not in gone]


# ---------------------------------------------------------------------------
# Reescritura de todos los artículos (rewrites-es.py, rewrites-es-2.py, rewrites-pt.py).
# Cada entrada puede traer answer, example, tips y steps. Los pasos deben tener el mismo número
# que en el artículo publicado (si no, las capturas numeradas quedarían descolocadas).
# ---------------------------------------------------------------------------
def _load_rewrites(name: str, var: str):
    import importlib.util
    path = pathlib.Path(__file__).resolve().parent / f'{name}.py'
    if not path.exists():
        return None
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, var)


def apply_rewrites(merged: dict) -> None:
    sources = {
        'es': [_load_rewrites('rewrites-es', 'REWRITES'), _load_rewrites('rewrites-es-2', 'REWRITES_2')],
        'pt-BR': [_load_rewrites('rewrites-pt', 'REWRITES')],
    }
    for loc, dicts in sources.items():
        arts = {a['id']: a for a in merged[loc]['articles']}
        n = 0
        for rw in dicts:
            for aid, new in (rw or {}).items():
                art = arts.get(aid)
                if art is None:
                    continue
                if 'steps' in new:
                    old = art.get('steps') or []
                    if len(new['steps']) != len(old):
                        raise SystemExit(f"{loc} · {aid}: {len(new['steps'])} pasos nuevos, {len(old)} en el artículo")
                    art['steps'] = [dict(t=s['t'], b=s['b']) for s in new['steps']]
                for key in ('answer', 'example'):
                    if key in new:
                        art[key] = new[key]
                if 'tips' in new:
                    art['tips'] = list(new['tips'])
                n += 1
        print(f'  {loc}: {n} artículos reescritos')


# Pasos de «Crear un curso» (10, como en la guía). Sustituyen a los textos de clics de la fusión;
# las capturas siguen en los pasos 1, 2, 3, 5, 7 y 9.
GUIDE_STEPS = {
    'es': [
        {'t': 'Abre Cursos y pulsa Crear curso', 'b': 'Es el punto de partida para cualquier curso nuevo. Lo que decidas en los pasos siguientes se puede ajustar después, así que no hace falta acertar a la primera.'},
        {'t': 'Paso 1: Datos básicos', 'b': 'El nombre, la asignatura y la clase son lo que ves en tu lista de cursos y lo que el alumnado busca al entrar. Usa el formato que sigue tu centro, porque pronto tendrás varios cursos parecidos.'},
        {'t': 'Paso 2: Elegir contenido', 'b': 'Vacío si quieres construir el curso tú; Todas las plantillas si partes de una unidad ya preparada; Copiar si quieres reutilizar un curso tuyo; Planificar con IA si quieres una primera propuesta que después revisas.'},
        {'t': 'Paso 3: Revisar y crear', 'b': 'Compruebas los datos antes de crear el curso. Mientras no pulses Crear, no se guarda nada, así que puedes volver atrás para corregir cualquier dato.'},
        {'t': 'Importar un curso que ya tienes', 'b': 'Si tienes un curso exportado, o un compañero te lo ha compartido, no hace falta rehacerlo: el botón Importar curso lo trae a tu lista.'},
        {'t': 'Elige el archivo', 'b': 'Selecciona el archivo del curso que quieres traer. Si no se abre, comprueba que sea un curso exportado desde Seven Assistant.'},
        {'t': 'Abre la pestaña Plantillas', 'b': 'Dentro de Cursos, Plantillas reúne unidades didácticas listas para adoptar. Filtra por país, materia, curso y tipo de centro para encontrar la que encaja con tu currículo.'},
        {'t': 'Pulsa Adoptar', 'b': 'Se crea un curso nuevo con todos los bloques de la plantilla, que después puedes editar.'},
        {'t': 'Confirma con Crear curso', 'b': 'Revisa la confirmación y pulsa Crear curso. Si lo prefieres, Ahora no cancela sin crear nada.'},
        {'t': 'Adapta el curso', 'b': 'Cambia el nombre, la descripción y el contenido en Configuración y en las secciones. Una plantilla es un punto de partida: ajústala a tu grupo y a tu país.'},
    ],
    'pt-BR': [
        {'t': 'Abra Cursos e clique em Criar curso', 'b': 'É o ponto de partida para qualquer curso novo. O que você decidir nos passos seguintes pode ser ajustado depois, então não precisa acertar de primeira.'},
        {'t': 'Passo 1: Dados básicos', 'b': 'Nome, disciplina e turma são o que você vê na sua lista de cursos e o que o estudante procura ao entrar. Use o formato que a sua escola segue, porque logo você terá vários cursos parecidos.'},
        {'t': 'Passo 2: Escolher conteúdo', 'b': 'Vazio se quiser montar o curso você mesmo; Todos os modelos se partir de uma unidade pronta; Copiar para reaproveitar um curso seu; Planejar com IA para receber uma primeira proposta que você revisa.'},
        {'t': 'Passo 3: Revisar e criar', 'b': 'Confira os dados antes de criar. Enquanto você não clicar em Criar, nada é salvo, então pode voltar para corrigir qualquer informação.'},
        {'t': 'Importar um curso que você já tem', 'b': 'Se você já tem um curso exportado, ou um colega o compartilhou, não precisa refazê-lo: o botão Importar curso o traz para a sua lista.'},
        {'t': 'Escolha o arquivo', 'b': 'Selecione o arquivo do curso que quer trazer. Se ele não abrir, confirme que é um curso exportado do Seven Assistant.'},
        {'t': 'Abra a aba Modelos', 'b': 'Em Cursos, a aba Modelos reúne unidades didáticas prontas para adotar. Filtre por país, disciplina, série e tipo de escola para achar a que combina com o seu currículo.'},
        {'t': 'Clique em Adotar', 'b': 'É criado um curso novo com todos os blocos do modelo, que você pode editar depois.'},
        {'t': 'Confirme com Criar curso', 'b': 'Revise a confirmação e clique em Criar curso. Se preferir, Agora não cancela sem criar nada.'},
        {'t': 'Adapte o curso', 'b': 'Mude o nome, a descrição e o conteúdo em Definições e nas seções. O modelo é um ponto de partida: ajuste-o ao seu grupo e ao seu país.'},
    ],
}


def _apply_guide_steps(loc, steps):
    """Sustituye los pasos fusionados por los de GUIDE_STEPS (mismo número, mismas capturas)."""
    new = GUIDE_STEPS.get(loc)
    if new is None:
        return steps
    if len(new) != len(steps):
        raise SystemExit(f"{loc}: GUIDE_STEPS tiene {len(new)} pasos y la fusión {len(steps)}")
    return [dict(t=s['t'], b=s['b']) for s in new]


# ---------------------------------------------------------------------------
# Reorganización de Cursos: artículos que se funden en otro (su contenido pasa al nuevo).
#  - secciones absorbe actividades y tipo de actividad: pasos, capturas y enlaces van juntos.
#  - configuración del curso absorbe la vista del curso: es un ajuste de Visualización.
# Los textos finales (TEXT) sustituyen a los pasos fusionados; el número de pasos debe coincidir.
# ---------------------------------------------------------------------------
MERGE_SPECS = {
    'secciones': {'absorb': ['actividades', 'tipo-de-actividad'], 'steps': True, 'steps_from': ['actividades']},
    'configuracion-del-curso': {'absorb': ['vistas-del-curso', 'ia-alumnado', 'exportar-curso'], 'steps': False, 'images': False},
    'serie-de-lecciones': {'absorb': ['serie-campos', 'serie-ajustar'], 'steps': False, 'images': False},
}
MERGE_TEXT = {
    'es': {
        'secciones': {
            'title': 'Organizar el curso: secciones, actividades y materiales',
            'answer': 'Una sección es un bloque del curso, como una unidad o un trimestre, y es donde reúnes lo que trabajas con el alumnado: materiales, actividades y entregas. Sirve para que el curso se lea en orden y para que cada tema tenga su sitio. Úsala al montar el curso: crea una sección por tema y, dentro de cada una, añade lo que el alumnado tiene que ver o hacer.',
            'example': 'En un curso de Historia creas una sección por tema: «Revolución industrial», «Imperialismo» y «Primera Guerra Mundial». Dentro de cada una pones el texto explicativo, un enlace a un documental, la ficha para practicar y la entrega del trabajo, y el alumnado sabe en qué bloque está cada cosa.',
            'tips': ['Pon un nombre que describa el bloque: «La célula, unidad de los seres vivos» informa mejor que «Tema 1».'],
            'steps': [
                {'t': 'Localiza las secciones', 'b': 'Cada tarjeta numerada es un bloque del curso. Así ves de un vistazo qué temas tienes creados y cuánto contenido tiene cada uno.'},
                {'t': 'Añade una sección', 'b': 'Crea una sección por cada tema nuevo. Es mejor tener varias cortas que una larga: el alumnado sabe dónde buscar cada cosa.'},
                {'t': 'Gestiona una sección', 'b': 'Desde el menú (…) de cada sección accedes a sus opciones. Revísalas al reorganizar el curso al empezar un trimestre.'},
                {'t': 'Pulsa Añadir actividad o material', 'b': 'Dentro de la sección, este botón es la puerta de entrada a todo lo que el alumnado ve o hace. Úsalo en la sección del tema correspondiente para que la actividad quede junto a su contenido.'},
                {'t': 'Elige el tipo', 'b': 'Material, Texto, Enlace, Nota, Ficha de trabajo, Tarea con comentarios, Entrega, Unidad didáctica, Agente de IA y Crear con IA. Elige según lo que quieres que el alumnado haga después: leer, practicar, entregar o recibir una devolutiva.'},
                {'t': 'Completa el formulario', 'b': 'Cada tipo tiene su propio formulario. La actividad aparece en la sección cuando pulsas «Añadir»; ponle un título que el alumnado entienda sin contexto.'},
                {'t': 'Quiero que lean o vean algo', 'b': 'Material o Texto. Para contenido que el alumnado consulta antes o después de la clase: apuntes, vídeos o lecturas. Lo explicamos en «Añadir un material con archivo» y «Escribir un material de lectura».'},
                {'t': 'Quiero que practiquen', 'b': 'Ficha de trabajo. Para ejercicios que el alumnado resuelve por su cuenta y que luego repasas en clase.'},
                {'t': 'Quiero que me entreguen un archivo', 'b': 'Entrega. Para recibir un trabajo, un PDF o un documento, con fecha límite. Consulta «Crear una entrega».'},
                {'t': 'Quiero devolutiva sobre su trabajo', 'b': 'Tarea con comentarios. Para corregir y devolver comentarios sobre un trabajo, y no solo recibirlo. Consulta «Añadir una tarea con comentarios a un curso».'},
                {'t': 'Quiero un asistente para sus dudas', 'b': 'Agente de IA, con instrucciones claras. Resuelve dudas fuera de clase; las instrucciones deciden si da pistas o soluciones, así que define bien ese límite.'},
            ],
        },
        'configuracion-del-curso': {
            'answer': 'La pestaña Configuración reúne los ajustes del curso: general, portada, visualización, código de inscripción, IA, exportación y archivado. Sirve para dejar el curso listo para tu grupo y revisarlo al empezar cada trimestre o al cerrar el curso.',
            'example': 'Al empezar el trimestre cambias la visualización a Lista con vista previa, para que el alumnado vea de un vistazo de qué trata cada material. Al terminar el curso, lo exportas como copia de seguridad y lo archivas.',
            'steps': [
                {'t': 'General', 'b': 'Nombre, Asignatura, Clase o curso escolar y Descripción. Son los datos que identifican el curso en tu lista y en la del centro, así que mantenlos con el formato que acordéis. Pulsa «Aplicar cambios» para guardarlos.'},
                {'t': 'Portada', 'b': 'La imagen que se ve en el curso, en la lista de cursos y en la página de inscripción. Una portada reconocible ayuda a encontrar el curso correcto entre varios.'},
                {'t': 'Visualización', 'b': 'Aquí eliges cómo ve el alumnado las secciones y los contenidos. Lista es la más compacta, útil con muchos contenidos. Lista con vista previa muestra las primeras líneas de cada uno y suele ser la más clara. Mosaicos muestra cada sección como tarjetas, bien para materiales visuales. Secciones como mosaicos da a cada sección su propia página. «Contenido anterior y siguiente» enlaza cada contenido con el anterior y el siguiente.'},
                {'t': 'Código de inscripción', 'b': 'El código, el enlace público (desactivado por defecto) y «Generar nuevo código». Genera un código nuevo si se ha compartido fuera de la clase, y desactiva el enlace público cuando termine la inscripción.'},
                {'t': 'IA en el curso', 'b': 'Qué puede hacer el alumnado con la IA. Antes de decidir, lee el artículo «IA para el alumnado y el Tutor de IA».'},
                {'t': 'Exportación y archivado', 'b': 'Exportar el curso o archivarlo y salir. Antes de archivar, revisa que no lo necesitas para otro grupo, y haz una copia de seguridad si quieres conservarlo.'},
            ],
        },
    },
    'pt-BR': {
        'secciones': {
            'title': 'Organizar o curso: seções, atividades e materiais',
            'answer': 'Uma seção é um bloco do curso, como uma unidade ou um trimestre, e é onde você reúne o que trabalha com o estudante: materiais, atividades e entregas. Serve para o curso ser lido em ordem e para cada tema ter o seu lugar. Use ao montar o curso: crie uma seção por tema e, dentro de cada uma, acrescente o que o estudante precisa ver ou fazer.',
            'example': 'Em um curso de História, você cria uma seção por tema: "Revolução Industrial", "Imperialismo" e "Primeira Guerra Mundial". Dentro de cada uma coloca o texto explicativo, um link para um documentário, a ficha de prática e a entrega do trabalho, e o estudante sabe em que bloco está cada coisa.',
            'tips': ['Dê um nome que descreva o bloco: "A célula, unidade dos seres vivos" informa melhor do que "Tema 1".'],
            'steps': [
                {'t': 'Localize as seções', 'b': 'Cada cartão numerado é um bloco do curso. Você vê de relance quais temas já criou e quanto conteúdo cada um tem.'},
                {'t': 'Adicione uma seção', 'b': 'Crie uma seção para cada tema novo. Várias seções curtas são melhores do que uma longa: o estudante sabe onde procurar cada coisa.'},
                {'t': 'Gerencie uma seção', 'b': 'Pelo menu (…) de cada seção você acessa as suas opções. Revise-as ao reorganizar o curso no início de um trimestre.'},
                {'t': 'Clique em Adicionar atividade ou material', 'b': 'Dentro da seção, este botão é a porta de entrada para tudo o que o estudante vê ou faz. Use-o na seção do tema correspondente, para que a atividade fique junto do seu conteúdo.'},
                {'t': 'Escolha o tipo', 'b': 'Material, Texto, Link, Nota, Ficha de trabalho, Tarefa com comentários, Entrega, Unidade didática, Agente de IA e Criar com IA. Escolha pelo que você quer que o estudante faça depois: ler, praticar, entregar ou receber uma devolutiva.'},
                {'t': 'Preencha o formulário', 'b': 'Cada tipo tem o seu formulário. A atividade aparece na seção quando você clica em Adicionar; dê a ela um título que o estudante entenda sem contexto.'},
                {'t': 'Quero que leiam ou vejam algo', 'b': 'Material ou Texto. Para conteúdo que o estudante consulta antes ou depois da aula: anotações, vídeos ou leituras. Veja "Adicionar um material com arquivo" e "Escrever um material de leitura".'},
                {'t': 'Quero que pratiquem', 'b': 'Ficha de trabalho. Para exercícios que o estudante resolve por conta própria e que você revisa depois em aula.'},
                {'t': 'Quero que me entreguem um arquivo', 'b': 'Entrega. Para receber um trabalho, um PDF ou um documento, com prazo. Veja "Criar uma entrega".'},
                {'t': 'Quero uma devolutiva sobre o trabalho', 'b': 'Tarefa com comentários. Para corrigir e devolver comentários sobre um trabalho, e não só recebê-lo. Veja "Adicionar uma tarefa com comentários a um curso".'},
                {'t': 'Quero um assistente para as dúvidas', 'b': 'Agente de IA, com instruções claras. Responde dúvidas fora da aula; as instruções definem se ele dá pistas ou soluções, então defina bem esse limite.'},
            ],
        },
        'configuracion-del-curso': {
            'answer': 'A aba Definições reúne os ajustes do curso: geral, capa, visualização, código de inscrição, IA, exportação e arquivamento. Serve para deixar o curso pronto para a sua turma e revisá-lo ao começar cada trimestre ou ao encerrar o curso.',
            'example': 'No início do trimestre você muda a visualização para Lista com visualização prévia, para o estudante ver de relance do que trata cada material. Ao terminar o curso, você o exporta como cópia de segurança e o arquiva.',
            'steps': [
                {'t': 'Geral', 'b': 'Nome, Disciplina, Turma ou série e Descrição. São os dados que identificam o curso na sua lista e na da escola, então mantenha-os no formato combinado. Clique em "Aplicar alterações" para salvá-los.'},
                {'t': 'Capa', 'b': 'A imagem que aparece no curso, na lista de cursos e na página de inscrição. Uma capa reconhecível ajuda a achar o curso certo entre vários.'},
                {'t': 'Visualização', 'b': 'Aqui você escolhe como o estudante vê as seções e os conteúdos. Lista é a mais compacta, útil com muitos conteúdos. Lista com visualização prévia mostra as primeiras linhas de cada um e costuma ser a mais clara. Mosaicos mostra cada seção como cartões, bom para materiais visuais. Seções como mosaicos dá a cada seção a sua própria página. "Conteúdo anterior e seguinte" liga cada conteúdo ao anterior e ao seguinte.'},
                {'t': 'Código de inscrição', 'b': 'O código, o link público (desativado por padrão) e "Gerar novo código". Gere um código novo se ele tiver sido compartilhado fora da turma, e desative o link público quando a inscrição terminar.'},
                {'t': 'IA no curso', 'b': 'O que o estudante pode fazer com a IA. Antes de decidir, leia o artigo "IA para o estudante e o Tutor de IA".'},
                {'t': 'Exportação e arquivamento', 'b': 'Exportar o curso ou arquivá-lo e sair. Antes de arquivar, confira se você não precisa dele para outra turma, e faça uma cópia de segurança se quiser guardá-lo.'},
            ],
        },
    },
}


def apply_article_merges(merged: dict) -> None:
    """Funde los artículos de MERGE_SPECS en su principal y aplica los textos finales (MERGE_TEXT)."""
    for loc in ('es', 'pt-BR'):
        d = merged[loc]
        arts = {a['id']: a for a in d['articles']}
        for keep_id, spec in MERGE_SPECS.items():
            keep = arts.get(keep_id)
            gone = [i for i in spec['absorb'] if i in arts]
            if keep is None or not gone:
                continue
            steps = list(keep.get('steps') or [])
            img = list(keep.get('img') or [])
            step_img = dict(keep.get('stepImg') or {})
            for gid in gone:
                src = arts[gid]
                if spec['steps'] and gid in spec.get('steps_from', gone):
                    base = len(steps)
                    for i, st in enumerate(src.get('steps') or []):
                        steps.append({'t': st['t'], 'b': st['b']})
                        k = (src.get('stepImg') or {}).get(str(i + 1))
                        if k:
                            step_img[str(base + i + 1)] = k
                if spec.get('images', True):
                    for k in src.get('img') or []:
                        if k not in img:
                            img.append(k)
            keep['steps'] = steps
            keep['img'] = img
            keep['stepImg'] = step_img
            d['articles'] = [a for a in d['articles'] if a['id'] not in gone]
            arts = {a['id']: a for a in d['articles']}
            d.setdefault('aliases', {})
            for gid in gone:
                d['aliases'][gid] = keep_id
            for a in d['articles']:
                for field in ('related', 'faqRelated'):
                    if a.get(field):
                        a[field] = [i for i in dict.fromkeys(keep_id if i in gone else i for i in a[field]) if i != a['id']]
            for g in d.get('courseGroups') or []:
                g['ids'] = [i for i in g['ids'] if i not in gone]
        # textos finales
        for keep_id, txt in MERGE_TEXT.get(loc, {}).items():
            art = arts.get(keep_id)
            if art is None:
                continue
            if 'steps' in txt:
                if len(txt['steps']) < len(art.get('steps') or []):
                    raise SystemExit(f"{loc} · {keep_id}: {len(txt['steps'])} pasos de texto y {len(art.get('steps') or [])} en el artículo")
                art['steps'] = [dict(t=s['t'], b=s['b']) for s in txt['steps']]
            for key in ('title', 'answer', 'example', 'tips'):
                if key in txt:
                    art[key] = txt[key]
            if 'related' in txt:
                art['related'] = list(txt['related'])
            if 'stepImg' in txt:
                art['stepImg'] = dict(txt['stepImg'])
            if 'img' in txt:
                art['img'] = list(txt['img'])
            if 'sections' in txt:
                art['sections'] = [dict(x) for x in txt['sections']]
            for k, alt in (txt.get('shots') or {}).items():
                merged[loc].setdefault('shots', {})[k] = f'shots/{k}.jpg'
                merged[loc].setdefault('alt', {})[k] = alt

MERGE_TEXT['es']['crear-curso'] = {
    'example': 'Un departamento de Matemáticas tiene tres grupos de 2.º de ESO. Uno de sus docentes prepara el curso del primer grupo, con sus secciones y materiales, y crea un curso para cada uno de los otros dos grupos con el mismo formato de nombre. Cada grupo entra con su propio código, y el departamento sabe siempre cuál es el curso de cada clase.',
}
MERGE_TEXT['es']['crear-curso'] = {
    'stepImg': {'1': 'es__crear-curso__cursos-lista', '2': 'es__crear-curso__curso-crear-paso1', '3': 'es__crear-curso__curso-crear-paso2', '5': 'es__importar-curso__cursos-lista'},
    'img': ['es__crear-curso__cursos-lista', 'es__crear-curso__curso-crear-paso1', 'es__crear-curso__curso-crear-paso2', 'es__importar-curso__cursos-lista'],
}
MERGE_TEXT['pt-BR']['crear-curso'] = {
    'example': 'Um departamento de Matemática tem três turmas do 8.º ano. Um dos docentes prepara o curso da primeira turma, com as seções e os materiais, e cria um curso para cada uma das outras duas, com o mesmo padrão de nome. Cada turma entra com o seu próprio código, e o departamento sabe sempre qual é o curso de cada turma.',
    'stepImg': {'1': 'pt__crear-curso__pt-cursos-lista', '2': 'pt__crear-curso__pt-curso-crear-paso1', '3': 'pt__crear-curso__pt-curso-crear-paso2', '5': 'pt__importar-curso__pt-cursos-lista'},
    'img': ['pt__crear-curso__pt-cursos-lista', 'pt__crear-curso__pt-curso-crear-paso1', 'pt__crear-curso__pt-curso-crear-paso2', 'pt__importar-curso__pt-cursos-lista'],
    'shots': {
        'pt__crear-curso__pt-cursos-lista': 'Lista de cursos com o botão Criar curso (passo 1) e Importar curso',
        'pt__crear-curso__pt-curso-crear-paso1': 'Formulário Criar curso com o passo 1: dados básicos',
        'pt__crear-curso__pt-curso-crear-paso2': 'Passo 2 de Criar curso: escolher conteúdo, com a aba Vazio',
        'pt__importar-curso__pt-cursos-lista': 'Lista de cursos com o botão Importar curso',
    },
}
MERGE_TEXT['pt-BR']['serie-de-lecciones'] = {
    'stepImg': {'2': 'pt__serie-de-lecciones__pt-serie-lista', '4': 'pt__serie-de-lecciones__pt-serie-completo'},
    'img': ['pt__serie-de-lecciones__pt-serie-lista', 'pt__serie-de-lecciones__pt-serie-completo'],
    'shots': {
        'pt__serie-de-lecciones__pt-serie-lista': 'Biblioteca de séries de lições com os passos 1 e 2: o ícone da Biblioteca e o botão Criar',
        'pt__serie-de-lecciones__pt-serie-completo': 'Formulário Criar série de lições com os passos 1 a 4: título, tema e botão Criar',
    },
}
MERGE_TEXT['es']['serie-de-lecciones'] = {
    'title': 'Crear una serie de lecciones',
    'answer': 'Una serie de lecciones es una secuencia de sesiones sobre un tema, con su progresión y su evaluación. Sirve para planificar un tema completo de una vez, en lugar de preparar cada clase por separado, y para reutilizarla el año siguiente.',
    'example': "Para una serie de 'Introducción al cálculo integral' rellenas Tema, Asignatura 'Matemáticas', Curso '1.º de bachillerato' y, en Descripción, indicas que el alumnado ya conoce las derivadas. Con esos datos la serie sale a su nivel y después la encuentras por asignatura.",
    'tips': ['Describe las sesiones y la evaluación en la Descripción: así la serie sirve para programar.'],
    'steps': [
        {'t': 'Abre Biblioteca → Serie de lecciones', 'b': 'Las series se crean desde la Biblioteca, no desde Cursos. Ahí verás las que ya tienes.'},
        {'t': 'Pulsa Crear', 'b': 'Crear abre el formulario. La serie nace vacía y añades cada lección tú. Si quieres que la IA la genere entera, usa Generar con IA.'},
        {'t': 'Rellena el formulario', 'b': 'Tema es obligatorio. Asignatura, Curso e Idioma ayudan a encontrar la serie y a adaptarla al grupo. En la Descripción indicas las sesiones y la evaluación.'},
        {'t': 'Pulsa Crear', 'b': 'La serie aparece en tu lista. Ábrela cuando quieras revisar o ajustar sus sesiones.'},
    ],
    'sections': [
        {'h': 'Qué significa cada campo', 'b': 'Tema: el tema de la serie, obligatorio. Asignatura y Curso: sirven para encontrarla después por asignatura o curso. Idioma: el idioma en que se genera el contenido. Descripción: cuanto más concreta, mejor encaja la serie con tu grupo.'},
        {'h': 'Ajustar una serie', 'b': 'Cuando la primera versión no encaja (más sesiones de las que das, otro nivel o otra evaluación), pide los cambios en una conversación, de uno en uno, y revisa la progresión antes de guardar la versión final.'},
    ],
    'stepImg': {'2': 'es__serie-de-lecciones__es-serie-lista', '4': 'es__serie-de-lecciones__es-serie-completo'},
    'img': ['es__serie-de-lecciones__es-serie-lista', 'es__serie-de-lecciones__es-serie-completo'],
}
MERGE_TEXT['pt-BR']['serie-de-lecciones'] = {
    'title': 'Criar uma série de aulas',
    'answer': 'Uma série de aulas é uma sequência de sessões sobre um tema, criada na Biblioteca para planejar um conjunto de aulas de uma vez. Serve para planejar o tema inteiro antes de começar, e para reutilizá-la no ano seguinte.',
    'example': "Para uma série de 'Introdução ao cálculo integral', você preenche Tema, Disciplina 'Matemática', Curso '1.º ano do ensino médio' e, na Descrição, escreve que a turma já conhece derivadas. Com esses dados a série sai no nível certo, e depois você a encontra por disciplina.",
    'tips': ['Descreva as sessões e a avaliação na Descrição: assim a série serve para programar.'],
    'steps': [
        {'t': 'Abra Biblioteca → Série de lições', 'b': 'As séries se criam pela Biblioteca, não pelos Cursos. Aí você vê as que já tem.'},
        {'t': 'Clique em Criar', 'b': 'Criar abre o formulário. A série nasce vazia e você acrescenta cada lição. Se quiser que a IA gere tudo, use Gerar com IA.'},
        {'t': 'Preencha o formulário', 'b': 'Tema é obrigatório. Disciplina, Curso e Idioma ajudam a encontrar a série e a adaptá-la à turma. Na Descrição, indique as sessões e a avaliação.'},
        {'t': 'Clique em Criar', 'b': 'A série aparece na sua lista. Abra-a quando quiser revisar ou ajustar as sessões.'},
    ],
    'sections': [
        {'h': 'O que significa cada campo', 'b': 'Tema: o tema da série, obrigatório. Disciplina e Curso: ajudam a encontrá-la depois por disciplina ou curso. Idioma: o idioma em que o conteúdo é gerado. Descrição: quanto mais concreta, melhor a série se encaixa na sua turma.'},
        {'h': 'Ajustar uma série', 'b': 'Quando a primeira versão não encaixa (mais sessões do que você dá, outro nível ou outra avaliação), peça as mudanças em uma conversa, uma de cada vez, e revise a progressão antes de guardar a versão final.'},
    ],
    'stepImg': {'2': 'pt__serie-de-lecciones__pt-serie-lista', '4': 'pt__serie-de-lecciones__pt-serie-completo'},
    'img': ['pt__serie-de-lecciones__pt-serie-lista', 'pt__serie-de-lecciones__pt-serie-completo'],
    'shots': {
        'pt__serie-de-lecciones__pt-serie-lista': 'Biblioteca de séries de lições com os passos 1 e 2: o ícone da Biblioteca e o botão Criar',
        'pt__serie-de-lecciones__pt-serie-completo': 'Formulário Criar série de lições com os passos 1 a 4: título, tema e botão Criar',
    },
}
MERGE_TEXT['pt-BR']['serie-campos'] = {
    'stepImg': {'4': 'pt__serie-campos__pt-serie-formulario-completo'},
    'img': ['pt__serie-campos__pt-serie-formulario-completo'],
    'shots': {
        'pt__serie-campos__pt-serie-formulario-completo': 'Formulário Criar série de lições com o passo 4: botão Criar',
    },
}


# Sección «Organizar el curso»: 6 pasos reales. Los tipos de actividad se explican dentro del paso 5.
# Capturas: el paso 4 muestra la vista de la sección con los pasos 1 a 4; el paso 5, el menú de tipos.
MERGE_TEXT['es']['secciones'] = {
    'title': 'Organizar el curso: secciones, actividades y materiales',
    'answer': 'Una sección es un bloque del curso, como una unidad o un trimestre, y es donde reúnes lo que trabajas con el alumnado: materiales, actividades y entregas. Sirve para que el curso se lea en orden y para que cada tema tenga su sitio. Úsala al montar el curso: crea una sección por tema y, dentro de cada una, añade lo que el alumnado tiene que ver o hacer.',
    'example': 'En un curso de Historia creas una sección por tema: «Revolución industrial», «Imperialismo» y «Primera Guerra Mundial». Dentro de cada una pones el texto explicativo, un enlace a un documental, la ficha para practicar y la entrega del trabajo, y el alumnado sabe en qué bloque está cada cosa.',
    'tips': ['Pon un nombre que describa el bloque: «La célula, unidad de los seres vivos» informa mejor que «Tema 1».'],
    'steps': [
        {'t': 'Localiza las secciones', 'b': 'Cada tarjeta numerada es un bloque del curso. Así ves de un vistazo qué temas tienes creados y cuánto contenido tiene cada uno.'},
        {'t': 'Pulsa Añadir sección', 'b': 'Crea una sección por cada tema nuevo, al final de la lista. Es mejor tener varias cortas que una larga: el alumnado sabe dónde buscar cada cosa.'},
        {'t': 'Gestiona una sección', 'b': 'Desde el menú (…) de cada sección accedes a sus opciones. Revísalas al reorganizar el curso al empezar un trimestre.'},
        {'t': 'Pulsa Añadir actividad o material', 'b': 'Dentro de la sección, este botón abre todo lo que puedes añadir. Úsalo en la sección del tema correspondiente, para que cada actividad quede junto a su contenido.'},
        {'t': 'Elige el tipo', 'b': 'Material: un archivo (PDF, vídeo o cuestionario H5P) para que el alumnado lo consulte antes o después de la clase. Texto: una lectura en su propia página, para explicar un tema con calma. Ficha de trabajo: ejercicios que el alumnado resuelve por su cuenta y que luego repasas en clase. Tarea con comentarios: un trabajo que corriges y al que devuelves comentarios, no solo una nota. Entrega: un archivo que el alumnado sube antes de una fecha límite. Unidad didáctica: un bloque completo, listo para adoptar. Agente de IA: un asistente al que el alumnado pregunta fuera de clase, con tus instrucciones. Enlace: una página web con su título. Nota: un texto breve que se lee sin abrir nada más. Crear con IA: la IA redacta un borrador a partir de tu descripción.'},
        {'t': 'Completa el formulario', 'b': 'Cada tipo tiene su propio formulario. La actividad aparece en la sección cuando pulsas «Añadir»; ponle un título que el alumnado entienda sin contexto.'},
    ],
    'stepImg': {'4': 'es__secciones__es-secciones-numerada', '5': 'es__secciones__es-tipo-menu-numerada'},
    'img': ['es__secciones__es-secciones-numerada', 'es__secciones__es-tipo-menu-numerada'],
    'shots': {
        'es__secciones__es-secciones-numerada': 'Vista de la sección con los pasos 1 a 4: tarjeta de la sección, Añadir sección, menú de la sección y Añadir actividad o material',
        'es__secciones__es-tipo-menu-numerada': 'Menú de tipos de actividad al pulsar Añadir actividad o material',
    },
}
MERGE_TEXT['pt-BR']['secciones'] = {
    'title': 'Organizar o curso: seções, atividades e materiais',
    'answer': 'Uma seção é um bloco do curso, como uma unidade ou um trimestre, e é onde você reúne o que trabalha com o estudante: materiais, atividades e entregas. Serve para o curso ser lido em ordem e para cada tema ter o seu lugar. Use ao montar o curso: crie uma seção por tema e, dentro de cada uma, acrescente o que o estudante precisa ver ou fazer.',
    'example': 'Em um curso de História, você cria uma seção por tema: "Revolução Industrial", "Imperialismo" e "Primeira Guerra Mundial". Dentro de cada uma coloca o texto explicativo, um link para um documentário, a ficha de prática e a entrega do trabalho, e o estudante sabe em que bloco está cada coisa.',
    'tips': ['Dê um nome que descreva o bloco: "A célula, unidade dos seres vivos" informa melhor do que "Tema 1".'],
    'steps': [
        {'t': 'Localize as seções', 'b': 'Cada cartão numerado é um bloco do curso. Você vê de relance quais temas já criou e quanto conteúdo cada um tem.'},
        {'t': 'Clique em Adicionar secção', 'b': 'Crie uma seção para cada tema novo, no fim da lista. Várias seções curtas são melhores do que uma longa: o estudante sabe onde procurar cada coisa.'},
        {'t': 'Gerencie uma seção', 'b': 'Pelo menu (…) de cada seção você acessa as opções dela. Revise-as ao reorganizar o curso no início de um trimestre.'},
        {'t': 'Clique em Adicionar atividade ou material', 'b': 'Dentro da seção, este botão abre tudo o que você pode acrescentar. Use-o na seção do tema correspondente, para que a atividade fique junto do seu conteúdo.'},
        {'t': 'Escolha o tipo', 'b': 'Material: um arquivo (PDF, vídeo ou questionário H5P) para o estudante consultar antes ou depois da aula. Texto: uma leitura em página própria, para explicar um tema com calma. Ficha de trabalho: exercícios que o estudante resolve sozinho e que você revisa depois na aula. Tarefa com feedback: um trabalho que você corrige e ao qual devolve comentários, não só uma nota. Entrega: um arquivo que o estudante envia antes de um prazo. Unidade didática: um bloco completo, pronto para adotar. Agente de IA: um assistente que o estudante consulta fora da aula, com as suas instruções. Ligação: uma página da web com título. Nota: um texto curto que se lê sem abrir mais nada. Criar com IA: a IA escreve um rascunho a partir da sua descrição.'},
        {'t': 'Preencha o formulário', 'b': 'Cada tipo tem o seu formulário. A atividade aparece na seção quando você clica em Adicionar; dê a ela um título que o estudante entenda sem contexto.'},
    ],
    'stepImg': {'4': 'pt__secciones__pt-secciones-numerada', '5': 'pt__secciones__pt-tipo-menu-numerada'},
    'img': ['pt__secciones__pt-secciones-numerada', 'pt__secciones__pt-tipo-menu-numerada'],
    'shots': {
        'pt__secciones__pt-secciones-numerada': 'Vista da seção com os passos 1 a 4: cartão da seção, Adicionar secção, menu da seção e Adicionar atividade ou material',
        'pt__secciones__pt-tipo-menu-numerada': 'Menu de tipos de atividade ao clicar em Adicionar atividade ou material',
    },
}


# --- Grupos de la categoría Cursos (orden: crear, organizar, materiales, participantes, configuración) ---
COURSE_GROUPS = {
    'es': [
        ('Crear el curso', ['crear-curso', 'que-es-un-curso-ayuda']),
        ('Organizar el contenido', ['secciones', 'visibilidad-entradas', 'contenidos-compartidos']),
        ('Materiales y entregas', ['agregar-material-archivo', 'texto-material', 'enlace-y-nota', 'entrega', 'tarea-con-comentarios', 'agente-de-ia']),
        ('Participantes y citas', ['invitar-alumnado', 'participantes-permisos', 'unirse-curso', 'participantes-citas']),
        ('Configuración', ['configuracion-del-curso']),
    ],
    'pt-BR': [
        ('Criar o curso', ['crear-curso', 'que-es-un-curso-ayuda']),
        ('Organizar o conteúdo', ['secciones', 'visibilidad-entradas', 'contenidos-compartidos']),
        ('Materiais e entregas', ['agregar-material-archivo', 'texto-material', 'enlace-y-nota', 'entrega', 'tarea-con-comentarios', 'agente-de-ia']),
        ('Participantes e compromissos', ['invitar-alumnado', 'participantes-permisos', 'unirse-curso', 'participantes-citas']),
        ('Configuração', ['configuracion-del-curso']),
    ],
}


def apply_course_groups(merged: dict) -> None:
    for loc, groups in COURSE_GROUPS.items():
        d = merged[loc]
        ids = {a['id'] for a in d['articles']}
        out = []
        for name, items in groups:
            present = [i for i in items if i in ids]
            if present:
                out.append({'name': name, 'ids': present})
        d['courseGroups'] = out


# Viñetas en los pasos (línea de cabecera + líneas que empiezan por "• ")
MERGE_TEXT['es']['secciones']['steps'][4]['b'] = (
    'Cada tipo sirve para algo distinto:\n'
    '• Material: un archivo (PDF, vídeo o cuestionario H5P) que el alumnado consulta antes o después de la clase.\n'
    '• Texto: una lectura en su propia página, para explicar un tema con calma.\n'
    '• Ficha de trabajo: ejercicios que el alumnado resuelve por su cuenta y que repasas luego en clase.\n'
    '• Tarea con comentarios: un trabajo que corriges y al que devuelves comentarios, no solo una nota.\n'
    '• Entrega: un archivo que el alumnado sube antes de una fecha límite.\n'
    '• Unidad didáctica: un bloque completo, listo para adoptar.\n'
    '• Agente de IA: un asistente para el alumnado fuera de clase, con tus instrucciones.\n'
    '• Enlace: una página web con su título.\n'
    '• Nota: un texto breve que se lee sin abrir nada más.\n'
    '• Crear con IA: la IA redacta un borrador a partir de tu descripción.')
MERGE_TEXT['pt-BR']['secciones']['steps'][4]['b'] = (
    'Cada tipo serve para uma coisa diferente:\n'
    '• Material: um arquivo (PDF, vídeo ou questionário H5P) que o estudante consulta antes ou depois da aula.\n'
    '• Texto: uma leitura em página própria, para explicar um tema com calma.\n'
    '• Ficha de trabalho: exercícios que o estudante resolve sozinho e que você revisa depois na aula.\n'
    '• Tarefa com feedback: um trabalho que você corrige e ao qual devolve comentários, não só uma nota.\n'
    '• Entrega: um arquivo que o estudante envia antes de um prazo.\n'
    '• Unidade didática: um bloco completo, pronto para adotar.\n'
    '• Agente de IA: um assistente para o estudante fora da aula, com as suas instruções.\n'
    '• Ligação: uma página da web com título.\n'
    '• Nota: um texto curto que se lê sem abrir mais nada.\n'
    '• Criar com IA: a IA escreve um rascunho a partir da sua descrição.')

# Configuración del curso: IA y exportación explicados aquí, con viñetas (6 pasos, mismas capturas).
MERGE_TEXT['es']['configuracion-del-curso'].update({
    'title': 'Configuración del curso',
    'answer': 'La pestaña Configuración reúne todos los ajustes del curso: los datos, la portada, cómo se ve el curso, el código de inscripción, la IA para el alumnado y la exportación o el archivado. Sirve para dejar el curso listo para tu grupo y revisarlo al empezar cada trimestre o al cerrar el curso.',
    'example': 'Al empezar el trimestre cambias la visualización a Lista con vista previa, para que el alumnado vea de un vistazo de qué trata cada material. Al terminar el curso lo exportas como copia de seguridad y lo archivas.',
    'steps': [
        {'t': 'General', 'b': 'Nombre, Asignatura, Clase o curso escolar y Descripción. Son los datos que identifican el curso en tu lista y en la del centro.\n• Pulsa «Aplicar cambios» para guardarlos.\n• Mantén el mismo formato de nombre en todo el departamento.'},
        {'t': 'Portada', 'b': 'La imagen que se ve en el curso, en la lista de cursos y en la página de inscripción.\n• Una portada reconocible ayuda a encontrar el curso correcto entre varios.'},
        {'t': 'Visualización', 'b': 'Cómo ve el alumnado las secciones y los contenidos.\n• Lista: la más compacta, útil con muchos contenidos.\n• Lista con vista previa: muestra las primeras líneas de cada contenido. Suele ser la más clara.\n• Mosaicos: cada sección se muestra como tarjetas, bien para materiales visuales.\n• Secciones como mosaicos: cada sección tiene su propia página.\n• «Contenido anterior y siguiente»: enlaza cada contenido con el anterior y el siguiente.'},
        {'t': 'Código de inscripción', 'b': 'El código, el enlace público y «Generar nuevo código».\n• El enlace público viene desactivado por defecto.\n• Genera un código nuevo si se ha compartido fuera de la clase.\n• Desactiva el enlace público cuando termine la inscripción.'},
        {'t': 'IA para el alumnado', 'b': 'Decide si el alumnado puede usar la IA del curso y cómo responde.\n• «IA para el alumnado»: enciende o apaga la IA. Apágala en semanas de examen.\n• Tutor de IA (por defecto): da pistas y hace preguntas, sin soluciones completas.\n• Solo contenidos del curso: responde solo con el material del curso. Libre: también responde fuera del curso.\n• Generar imágenes y Búsqueda web vienen desactivadas; Adjuntar archivos, activada.\n• «Mensajes por estudiante y día»: 50 por defecto.\n• IA para invitados: se aplica a quien entró con el enlace público. Viene desactivada.\n• Pausar la IA: al final de la página, para cortarla de forma temporal, por ejemplo en un examen.'},
        {'t': 'Exportación y archivado', 'b': 'Lo último del curso: exportar o archivar.\n• Exportar: copia completa en ZIP, IMS Common Cartridge o copia de seguridad de Moodle (.mbz).\n• Archivar: el curso sale de tu lista. Antes, revisa que no lo necesitas para otro grupo.\n• «Eliminar curso» no aparece en los pasos normales: no tiene vuelta atrás.'},
    ],
})
MERGE_TEXT['pt-BR']['configuracion-del-curso'].update({
    'title': 'Configurações do curso',
    'answer': 'A aba Definições reúne todos os ajustes do curso: os dados, a capa, como o curso aparece, o código de inscrição, a IA para o estudante e a exportação ou o arquivamento. Serve para deixar o curso pronto para a sua turma e revisá-lo no início de cada trimestre ou ao encerrar o curso.',
    'example': 'No início do trimestre você muda a visualização para Lista com visualização prévia, para o estudante ver de relance do que trata cada material. Ao terminar o curso, você o exporta como cópia de segurança e o arquiva.',
    'steps': [
        {'t': 'Geral', 'b': 'Nome, Disciplina, Turma ou série e Descrição. São os dados que identificam o curso na sua lista e na da escola.\n• Clique em "Aplicar alterações" para salvá-los.\n• Mantenha o mesmo formato de nome em todo o departamento.'},
        {'t': 'Capa', 'b': 'A imagem que aparece no curso, na lista de cursos e na página de inscrição.\n• Uma capa reconhecível ajuda a achar o curso certo entre vários.'},
        {'t': 'Visualização', 'b': 'Como o estudante vê as seções e os conteúdos.\n• Lista: a mais compacta, útil com muitos conteúdos.\n• Lista com visualização prévia: mostra as primeiras linhas de cada conteúdo. Costuma ser a mais clara.\n• Mosaicos: cada seção aparece como cartões, bom para materiais visuais.\n• Seções como mosaicos: cada seção tem a sua própria página.\n• "Conteúdo anterior e seguinte": liga cada conteúdo ao anterior e ao seguinte.'},
        {'t': 'Código de inscrição', 'b': 'O código, o link público e "Gerar novo código".\n• O link público vem desativado por padrão.\n• Gere um código novo se ele tiver sido compartilhado fora da turma.\n• Desative o link público quando a inscrição terminar.'},
        {'t': 'IA para o estudante', 'b': 'Decide se o estudante pode usar a IA do curso e como ela responde.\n• "IA para o estudante": liga ou desliga a IA. Desligue-a em semanas de prova.\n• Tutor de IA (padrão): dá pistas e faz perguntas, sem soluções completas.\n• Somente conteúdos do curso: responde só com o material do curso. Livre: responde também fora do curso.\n• Gerar imagens e Busca na web vêm desativadas; Anexar arquivos, ativada.\n• "Mensagens por estudante e dia": 50 por padrão.\n• IA para convidados: vale para quem entrou pelo link público. Vem desativada.\n• Pausar a IA: no fim da página, para cortá-la temporariamente, por exemplo durante uma prova.'},
        {'t': 'Exportação e arquivamento', 'b': 'O último passo do curso: exportar ou arquivar.\n• Exportar: cópia completa em ZIP, IMS Common Cartridge ou cópia de segurança do Moodle (.mbz).\n• Arquivar: o curso sai da sua lista. Antes, confira se você não precisa dele para outra turma.\n• "Excluir curso" não aparece nos passos normais: não tem volta.'},
    ],
})


# Artículos relacionados de Organizar el curso: los de actividades y materiales.
_REL_SECCIONES = ['agregar-material-archivo', 'texto-material', 'enlace-y-nota', 'entrega', 'tarea-con-comentarios', 'agente-de-ia']
MERGE_TEXT['es']['secciones']['related'] = list(_REL_SECCIONES)
MERGE_TEXT['pt-BR']['secciones']['related'] = list(_REL_SECCIONES)


# Limpieza de categorías: "Cuenta y configuración" se elimina (no aporta). "Para centros" se elimina salvo
# seguridad y privacidad, que pasa a preguntas frecuentes.
DROP_CATEGORIES = ['configuracion', 'it']
MOVE_TO_FAQ = ['seguridad-datos']


def apply_category_cleanup(merged: dict) -> None:
    for loc in ('es', 'pt-BR'):
        d = merged[loc]
        gone = {a['id'] for a in d['articles'] if a['cat'] in DROP_CATEGORIES and a['id'] not in MOVE_TO_FAQ}
        for a in d['articles']:
            if a['id'] in MOVE_TO_FAQ:
                a['cat'] = 'faq'
        d['articles'] = [a for a in d['articles'] if a['id'] not in gone]
        d['categories'] = [c for c in d['categories'] if c['id'] not in DROP_CATEGORIES]
        for a in d['articles']:
            for field in ('related', 'faqRelated'):
                if a.get(field):
                    a[field] = [i for i in a[field] if i not in gone]
            if a.get('id') and a.get('related') is not None:
                pass
        for field in ('popular',):
            pass
        ui = d.get('ui') or {}
        if ui.get('popular'):
            ui['popular'] = [i for i in ui['popular'] if i not in gone]
        for g in d.get('courseGroups') or []:
            g['ids'] = [i for i in g['ids'] if i not in gone]


# Configuración del curso: una captura por sección, con el número de su entrada del menú lateral.
# Los títulos de los pasos son los nombres que aparecen en la plataforma.
_CFG_PT_KEYS = [f'pt__configuracion-del-curso__pt-cfg-{n}-numerada' for n in range(1, 7)]
_CFG_PT_TITLES = ['Geral', 'Capa', 'Apresentação', 'Código de adesão', 'IA no curso', 'Exportação']
for _i, _t in enumerate(_CFG_PT_TITLES):
    MERGE_TEXT['pt-BR']['configuracion-del-curso']['steps'][_i]['t'] = _t
MERGE_TEXT['pt-BR']['configuracion-del-curso']['stepImg'] = {str(_i + 1): k for _i, k in enumerate(_CFG_PT_KEYS)}
MERGE_TEXT['pt-BR']['configuracion-del-curso']['img'] = list(_CFG_PT_KEYS)
MERGE_TEXT['pt-BR']['configuracion-del-curso']['shots'] = {
    k: f'Configurações do curso, passo {_i + 1}: {_CFG_PT_TITLES[_i]}' for _i, k in enumerate(_CFG_PT_KEYS)}


# Configuración del curso (español): una captura por sección, numerada con su entrada del menú lateral.
_CFG_ES_KEYS = [f'es__configuracion-del-curso__es-cfg-{n}-numerada' for n in range(1, 7)]
_CFG_ES_TITLES = ['General', 'Portada', 'Visualización', 'Código de inscripción', 'IA en el curso', 'Exportación']
for _i, _t in enumerate(_CFG_ES_TITLES):
    MERGE_TEXT['es']['configuracion-del-curso']['steps'][_i]['t'] = _t
MERGE_TEXT['es']['configuracion-del-curso']['stepImg'] = {str(_i + 1): k for _i, k in enumerate(_CFG_ES_KEYS)}
MERGE_TEXT['es']['configuracion-del-curso']['img'] = list(_CFG_ES_KEYS)
MERGE_TEXT['es']['configuracion-del-curso']['shots'] = {
    k: f'Configuración del curso, paso {_i + 1}: {_CFG_ES_TITLES[_i]}' for _i, k in enumerate(_CFG_ES_KEYS)}


# Citas (español): capturas nuevas con datos en español (sin citas en portugués).
_CITAS_ES_A = 'es__participantes-citas__es-citas-pestana-numerada'
_CITAS_ES_B = 'es__participantes-citas__es-citas-formulario-numerada'
MERGE_TEXT['es']['participantes-citas'] = {
    'stepImg': {'2': _CITAS_ES_A, '4': _CITAS_ES_B},
    'img': [_CITAS_ES_A, _CITAS_ES_B],
    'shots': {
        _CITAS_ES_A: 'Pestaña Citas con los pasos 1 y 2: la pestaña y el botón Crear cita',
        _CITAS_ES_B: 'Formulario de cita con los pasos 3 y 4: los datos y el botón Guardar',
    },
}


def apply_link_fix(merged: dict) -> None:
    """Relacionados y FAQ relacionadas apuntan a artículos existentes (redirigiendo los fusionados)."""
    for loc in ('es', 'pt-BR'):
        d = merged[loc]
        ids = {a['id'] for a in d['articles']}
        al = d.get('aliases') or {}
        for a in d['articles']:
            for field in ('related', 'faqRelated'):
                if not a.get(field):
                    continue
                fixed = []
                for r in a[field]:
                    r2 = al.get(r, r)
                    if r2 in ids and r2 != a['id'] and r2 not in fixed:
                        fixed.append(r2)
                a[field] = fixed


# Capturas en portugués equivalentes a las españolas (misma pantalla y mismo paso numerado).
def _pt_shots(article, mapping, alts):
    MERGE_TEXT['pt-BR'].setdefault(article, {})
    MERGE_TEXT['pt-BR'][article]['img'] = list(mapping.values())
    MERGE_TEXT['pt-BR'][article]['stepImg'] = {str(k): v for k, v in mapping.items()}
    MERGE_TEXT['pt-BR'][article]['shots'] = {v: alts[v] for v in mapping.values()}

_pt_shots('buscar-contenido', {1: 'pt__buscar-contenido__pt-biblioteca'},
          {'pt__buscar-contenido__pt-biblioteca': 'Biblioteca com a pesquisa de todo o conteúdo no passo 1'})
_pt_shots('beta', {1: 'pt__beta__pt-menu-cuenta'},
          {'pt__beta__pt-menu-cuenta': 'Menu da conta com o item O que há de novo no passo 1'})
_pt_shots('idioma-no-cambia', {1: 'pt__idioma-no-cambia__pt-menu-idioma'},
          {'pt__idioma-no-cambia__pt-menu-idioma': 'Menu da conta com a opção Idioma e a lista de idiomas'})
_pt_shots('unirse-curso', {1: 'pt__unirse-curso__pt-unirse-dialogo'},
          {'pt__unirse-curso__pt-unirse-dialogo': 'Diálogo Aderir a um curso com o campo do código de adesão no passo 1'})
_pt_shots('subir-documento', {1: 'pt__subir-documento__pt-biblioteca-inicio', 2: 'pt__subir-documento__pt-biblioteca-documentos'},
          {'pt__subir-documento__pt-biblioteca-inicio': 'Biblioteca com o cartão Carregar documento no passo 1',
           'pt__subir-documento__pt-biblioteca-documentos': 'Minha biblioteca com o botão Conteúdo e a pesquisa de documentos nos passos 1 e 2'})

_pt_shots('tarea-correccion-biblioteca', {1: 'pt__tarea-correccion-biblioteca__pt-tarea-lista', 5: 'pt__tarea-correccion-biblioteca__pt-tarea-formulario'},
          {'pt__tarea-correccion-biblioteca__pt-tarea-lista': 'Lista de Tarefas de correção e feedback com o botão Criar no passo 1',
           'pt__tarea-correccion-biblioteca__pt-tarea-formulario': 'Formulário Criar tarefa de feedback com título, descrição, solução modelo e botão Criar'})
MERGE_TEXT['pt-BR'].setdefault('tarea-calibrar', {})
MERGE_TEXT['pt-BR']['tarea-calibrar']['img'] = ['pt-tarea-lista']
MERGE_TEXT['pt-BR']['tarea-calibrar']['shots'] = {'pt-tarea-lista': 'Lista de Tarefas de correção e feedback com as tarefas criadas'}

# Conversas e ferramentas: capturas em portugués equivalentes às espanholas
MERGE_TEXT['pt-BR'].setdefault('hacer-pregunta', {})
MERGE_TEXT['pt-BR']['hacer-pregunta']['img'] = ['pt__hacer-pregunta__pt-conversa-inicio', 'pt-conversa-respuesta']
MERGE_TEXT['pt-BR']['hacer-pregunta']['stepImg'] = {'3': 'pt__hacer-pregunta__pt-conversa-inicio'}
MERGE_TEXT['pt-BR']['hacer-pregunta']['shots'] = {'pt__hacer-pregunta__pt-conversa-inicio': 'Tela inicial do chat com o campo de pergunta, o botão de ferramentas e o botão de enviar', 'pt-conversa-respuesta': 'Resposta do assistente na conversa'}
MERGE_TEXT['pt-BR'].setdefault('conversacion-contexto', {})
MERGE_TEXT['pt-BR']['conversacion-contexto']['img'] = ['pt-conversaciones']
MERGE_TEXT['pt-BR']['conversacion-contexto']['stepImg'] = {}
MERGE_TEXT['pt-BR']['conversacion-contexto']['shots'] = {'pt-conversaciones': 'Lista de conversas com a conversa criada'}
MERGE_TEXT['pt-BR'].setdefault('respuesta-no-correcta', {})
MERGE_TEXT['pt-BR']['respuesta-no-correcta']['img'] = ['pt-conversaciones']
MERGE_TEXT['pt-BR']['respuesta-no-correcta']['stepImg'] = {}
MERGE_TEXT['pt-BR']['respuesta-no-correcta']['shots'] = {'pt-conversaciones': 'Lista de conversas com a conversa criada'}
MERGE_TEXT['pt-BR'].setdefault('conversacion-modos', {})
MERGE_TEXT['pt-BR']['conversacion-modos']['img'] = ['pt__conversacion-modos__pt-modos']
MERGE_TEXT['pt-BR']['conversacion-modos']['stepImg'] = {'2': 'pt__conversacion-modos__pt-modos'}
MERGE_TEXT['pt-BR']['conversacion-modos']['shots'] = {'pt__conversacion-modos__pt-modos': 'Lista de modos de conversa com Dinâmico, Padrão e as ferramentas'}
MERGE_TEXT['pt-BR'].setdefault('herramientas-asistente', {})
MERGE_TEXT['pt-BR']['herramientas-asistente']['img'] = ['pt__herramientas-asistente__pt-herramientas', 'pt__herramientas-asistente__pt-modos']
MERGE_TEXT['pt-BR']['herramientas-asistente']['stepImg'] = {'4': 'pt__herramientas-asistente__pt-herramientas', '3': 'pt__herramientas-asistente__pt-modos'}
MERGE_TEXT['pt-BR']['herramientas-asistente']['shots'] = {'pt__herramientas-asistente__pt-herramientas': 'Menu de ferramentas do assistente com Gerir biblioteca e Criar H5P', 'pt__herramientas-asistente__pt-modos': 'Modos de conversa com o seletor de ferramentas e o botão de ferramentas'}
_CHAT_PT_OK = True

# Citas: misma pareja de capturas que en español (sin la de cita guardada)
MERGE_TEXT['pt-BR'].setdefault('participantes-citas', {})
MERGE_TEXT['pt-BR']['participantes-citas']['img'] = ['pt__participantes-citas__pt-cita-pestana', 'pt__participantes-citas__pt-cita-formulario']
MERGE_TEXT['pt-BR']['participantes-citas']['stepImg'] = {'2': 'pt__participantes-citas__pt-cita-pestana', '4': 'pt__participantes-citas__pt-cita-formulario'}
MERGE_TEXT['pt-BR']['participantes-citas']['shots'] = {
    'pt__participantes-citas__pt-cita-pestana': 'Separador Citas do curso com o botão Criar cita no passo 2',
    'pt__participantes-citas__pt-cita-formulario': 'Formulário Criar cita com os campos e o botão Guardar no passo 4'}
# Qué es: pantalla de inicio con la barra lateral numerada (paso 7 en la versión española)
MERGE_TEXT['pt-BR'].setdefault('que-es', {})
MERGE_TEXT['pt-BR']['que-es']['img'] = ['pt__que-es__pt-inicio']
MERGE_TEXT['pt-BR']['que-es']['stepImg'] = {'7': 'pt__que-es__pt-inicio'}
MERGE_TEXT['pt-BR']['que-es']['shots'] = {'pt__que-es__pt-inicio': 'Início do assistente com a barra lateral: conversas, cursos, biblioteca, administração e o perfil no passo 7'}

# Paridad final de capturas (mismo número en español y portugués)
# Crear asistente: el estado guardado en portugués (sin nombres en español)
_pt_ca = MERGE_TEXT['pt-BR'].setdefault('crear-asistente', {})
_pt_ca['img'] = ['pt__crear-asistente__pt-asistente-formulario', 'pt-asistente-guardado']
_pt_ca['stepImg'] = {'4': 'pt__crear-asistente__pt-asistente-formulario', '5': 'pt-asistente-guardado'}
_pt_ca.setdefault('shots', {})['pt-asistente-guardado'] = 'Lista de modelos com o assistente guardado, com o nome, a descrição e os botões de ação'
# Ficha interactiva: la pantalla de fuentes en portugués
_pt_fi = MERGE_TEXT['pt-BR'].setdefault('ficha-interactiva', {})
_pt_fi['img'] = ['pt__ficha-interactiva__pt-ficha-paso1', 'pt-ficha-paso2-fuentes']
_pt_fi['stepImg'] = {'4': 'pt__ficha-interactiva__pt-ficha-paso1', '2': 'pt-ficha-paso2-fuentes'}
_pt_fi.setdefault('shots', {})['pt-ficha-paso2-fuentes'] = 'Segundo passo de Criar ficha de trabalho, com a área para escolher documentos fonte da biblioteca'
# Tarea con comentarios: el español se queda con la vista general, igual que el portugués
MERGE_TEXT['es'].setdefault('tarea-con-comentarios', {})
MERGE_TEXT['es']['tarea-con-comentarios']['img'] = ['bio-vista-general-con-tarea']
MERGE_TEXT['es']['tarea-con-comentarios']['stepImg'] = {}
# Plantillas: la lista de modelos en portugués (recorte sin el modelo en español)
_pt_pn = MERGE_TEXT['pt-BR'].setdefault('plantilla-nombrar', {})
_pt_pn['img'] = ['pt-plantillas-asistentes-recorte']
_pt_pn.setdefault('shots', {})['pt-plantillas-asistentes-recorte'] = 'Lista de modelos com dois assistentes de laboratório, cada um com o nome, a descrição e a etiqueta Criar H5P'
MERGE_TEXT['es'].setdefault('plantillas-vs-asistentes', {})
MERGE_TEXT['es']['plantillas-vs-asistentes']['img'] = ['es__plantillas-vs-asistentes__plantillas-asistentes']
MERGE_TEXT['es']['plantillas-vs-asistentes']['stepImg'] = {'2': 'es__plantillas-vs-asistentes__plantillas-asistentes'}
_pt_pv = MERGE_TEXT['pt-BR'].setdefault('plantillas-vs-asistentes', {})
_pt_pv['img'] = ['pt-plantillas-asistentes-recorte']
_pt_pv['stepImg'] = {'2': 'pt-plantillas-asistentes-recorte'}
_pt_pv.setdefault('shots', {})['pt-plantillas-asistentes-recorte'] = 'Lista de modelos, con los assistentes de prática de laboratório'


# Más capturas, misma cantidad en ambos idiomas (revisión final)
# Tarea con comentarios: selector de la biblioteca (paso 3) y tarea elegida (paso 4), más la vista general
PT_TAREA_STEPS = [{'t': 'Adicionar atividade ou material', 'b': 'Confirme em qual seção você está antes de continuar, porque é nela que a tarefa vai aparecer.'}, {'t': 'Escolher Tarefa com feedback', 'b': 'Selecione esse tipo para indicar que a atividade será devolvida com feedback. O título da janela mostra a seção de destino, e vale conferi-lo antes de seguir.'}, {'t': 'Escolher da biblioteca', 'b': 'Aqui aparecem as tarefas que você já criou na Biblioteca. Se aparecer "Sua biblioteca ainda não tem nada desse tipo", crie primeiro a tarefa de correção.'}, {'t': 'Selecionar e adicionar', 'b': 'A tarefa entra na seção com o seu tipo, e o curso fica com a cópia. Se você ajustar a tarefa na Biblioteca depois, lembre-se de que a mudança não chega ao curso sozinha.'}]
MERGE_TEXT['pt-BR'].setdefault('tarea-con-comentarios', {})
MERGE_TEXT['pt-BR']['tarea-con-comentarios']['steps'] = PT_TAREA_STEPS
MERGE_TEXT['pt-BR']['tarea-con-comentarios']['img'] = ['pt-tarea-elegir-biblioteca', 'pt-tarea-elegida', 'pt-bio-vista-general-con-tarea']
MERGE_TEXT['pt-BR']['tarea-con-comentarios']['stepImg'] = {'3': 'pt-tarea-elegir-biblioteca', '4': 'pt-tarea-elegida'}
MERGE_TEXT['pt-BR']['tarea-con-comentarios']['shots'] = {
    'pt-tarea-elegir-biblioteca': 'Janela Adicionar a «Geral» com a lista Escolher da biblioteca e as tarefas criadas',
    'pt-tarea-elegida': 'Mesma janela com a tarefa escolhida marcada e o botão Adicionar',
    'pt-bio-vista-general-con-tarea': 'Visão geral do curso com a tarefa com feedback na seção',
}
MERGE_TEXT['es']['tarea-con-comentarios']['img'] = ['es__tarea-con-comentarios__tarea-elegir-biblioteca', 'es__tarea-con-comentarios__tarea-elegida', 'bio-vista-general-con-tarea']
MERGE_TEXT['es']['tarea-con-comentarios']['stepImg'] = {'3': 'es__tarea-con-comentarios__tarea-elegir-biblioteca', '4': 'es__tarea-con-comentarios__tarea-elegida'}
# Citas: pestaña, formulario y cita guardada en ambos idiomas
_CITAS_ES_GUARDADA = 'es__participantes-citas__es-cita-guardada'
MERGE_TEXT['es']['participantes-citas']['img'] = [_CITAS_ES_A, _CITAS_ES_B, _CITAS_ES_GUARDADA]
MERGE_TEXT['es']['participantes-citas']['shots'][_CITAS_ES_GUARDADA] = 'La cita guardada aparece en la lista de próximos'
MERGE_TEXT['pt-BR'].setdefault('participantes-citas', {})
MERGE_TEXT['pt-BR']['participantes-citas']['img'] = ['pt__participantes-citas__pt-cita-pestana', 'pt__participantes-citas__pt-cita-formulario', 'pt__participantes-citas__pt-cita-guardada']
MERGE_TEXT['pt-BR']['participantes-citas']['stepImg'] = {'2': 'pt__participantes-citas__pt-cita-pestana', '4': 'pt__participantes-citas__pt-cita-formulario'}
MERGE_TEXT['pt-BR']['participantes-citas']['shots'] = {
    'pt__participantes-citas__pt-cita-pestana': 'Separador Citas do curso com o botão Criar cita no passo 2',
    'pt__participantes-citas__pt-cita-formulario': 'Formulário Criar cita com os campos e o botão Guardar no passo 4',
    'pt__participantes-citas__pt-cita-guardada': 'A cita guardada aparece na lista de próximos',
}
# Plantillas vs asistentes: la biblioteca de plantillas en español; en portugués, el formulario de creación del asistente
MERGE_TEXT['es']['plantillas-vs-asistentes']['img'] = ['es__plantillas-vs-asistentes__plantillas-asistentes', 'es__plantillas-vs-asistentes__plantillas-curso']
MERGE_TEXT['es']['plantillas-vs-asistentes']['stepImg'] = {'1': 'es__plantillas-vs-asistentes__plantillas-curso', '2': 'es__plantillas-vs-asistentes__plantillas-asistentes'}
MERGE_TEXT['pt-BR']['plantillas-vs-asistentes']['img'] = ['pt-plantillas-asistentes-recorte', 'pt__crear-asistente__pt-asistente-formulario']
MERGE_TEXT['pt-BR']['plantillas-vs-asistentes']['stepImg'] = {'2': 'pt-plantillas-asistentes-recorte'}
MERGE_TEXT['pt-BR']['plantillas-vs-asistentes']['shots'] = {
    'pt-plantillas-asistentes-recorte': 'Lista de modelos com dois assistentes de práticas de laboratório',
    'pt__crear-asistente__pt-asistente-formulario': 'Formulário Criar modelo: nome, ferramentas e instrução',
}
