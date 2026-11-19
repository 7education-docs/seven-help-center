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
        answer="Un curso es el espacio donde reúnes todo lo que trabajas con un grupo de alumnos: las secciones con los temas, los materiales, las actividades, las citas y el código para que el alumnado entre. Sirve para tener cada asignatura organizada en un único lugar, en lugar de repartirla entre carpetas, correos y chats. Puedes empezar un curso desde cero con el asistente, importar uno que ya tienes o adoptar una plantilla; los pasos recogen las tres formas.",
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
        answer="Um curso é o espaço onde você reúne tudo o que trabalha com um grupo de estudantes: as seções com os temas, os materiais, as atividades, os compromissos e o código para que os estudantes entrem. Serve para ter cada disciplina organizada em um só lugar, em vez de espalhá-la entre pastas, e-mails e conversas. Você pode começar um curso do zero com o assistente, importar um que já tem ou adotar um modelo; os passos reúnem as três formas.",
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
