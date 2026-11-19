# -*- coding: utf-8 -*-
REWRITES = {
    'que-es': {
        'answer': 'O Seven Assistant é um assistente de IA para o trabalho docente: você o usa para planejar aulas, criar materiais e redigir ou revisar trabalhos. Ele faz propostas, e a decisão sobre o que chega aos estudantes e às famílias é sempre sua. Este artigo apresenta as principais áreas da barra lateral, para você saber onde encontrar cada coisa desde o primeiro dia.',
        'steps': [
            {'t': 'O que você pode fazer', 'b': 'Conversar com o assistente, montar cursos com seções e atividades, guardar materiais na Biblioteca, criar séries de aulas, fichas interativas e tarefas de correção. Cada uma dessas funções tem um artigo próprio nesta ajuda.'},
            {'t': 'O que ele não faz', 'b': 'O assistente não substitui o seu critério profissional. Revise sempre o que ele propõe antes de compartilhar com estudantes ou famílias.'},
            {'t': 'Conversas', 'b': 'É a página inicial e o lugar para fazer perguntas ao assistente. Comece por aqui quando precisar de uma resposta rápida ou de um primeiro rascunho.'},
            {'t': 'Cursos', 'b': 'Aqui você cria cursos, entra em um curso que já existe ou o importa. É também por essa área que os estudantes entram no curso da turma.'},
            {'t': 'Biblioteca', 'b': 'Guarde aqui os documentos, séries de aulas, fichas interativas e tarefas de correção que você quer reaproveitar em outras aulas e turmas.'},
            {'t': 'Modelos', 'b': 'Reúne os seus assistentes de IA, cada um com instruções próprias, para tarefas que se repetem. Vale criar um quando você perceber que faz o mesmo tipo de pedido várias vezes.'},
            {'t': 'Menu da conta', 'b': 'Fica no avatar, embaixo à esquerda. Dali você acessa Configurações, troca o idioma e gerencia as pastas compartilhadas, e é também a opção para sair em um computador que não é seu.'},
        ],
        'tips': ['Comece por uma necessidade concreta: uma aula da próxima semana, uma rubrica ou uma avaliação.'],
        'example': 'Uma professora de Biologia tem prova na próxima semana. Ela começa em Conversas, pede um roteiro de revisão para o 9.º ano, ajusta o texto e guarda o resultado na Biblioteca. Depois o disponibiliza no curso da turma, em Cursos, sem precisar procurar o arquivo em outra pasta.',
    },
    'que-es-un-curso-ayuda': {
        'answer': 'A visão geral é a tela principal de cada curso: é ali que você convida os estudantes, confere a próxima aula e vê o conteúdo organizado em seções. Use-a como ponto de partida sempre que abrir o curso, porque ela mostra de relance o que os estudantes veem. Conhecer a visão geral evita surpresas na hora de compartilhar o código e de começar a aula.',
        'steps': [
            {'t': 'Convidar alunos', 'b': 'O código de inscrição aparece aqui, com botão para copiá-lo, para você passá-lo à turma sem procurá-lo em outro lugar. O link "Ir para os participantes" leva à lista de quem já entrou.'},
            {'t': 'Próximo encontro', 'b': 'Mostra a próxima sessão marcada no curso, para você lembrar o que vem em seguida. Se não houver nenhuma, aparece "Nenhum encontro previsto" e você pode marcá-la em Compromissos.'},
            {'t': 'Seções', 'b': 'O conteúdo do curso se organiza em blocos. Cada seção informa a quantidade de entradas, e o menu (…) reúne as opções dela, enquanto os materiais e atividades ficam dentro.'},
            {'t': 'Entradas ocultas', 'b': 'Uma entrada marcada como "Oculto" não aparece para os estudantes. Use essa marcação para montar o conteúdo com antecedência e publicá-lo no dia certo.'},
            {'t': 'Abas do curso', 'b': 'Visão geral, Compromissos, Conteúdos compartilhados, Participantes e Definições ficam no topo. "Ver como aluno" aparece no alto à direita e mostra o curso como o estudante o vê.'},
        ],
        'tips': ['Revise a visão geral antes de cada aula: é o jeito mais rápido de conferir o que os estudantes veem.'],
        'example': 'Uma professora de Matemática abre o curso na segunda-feira. Na visão geral, percebe que a próxima aula é na quarta, que duas seções ainda têm entradas ocultas e que o código de inscrição está pronto para a turma. Ela ajusta o que falta, e a aula de quarta começa com tudo no lugar.',
    },
    'secciones': {
        'answer': 'Uma seção agrupa o conteúdo de um curso em um bloco, como uma unidade didática, um trimestre ou um tema. Ela ajuda o estudante a encontrar cada assunto no lugar certo e permite reorganizar o curso por blocos sem misturar materiais. Crie seções quando quiser que o curso siga a sequência do seu planejamento, com cada bloco em ordem.',
        'steps': [
            {'t': 'Localizar as seções', 'b': 'Antes de mexer em qualquer coisa, veja a ordem atual do curso. Assim você sabe onde inserir o bloco novo sem bagunçar a sequência.'},
            {'t': 'Adicionar seção', 'b': 'Use para acrescentar um bloco novo ao final da lista de seções. Ao criá-lo, dê um nome que diga qual conteúdo ele reúne.'},
            {'t': 'Gerenciar a seção', 'b': 'Use o menu (…) para as ações que valem para o bloco inteiro. Antes de mudar uma seção que já tem materiais, confira o que há dentro dela.'},
        ],
        'tips': ['Dê um nome que descreva o bloco: "A célula, unidade dos seres vivos" informa melhor do que "Tema 1".'],
    },
    'actividades': {
        'answer': 'Atividades e materiais são o conteúdo que você coloca dentro de uma seção: textos, fichas, entregas, links, agentes de IA e outros tipos. Use "Adicionar atividade ou material" sempre que quiser que o estudante leia, pratique, envie um trabalho ou tire dúvidas. Escolher bem o tipo desde o início evita refazer a seção depois.',
        'steps': [
            {'t': 'Abrir a seção', 'b': 'Escolha a seção em que o conteúdo deve ficar, para que ele apareça no bloco certo desde o início.'},
            {'t': 'Escolher o tipo', 'b': 'Material, Texto, Link e Nota servem para leitura e consulta; Ficha de trabalho, para praticar; Entrega, para receber arquivos; Tarefa com comentários, para devolver uma correção; e Agente de IA, para tirar dúvidas. Unidade didática e Criar com IA também aparecem na lista.'},
            {'t': 'Preencher o formulário', 'b': 'Cada tipo tem campos próprios. O item só entra na seção quando você confirma com "Adicionar", então confira os dados antes.'},
        ],
        'tips': ['Se o estudante deve enviar um arquivo, use Entrega. Se deve treinar, use Ficha de trabalho.'],
        'example': 'Uma professora de História quer que a turma leia um texto sobre a Revolução Industrial e, em seguida, resolva exercícios. Ela adiciona um Material com o texto e uma Ficha de trabalho na mesma seção, e a turma encontra as duas coisas no mesmo lugar do curso.',
    },
    'tipo-de-actividad': {
        'answer': 'Há cinco tipos de atividade no Seven Assistant: material para ler ou ver, ficha para praticar, entrega para receber um arquivo, tarefa com comentários para devolver uma correção e agente de IA para tirar dúvidas. A escolha depende do que você quer verificar e do que quer receber de volta. Pensar nisso antes evita criar uma atividade que não serve ao seu objetivo.',
        'steps': [
            {'t': 'Leitura ou vídeo', 'b': 'Use Material ou Texto para apresentar um conteúdo que o estudante precisa ler ou ver. Se a intenção for que ele responda algo, escolha outro tipo.'},
            {'t': 'Treino', 'b': 'Ficha de trabalho serve para o estudante exercitar o que acabou de ver. É a escolha indicada antes de uma prova ou para a prática em casa.'},
            {'t': 'Receber um arquivo', 'b': 'Entrega serve para receber o trabalho do estudante como arquivo, dentro de um prazo. Defina no enunciado exatamente o que deve ser entregue.'},
            {'t': 'Devolutiva sobre o trabalho', 'b': 'Tarefa com comentários é o tipo para devolver uma correção ao estudante. Se ainda não a criou, faça-o primeiro na Biblioteca, porque o curso recebe uma cópia dela.'},
            {'t': 'Assistente para as dúvidas', 'b': 'Agente de IA responde às perguntas dos estudantes seguindo as instruções que você escreve. Quanto mais claro o que ele pode e não pode dar, mais útil ele fica para a turma.'},
        ],
        'tips': ['Se uma atividade pede ao mesmo tempo leitura e entrega, separe em duas: um material e uma entrega, cada um com a sua função.'],
        'example': 'Uma professora quer saber se a turma entendeu a fotossíntese. Ela cria uma ficha com três exercícios para treinar em casa. Se depois quiser o texto escrito dos estudantes, adiciona uma entrega; se quiser devolver comentários sobre o texto, usa uma tarefa com comentários.',
    },
    'tarea-con-comentarios': {
        'answer': 'Uma tarefa com comentários é uma atividade que você escolhe da Biblioteca e coloca em uma seção do curso, para o estudante entregar o trabalho e receber devolutiva. O curso recebe uma cópia dela, então mudanças feitas depois na Biblioteca não alteram o que já está no curso. Use quando quiser que uma tarefa pronta faça parte do curso, sem precisar recriá-la.',
        'steps': [
            {'t': 'Adicionar atividade ou material', 'b': 'Confirme em qual seção você está antes de continuar, porque é nela que a tarefa vai aparecer.'},
            {'t': 'Escolher Tarefa com comentários', 'b': 'Selecione esse tipo para indicar que a atividade será devolvida com comentários. O título da janela mostra a seção de destino, e vale conferi-lo antes de seguir.'},
            {'t': 'Escolher da biblioteca', 'b': 'Aqui aparecem as tarefas que você já criou na Biblioteca. Se aparecer "Sua biblioteca ainda não tem nada desse tipo", crie primeiro a tarefa de correção.'},
            {'t': 'Selecionar e adicionar', 'b': 'A tarefa entra na seção com o seu tipo, e o curso fica com a cópia. Se você ajustar a tarefa na Biblioteca depois, lembre-se de que a mudança não chega ao curso sozinha.'},
        ],
        'tips': ['Crie a tarefa na Biblioteca antes, seguindo o artigo sobre tarefas de correção e feedback.'],
        'example': 'Um professor de Língua Portuguesa criou na Biblioteca uma tarefa de redação com critérios claros. Ao usá-la no curso do 9.º ano, ela entra na seção "Produção de texto" com o tipo Tarefa com comentários. Se depois ele ajustar a redação na Biblioteca, o curso continua com a versão que já foi copiada.',
    },
    'vistas-del-curso': {
        'answer': 'A visualização define como as seções e os conteúdos aparecem na visão geral do curso: em lista, em lista com pré-visualização, em mosaicos ou com cada seção em sua própria página. Escolha a que deixa o curso mais claro para você e para os estudantes. Vale revisar isso quando o curso crescer e a visão geral começar a ficar longa demais.',
        'steps': [
            {'t': 'Lista', 'b': 'É a opção mais compacta, com títulos e tipos um embaixo do outro. Funciona bem quando o curso tem muitos conteúdos e você quer ver tudo de uma vez.'},
            {'t': 'Lista com pré-visualização', 'b': 'Mostra as primeiras linhas de cada conteúdo, o que ajuda a reconhecer um item sem precisar abri-lo.'},
            {'t': 'Mosaicos', 'b': 'Cada seção mostra os seus conteúdos como cartões, o que dá um aspecto mais visual à visão geral.'},
            {'t': 'Seções como mosaicos', 'b': 'Cada seção tem a sua própria página, o que separa melhor os blocos quando o curso é grande.'},
            {'t': 'Navegação entre conteúdos', 'b': 'Quando ativada em Definições, cada conteúdo traz links para o anterior e o seguinte, e o estudante percorre o material na ordem sem voltar à visão geral.'},
        ],
        'tips': ['Para os estudantes, Lista com pré-visualização costuma ser a mais clara.'],
        'example': 'Um professor de Geografia tem muitos materiais por seção. Ele escolhe Lista com pré-visualização para que os estudantes reconheçam cada material pelas primeiras linhas e ativa a navegação entre conteúdos, para que a leitura siga a ordem da aula.',
    },
    'unirse-curso': {
        'answer': 'Estudantes podem entrar em um curso de três formas: com o código de inscrição e a própria conta, com o link do curso, sem conta, ou aceitando um convite enviado por e-mail. Cada caminho atende a um caso: o código para quem já tem conta, o link para quem ainda não tem e o convite para quem o docente cadastrou diretamente. Este artigo ajuda a orientar o estudante a escolher o caminho certo.',
        'steps': [
            {'t': 'Com código e conta', 'b': 'Use este caminho quando o estudante já tem conta no Seven Assistant. O nome que aparece no curso é o da conta, então não é preciso digitá-lo.'},
            {'t': 'Com o link, sem conta', 'b': 'Serve para quem ainda não tem conta. Depois de entrar, o estudante aparece na lista de participantes do curso, e o docente o identifica por esse nome.'},
            {'t': 'Com um convite por e-mail', 'b': 'É preciso aceitar o convite com a conta à qual ele foi enviado. Se não encontrar o convite, peça ao docente que o envie de novo.'},
        ],
        'tips': ['Se o estudante já tem um código de acesso pessoal deste curso, a página do link oferece a opção "Tenho um código de acesso".'],
        'example': 'Uma estudante do 8.º ano ainda não tinha conta no Seven Assistant, mas a professora de Ciências compartilhou o link do curso. Ela escreveu o seu nome e a primeira letra do sobrenome e entrou no curso sem precisar criar conta. A professora a encontrou na lista de participantes.',
    },
    'ia-alumnado': {
        'answer': 'Na aba Definições, a seção IA no curso permite decidir se os estudantes podem usar a IA, como ela responde e quantas mensagens cada um pode enviar por dia. Esses ajustes valem só para este curso, e você pode pausar a IA quando precisar. Use-os para alinhar a IA ao tipo de trabalho que espera do estudante, por exemplo treinar sem receber a solução pronta.',
        'steps': [
            {'t': 'Ativar ou desativar a IA', 'b': 'Liga ou desliga a IA para os estudantes de todo o curso. Desligue-a durante uma avaliação ou enquanto a turma ainda não estiver pronta para usá-la.'},
            {'t': 'Escolher como ela responde', 'b': 'Tutor de IA, o padrão, dá dicas e faz perguntas sem entregar soluções completas. Só conteúdos do curso restringe as respostas ao material do curso, e Livre também responde a assuntos de fora dele.'},
            {'t': 'Escolher as funções', 'b': 'Gerar imagens e Busca na web vêm desativadas, e Anexar arquivos vem ativada. Ative apenas o que você quer que os estudantes usem neste curso.'},
            {'t': 'Limitar as mensagens', 'b': 'Define quantas mensagens cada estudante pode enviar por dia. O padrão é 50; reduza se quiser limitar o uso ou aumente se a turma precisar de mais.'},
            {'t': 'IA para convidados', 'b': 'Vale para quem entrou pelo link público. Vem desativada, então ative-a só se quiser que essas pessoas usem a IA do curso.'},
            {'t': 'Pausar a IA', 'b': 'Interrompe a IA do curso enquanto você precisar, por exemplo durante uma avaliação. Lembre-se de reativá-la quando a atividade terminar.'},
        ],
        'tips': ['Os professores podem usar a IA do curso sempre, mesmo que os estudantes não a tenham ativada.'],
        'example': 'Um professor de Espanhol quer que a turma treine redações sem receber o texto pronto. Ele deixa o Tutor de IA ativado, mantém desligadas a Busca na web e a geração de imagens e reduz o limite diário de mensagens. Assim a IA dá pistas e faz perguntas, e o estudante continua escrevendo sozinho.',
    },
    'agente-de-ia': {
        'answer': 'Um agente de IA é um assistente criado dentro do curso, com um nome e instruções que você define, para que os estudantes tirem dúvidas sobre aquela parte do conteúdo. Ele responde seguindo as regras que você escreve, o que permite oferecer apoio com limites claros. Use quando quiser ter ajuda disponível fora do horário de aula, sem que ele entregue as respostas prontas.',
        'steps': [
            {'t': 'Escolher Agente de IA', 'b': 'Está entre os tipos de atividade da seção. Use-o quando a mesma dúvida se repete e você quer oferecer apoio permanente sobre aquele tema.'},
            {'t': 'Escrever o título', 'b': 'Dê um nome que diga em que o agente ajuda, para os estudantes saberem quando recorrer a ele. "Ajudante da célula" já informa o tema logo de início.'},
            {'t': 'Escrever as instruções', 'b': 'É o campo que define como o agente se comporta. Diga o que ele deve fazer e, principalmente, o que não deve entregar, como a solução completa dos exercícios.'},
            {'t': 'Adicionar', 'b': 'O agente aparece na seção. Antes de liberá-lo para a turma, faça uma pergunta como um estudante faria para conferir se a resposta segue as instruções.'},
        ],
        'tips': ['Se o agente der a solução completa, a instrução está permissiva demais: reescreva-a deixando claro o que ele não deve fazer.'],
        'example': 'Um professor de Biologia cria um agente para a seção sobre a célula, chamado "Ajudante da célula". Nas instruções, pede que ele faça perguntas que levem o estudante a pensar e não entregue as respostas dos exercícios. Os estudantes tiram dúvidas com ele fora do horário de aula.',
    },
    'participantes-citas': {
        'answer': 'A aba Compromissos reúne as sessões do curso com data, horário e local. Cada encontro criado aparece em "Próximos", e a visão geral mostra o próximo, para que você e os estudantes saibam quando e onde será a aula. Crie os compromissos ao planejar o calendário do curso, para que a agenda esteja visível antes das aulas.',
        'steps': [
            {'t': 'Abrir a aba Compromissos', 'b': 'Se o curso ainda não tiver encontros, aparece "Este curso ainda não tem encontros". É o seu ponto de partida para montar a agenda.'},
            {'t': 'Criar compromisso', 'b': 'Abre o formulário da sessão. Os campos Das e Até definem o horário do encontro, enquanto Local e Nota são opcionais.'},
            {'t': 'Preencher o formulário', 'b': 'O título deve dizer o que será feito no encontro, para a turma se preparar. Use o local para indicar o espaço onde a aula acontece.'},
            {'t': 'Salvar', 'b': 'O encontro passa a aparecer em "Próximos", com dia, horário, título e local. Confira a lista depois de salvar, para garantir que a data está certa.'},
        ],
        'tips': ['Use a Nota para o material que os estudantes devem trazer, por exemplo "Trazer o microscópio óptico e uma cebola".'],
        'example': 'Uma professora de Ciências tem laboratório na próxima semana. Ela cria o compromisso "Laboratório: observar células de cebola" no dia 24, das 09:00 às 09:50, no laboratório de ciências, e registra na nota o que os estudantes precisam trazer. A turma vê o encontro em "Próximos" e chega preparada.',
    },
    'configuracion-del-curso': {
        'answer': 'A aba Definições reúne todos os ajustes do curso: dados gerais, capa, visualização, código de inscrição, IA, exportação e arquivamento. Use-a quando precisar mudar algo que vale só para aquele curso, como o código de entrada ou o que os estudantes podem fazer com a IA. Ajustar o essencial no começo do curso evita correções em cima da hora.',
        'steps': [
            {'t': 'Dados gerais', 'b': 'Nome do curso, disciplina, turma ou série e descrição. Um nome que identifique turma e disciplina facilita encontrar o curso depois, e as alterações só são gravadas quando você as aplica nessa mesma seção.'},
            {'t': 'Capa', 'b': 'É a imagem que aparece no curso, na lista de cursos e na página de inscrição. Escolha uma que identifique a disciplina, para reconhecer o curso rapidamente.'},
            {'t': 'Visualização', 'b': 'Define como o conteúdo aparece na visão geral e se cada conteúdo traz links para o anterior e o seguinte. Compare as opções no artigo sobre a visualização do curso.'},
            {'t': 'Código de inscrição', 'b': 'É o código que a turma usa para entrar, e há também o link público, que vem desativado por padrão. Ao gerar um novo código, o antigo deixa de servir para novas entradas, então avise a turma antes.'},
            {'t': 'IA no curso', 'b': 'Controla o que os estudantes podem fazer com a IA. Antes de liberar, veja o artigo sobre IA para estudantes.'},
            {'t': 'Exportação e arquivamento', 'b': 'Permite exportar o conteúdo ou arquivar o curso e sair dele. Antes de arquivar, confirme que você não vai precisar dele para outra turma.'},
        ],
        'tips': ['A exclusão do curso não faz parte dos passos normais: use-a só com certeza, porque não há como desfazê-la.'],
        'example': 'Uma professora de Matemática usa o curso do 8.º ano pelo segundo ano seguido. Antes do início das aulas, atualiza o nome com o ano letivo, gera um novo código de inscrição e revisa a IA do curso. Ao final do ano, exporta uma cópia de segurança antes de arquivar o curso.',
    },
    'hacer-pregunta': {
        'answer': 'Fazer uma pergunta é escrever no campo de Conversas e enviar, a forma mais direta de pedir algo ao assistente. Quanto mais contexto você der (país, etapa, ano, disciplina, número de estudantes e tempo disponível), mais a resposta se encaixa na sua turma. Use para planejar aulas, rever conteúdos ou criar atividades, e confira sempre o resultado antes de usá-lo.',
        'steps': [
            {'t': 'Escrever no campo', 'b': 'O campo fica na página inicial, com o texto "Pergunte qualquer coisa". Escreva o pedido como se estivesse explicando a tarefa a um colega.'},
            {'t': 'Dar contexto', 'b': 'Informe país, etapa, ano, disciplina, número de estudantes e tempo. Sem essas informações, o assistente precisa supor, e a resposta pode não servir para a sua turma.'},
            {'t': 'Enviar e revisar', 'b': 'Leia a resposta com atenção antes de usá-la com estudantes ou famílias. Se algo não bater com o seu planejamento, peça o ajuste em uma nova mensagem.'},
        ],
        'tips': ['Peça algo concreto: "Crie quatro problemas de proporcionalidade para o 8.º ano" funciona melhor que "me ajude com frações".'],
        'example': 'Uma professora de Ciências do 6.º ano precisa de um roteiro de experimento para uma aula de 50 minutos, com materiais simples que a escola tenha. Ela informa esses dados e pede o formato de uma página, no máximo. Com o pedido claro, o texto sai perto do que ela precisa e exige menos ajustes.',
    },
    'herramientas-asistente': {
        'answer': 'As ferramentas do assistente reúnem modelos prontos para tarefas específicas, como diferenciação, organização de materiais, apoio para deveres ou geração de áudio. Escolher a ferramenta adequada faz a resposta sair mais útil desde a primeira tentativa. Use-as quando sua tarefa se encaixa em uma dessas funções, e escreva o pedido normalmente depois de escolhê-la.',
        'steps': [
            {'t': 'Abrir as ferramentas', 'b': 'O ícone de martelo, na barra de ferramentas do campo de escrita, abre os Modelos do Seven Assistant. Use-o antes de escrever, para que o pedido já saia na ferramenta certa.'},
            {'t': 'Escolher a ferramenta', 'b': 'Diferenciação serve para níveis de dificuldade, Materiais para organizar os seus recursos, Deveres para apoio com as tarefas e Texto de áudio para gerar áudio ou transcrever vídeos. Escolha pela tarefa que você precisa resolver.'},
            {'t': 'Modo de conversa', 'b': 'O botão Dinâmico muda o modo da conversa, com opções como Busca na web, Criar imagens e Sequência didática. Busca na web é a escolha para informação atual, e Sequência didática, para planejar um conjunto de aulas.'},
            {'t': 'Escrever o pedido', 'b': 'Descreva o tema, a turma e o objetivo da aula. Quanto mais específico o pedido, menos ajustes você terá de fazer depois.'},
        ],
        'example': 'Um professor precisa de uma atividade para três níveis de dificuldade na mesma turma. Ele escolhe a ferramenta Diferenciação, indica o tema e a turma no pedido e pede propostas para cada nível. Assim tem um ponto de partida para cada grupo.',
    },
    'regenerar-respuesta': {
        'answer': 'Gerar a resposta de novo pede ao assistente que responda outra vez à mesma pergunta, sem que você precise reescrevê-la. Use quando a resposta estiver fraca, genérica, longa demais ou fora do formato de que você precisa. Se a segunda versão ainda não servir, gere de novo, mas, se o problema estiver no pedido, ajuste-o antes.',
        'steps': [
            {'t': 'Gerar de novo', 'b': 'A opção fica na própria resposta. Use-a quando o problema está no texto que veio, e não no pedido, porque o contexto que você já deu continua valendo.'},
            {'t': 'Mudar o pedido, se for preciso', 'b': 'Se a resposta continuar sem se encaixar, o pedido provavelmente precisa de mais contexto ou de um formato mais claro antes de gerar outra vez.'},
        ],
        'tips': ['Mude uma coisa por vez ao pedir ajustes: assim você sabe o que melhorou.'],
        'example': 'Você pede uma lista de atividades para o 5.º ano e a primeira é teórica demais. Você gera a resposta de novo e recebe outra proposta, mais prática. Se ainda não agradar, gera mais uma vez.',
    },
    'subir-documento': {
        'answer': 'Subir um documento é guardar na Biblioteca um PDF, um vídeo ou o endereço de uma página, para que o assistente possa usá-lo nas suas conversas. Use quando tiver um material de referência que quer reaproveitar, como um capítulo de livro didático ou um artigo. Quando o documento estiver Pronto, a IA já pode trabalhar com ele.',
        'steps': [
            {'t': 'Abrir Minha biblioteca', 'b': 'É onde ficam os documentos que você já tem. Veja-os antes de enviar algo, para não guardar duas vezes o mesmo arquivo.'},
            {'t': 'Conteúdo', 'b': 'É o botão que dá acesso ao envio de novos itens, no alto da página. Ele é o ponto de partida para adicionar qualquer documento.'},
            {'t': 'Escolher o que enviar', 'b': 'Enviar arquivos serve para PDFs ou vídeos do seu computador. Adicionar página web é para materiais que estão na internet, como um artigo, e pede apenas o endereço.'},
            {'t': 'Aguardar até ficar Pronto', 'b': 'Enquanto aparece "A preparar…", o documento ainda está sendo processado. Só use-o nas conversas depois que o status mudar para Pronto.'},
            {'t': 'Revisar o documento', 'b': 'Abra o documento para conferir se o conteúdo foi lido corretamente. Se o resumo não representar bem o material, você pode editá-lo ou abrir a página original.'},
        ],
        'tips': [
            'Dê a cada arquivo um nome que identifique disciplina, turma e data. Assim você o encontra depois com o buscador de Minha biblioteca ("Pesquisar documentos…").',
            'Se você começar pela página inicial da Biblioteca, use o atalho de envio: ele leva a Minha biblioteca, onde fica o botão Conteúdo.',
        ],
        'example': 'Um professor de História tem um capítulo em PDF do livro didático e um artigo sobre a Revolução Industrial na internet. Ele envia o PDF, adiciona o artigo pelo endereço e confere os dois documentos. Quando for preparar a próxima série de aulas, o material já estará na Biblioteca.',
    },
    'buscar-contenido': {
        'answer': 'O buscador da Biblioteca encontra documentos, séries e fichas pelo nome. Ele economiza tempo quando você tem muito material guardado e não quer percorrer pastas: pode localizar uma prática feita meses atrás, conferir se já existe uma série sobre o tema ou achar a versão vigente entre várias. Use-o antes de criar algo novo, para não duplicar o que já tem.',
        'steps': [
            {'t': 'Pesquisar pelo nome', 'b': 'Digite palavras do título do material, porque a busca considera o nome. Os resultados mostram apenas os elementos que combinam com o que você escreveu.'},
        ],
        'tips': [
            'Use palavras do título: termos com menos de duas letras não entram na busca.',
            'Nomear bem os materiais (veja Nomear e atualizar versões) melhora os resultados.',
        ],
    },
    'serie-de-lecciones': {
        'answer': 'Uma série de aulas é uma sequência de sessões sobre um tema, criada na Biblioteca para planejar um conjunto de aulas de uma vez. Ela fica salva na sua lista de séries e pode ser encontrada depois pelo buscador. Crie uma série quando o tema se estender por várias aulas e você quiser organizar a progressão antes de começar.',
        'steps': [
            {'t': 'Série de aulas na Biblioteca', 'b': 'A página oferece Gerar com IA, Criar e o buscador. Este caminho usa Criar, indicado quando você já tem o tema e quer descrever a série por conta própria.'},
            {'t': 'Criar', 'b': 'Abre o formulário da série. Tenha em mãos o tema e a lista de sessões antes de começar, para preencher tudo de uma vez.'},
            {'t': 'Preencher o formulário', 'b': 'Tema é o único campo obrigatório. Disciplina, Curso e Idioma ajudam a encontrar a série depois, e a Descrição é onde você registra o conteúdo e as sessões previstas.'},
            {'t': 'Criar a série', 'b': 'A série aparece na lista de séries da Biblioteca. Confira o nome e o idioma antes de começar o planejamento das sessões.'},
        ],
        'tips': ['Descreva as sessões e a avaliação na Descrição: assim a série serve para programar.'],
        'example': 'Um professor de Biologia precisa planejar as aulas sobre os níveis de organização dos seres vivos para o 1.º ano do ensino médio. Ele cria a série com o tema, a disciplina e o curso, e descreve na Descrição as sessões e a forma de avaliação. No ano seguinte, encontra a série pela lista e a ajusta.',
    },
    'ficha-interactiva': {
        'answer': 'Uma ficha interativa é uma folha de trabalho gerada pelo assistente a partir do tema e dos documentos que você indicar, com exercícios e respostas corretas. Ela serve para praticar um conteúdo ou montar um teste sem escrever cada exercício do zero. Use quando precisar de uma ficha rápida, revisando sempre o resultado antes de entregá-la aos estudantes.',
        'steps': [
            {'t': 'Passo 1: Contexto', 'b': 'Defina tema (obrigatório), disciplina, nível escolar, dificuldade e idioma. A extensão indica se a ficha será um miniteste, uma ficha de exercícios, um material de apoio ou um teste de avaliação.'},
            {'t': 'Passo 2: Fontes', 'b': 'Indique os documentos que a ficha deve usar, da Biblioteca ou por pesquisa. O indicador mostra quanto contexto a ficha está usando, o que ajuda a decidir se vale incluir mais um documento.'},
            {'t': 'Passo 3: Análise e ajuste', 'b': 'Antes de gerar, ajuste o número de exercícios e a densidade do texto. Essas escolhas definem o tamanho e o ritmo da ficha.'},
            {'t': 'Continuar até o final', 'b': 'Continuar avança de passo, mas não deixa seguir sem o tema. Passe pelos três passos com calma para não perder nenhum ajuste.'},
            {'t': 'Gerar', 'b': 'Inicia a criação da ficha com os ajustes feitos nos passos anteriores.'},
            {'t': 'Aguardar o resultado', 'b': 'A geração leva entre 1 e 3 minutos. Não feche a página enquanto espera.'},
            {'t': 'Conferir a ficha', 'b': 'Revise o título, os blocos de exercícios e as respostas corretas. Se aparecer um aviso de verificação, reveja essas respostas antes de distribuir a ficha.'},
        ],
        'tips': ['Para material de apoio, densidade compacta e dificuldade baixa. Para teste de avaliação, densidade equilibrada.'],
        'example': 'Um professor de Matemática do 7.º ano precisa de um miniteste sobre frações para a próxima semana. No passo de contexto, escolhe o tema e o nível médio; em Fontes, inclui o capítulo já guardado na Biblioteca; e, com a densidade equilibrada, gera a ficha. Antes de aplicá-la, resolve os exercícios e confere as respostas.',
    },
    'ficha-de-trabajo-curso': {
        'answer': 'Uma ficha de trabalho é uma folha de prática que o estudante resolve dentro do curso, com exercícios que você prepara. Ela serve para treinar o que acabou de ser visto e para identificar o que ainda não ficou claro. Use depois de explicar um conceito, como revisão antes de uma prova ou prática para casa.',
        'steps': [
            {'t': 'Adicionar a ficha na seção', 'b': 'Escolha a seção do conteúdo que a ficha pratica, para que ela fique junto da explicação. Antes de adicioná-la, resolva-a como um estudante faria.'},
        ],
        'tips': ['Comece com um exercício resolvido, siga com exercícios parecidos e termine com um mais difícil.'],
    },
    'tarea-correccion-biblioteca': {
        'answer': 'Uma tarefa de correção e feedback é uma atividade criada na Biblioteca, com critérios, pontos e uma solução modelo oculta para os estudantes. Ela permite corrigir todos os trabalhos com a mesma régua e explicar cada nota com clareza. Use quando quiser avaliar entregas com critérios definidos e registrar a pontuação de cada aspecto.',
        'steps': [
            {'t': 'Tarefa de correção e feedback', 'b': 'Aqui você cria a tarefa, que depois pode ser levada a um curso pelo tipo Tarefa com comentários.'},
            {'t': 'Dados gerais', 'b': 'Título, Rigor da avaliação (padrão Equilibrado) e Envios máximos (padrão 1) definem a exigência e o número de entregas permitidas. Descreva a tarefa com clareza, porque é a partir dela que o estudante entende o que entregar.'},
            {'t': 'Solução modelo', 'b': 'É a resposta de referência que você usará na correção. Ela fica oculta para os estudantes, então pode conter detalhes que você não quer mostrar a eles.'},
            {'t': 'Critérios de avaliação', 'b': 'Cada critério descreve algo a verificar e recebe pontos, com padrão de 10. Os pontos devem ficar entre 0,5 e 1000, em passos de meio ponto.'},
            {'t': 'Criar', 'b': 'A tarefa passa a aparecer na lista de Tarefas de correção e feedback. Antes de usá-la, confira os critérios e os pontos de cada um.'},
            {'t': 'Revisar as entregas', 'b': 'Ao abrir uma entrega, você vê o texto do estudante, a pontuação de cada critério e o comentário. Confira a nota com os critérios que definiu, para manter a mesma régua em todos os trabalhos.'},
        ],
        'tips': [
            'Se digitar texto no campo de pontos, o formulário não salva e aparece em vermelho o aviso "Entre 0,5 e 1000 pontos".',
            'Calibre com três trabalhos antes de corrigir a turma.',
        ],
        'example': 'Um professor de Língua Portuguesa cria uma tarefa de redação com três critérios, cada um valendo 10 pontos. Na solução modelo, descreve o que um texto completo deveria trazer. Quando a turma entrega, abre cada entrega e registra a nota e o comentário de cada critério.',
    },
    'plantillas-vs-asistentes': {
        'answer': 'Os modelos de curso são unidades didáticas prontas para adotar em Cursos, e os assistentes são modelos da barra lateral com instruções próprias. Use um modelo de curso quando quiser começar com uma unidade já pronta, e um assistente quando quiser que a IA siga as suas instruções nas tarefas que você repete. Entender essa diferença evita procurar o que você precisa no lugar errado.',
        'steps': [
            {'t': 'Modelos de curso', 'b': 'Ficam dentro de Cursos, na aba Modelos. São unidades prontas que você adota e depois adapta à sua turma.'},
            {'t': 'Assistentes de IA', 'b': 'Ficam em Modelos, na barra lateral (ícone de estrelas). Seguem as instruções que você escreve e servem para tarefas que se repetem.'},
        ],
        'tips': ['Se quer um conteúdo já pronto, é um modelo de curso; se quer que a IA trabalhe com as suas instruções, é um assistente.'],
        'example': 'Você precisa de uma unidade sobre "A água" para uma turma do 3.º ano: procura em Cursos, na aba Modelos, e adota a unidade pronta. Já se quer um assistente que corrija redações com os seus critérios, você o cria em Modelos (ícone de estrelas) com as suas instruções.',
    },
    'crear-asistente': {
        'answer': 'Um assistente de IA criado em Modelos é uma conversa pré-configurada, com um nome e uma instrução sua, que você reutiliza sempre que precisar do mesmo tipo de ajuda. Ele fica disponível na sua lista e pode ser testado antes de você usá-lo com a turma. Crie um assistente quando uma tarefa se repete, como corrigir redações ou preparar guias de laboratório.',
        'steps': [
            {'t': 'Modelos', 'b': 'É o ícone de estrelas na barra lateral e reúne a sua lista de assistentes. Confira se já existe um parecido antes de criar outro.'},
            {'t': 'Criar modelo', 'b': 'Os campos são Nome e Instrução. A instrução define o papel do assistente e costuma começar com algo como "Você é um assistente útil...".'},
            {'t': 'Preencher o formulário', 'b': 'Na instrução, descreva o papel do assistente, os passos que ele deve seguir e o que ele não deve fazer. Quanto mais precisa a instrução, mais previsível fica o resultado.'},
            {'t': 'Salvar', 'b': 'O modelo passa a aparecer na lista de Modelos, pronto para ser testado.'},
            {'t': 'Testar em um chat', 'b': 'Faça uma pergunta real, como a que a turma faria. Se a resposta for completa demais, volte à instrução e torne-a mais precisa.'},
        ],
        'tips': ['Escreva o nome com tipo e etapa para encontrá-lo depois.'],
        'example': 'Uma professora de Biologia cria o assistente "Guia de laboratório · 1.º ano" com a instrução de explicar o procedimento em etapas, lembrar as medidas de segurança e não redigir o relatório pronto para o estudante. Ela testa com uma pergunta e ajusta a instrução até a resposta ficar no nível da turma.',
    },
    'idioma': {
        'answer': 'A opção de idioma muda os menus e os botões do Seven Assistant entre espanhol e português do Brasil, sem alterar o conteúdo que você já criou. Use quando trabalha com colegas que usam outro idioma, quando compartilha o computador com alguém que prefere outro idioma ou quando quer que a interface combine com os materiais que prepara. Como a escolha vale para a sua conta, cada pessoa que usa a mesma ferramenta pode ter o seu próprio idioma.',
        'steps': [
            {'t': 'Menu da conta', 'b': 'O avatar fica embaixo à esquerda, com as suas iniciais, e é daqui que se acessam os ajustes da sua conta, incluindo o idioma.'},
            {'t': 'Idioma', 'b': 'Escolha o idioma da interface. A mudança vale para a sua conta, então cada pessoa ajusta o próprio idioma.'},
        ],
        'tips': ['Os textos que você escreve permanecem no idioma em que foram criados.'],
    },
    'menu-de-cuenta': {
        'answer': 'O menu da conta fica no avatar, embaixo à esquerda, com as suas iniciais. Dali você acessa Configurações, troca o idioma, gerencia tarefas e pastas compartilhadas, consulta as novidades e a ajuda e encerra a sessão. Use-o para ajustar a sua conta e para sair quando estiver em um computador que não é seu.',
        'steps': [
            {'t': 'Avatar', 'b': 'Fica embaixo à esquerda e mostra as suas iniciais, o que ajuda a confirmar em qual conta você está antes de fazer alterações.'},
            {'t': 'Opções do menu', 'b': 'Configurações reúne os ajustes da conta; Idioma muda a interface; Gerenciar tarefas e Gerenciar pastas compartilhadas organizam o seu trabalho; O que há de novo? mostra as novidades; Ajuda, para dúvidas; e Sair encerra a sessão.'},
        ],
        'tips': ['Encerre a sessão se usar um computador compartilhado.'],
        'example': 'Você termina o trabalho em um computador da escola. Ao sair da conta pelo menu do avatar, ela deixa de ficar aberta para quem usar o computador depois.',
    },
    'carpetas-compartidas': {
        'answer': 'Pastas compartilhadas são espaços para reunir materiais com outras pessoas, e você entra em uma pasta existente com um token. Elas ficam em Gerenciar pastas compartilhadas, no menu da conta, onde também é possível criar uma pasta nova. Use quando quiser guardar material junto com o departamento ou com colegas que dão a mesma disciplina.',
        'steps': [
            {'t': 'Gerenciar pastas compartilhadas', 'b': 'Fica no menu da conta e serve para criar uma pasta nova ou entrar em uma que já existe.'},
            {'t': 'Nova pasta', 'b': 'Pede um nome e uma descrição. Escreva uma descrição que diga o conteúdo e para quem a pasta serve, para que os colegas entendam sem perguntar.'},
            {'t': 'Preencher e salvar', 'b': 'Use um nome que identifique a área e o tipo de material, como "Departamento de Biologia · materiais". Um nome assim torna a pasta fácil de reconhecer na lista.'},
            {'t': 'Entrar com um token', 'b': 'Se alguém compartilhou uma pasta com você, digite o token no campo da parte de cima para entrar nela.'},
        ],
        'tips': ['Trate o token como uma senha: não o publique.'],
        'example': 'Um departamento de Biologia cria a pasta "Departamento de Biologia · materiais" com uma descrição dizendo que ali ficam as fichas e os guias de laboratório. Quando chega um professor novo, ele recebe o token e entra na pasta para encontrar o material do departamento.',
    },
    'participantes-permisos': {
        'answer': 'A aba Participantes mostra quem tem acesso ao curso, separado entre docentes e estudantes. Os convites que ainda não foram aceitos aparecem com a etiqueta "Convidado" até a pessoa entrar. Use para conferir quem está no curso, quem ainda falta entrar e qual papel cada pessoa tem antes de começar as aulas.',
        'steps': [
            {'t': 'Abrir Participantes', 'b': 'Aqui estão o buscador, o botão "Convidar pessoas" e os filtros Todos, Docentes e Estudantes, com a quantidade de cada grupo. Use os filtros para conferir cada papel separadamente.'},
            {'t': 'Distinguir os papéis', 'b': 'Cada pessoa aparece como Docente ou Estudante, e "Você" marca o seu próprio perfil. Confira o papel antes de convidar alguém, para não misturar docentes e estudantes.'},
            {'t': 'Conferir os convites pendentes', 'b': 'Em "Convites" ficam as pessoas convidadas por e-mail, com o papel e a etiqueta "Convidado", até aceitarem. Se alguém não aparece como participante, confira se o e-mail do convite está correto.'},
        ],
        'tips': ['Para convidar alguém, consulte "Convidar alunos": ali estão as três formas de entrar.'],
        'example': 'Uma coordenadora acompanha o curso de Matemática do 8.º ano junto com outra professora. Ela confere na aba Participantes que as duas aparecem como Docente e que os estudantes estão no filtro Estudantes. Um estudante que ainda aparece em "Convites" recebe um novo convite no e-mail correto.',
    },
    'organizacion-centro': {
        'answer': 'Organizar os cursos da escola é combinar, antes de criar muitos cursos, como cada um será nomeado: disciplina, turma ou série e ano. Com um padrão único, qualquer docente ou coordenador reconhece cada curso sem precisar perguntar. Faça isso ao preparar o novo ano letivo ou quando coordena docentes que devem seguir o mesmo padrão.',
        'steps': [
            {'t': 'Combinar disciplinas e séries', 'b': 'Use sempre os mesmos nomes nos campos Disciplina e Turma ou série. Assim não surgem variações, como "Mat." e "Matemática", que confundem quem procura o curso.'},
            {'t': 'Definir um formato para os títulos', 'b': 'Escolha um modelo fixo, como "Matemática · 8.º ano · 2026", e aplique-o a todos os cursos. Um formato único deixa a lista mais fácil de ler.'},
            {'t': 'Revisar todo ano', 'b': 'Ao fechar o ano letivo, revise os nomes e ajuste-os para o seguinte, para que o padrão continue valendo.'},
        ],
        'tips': ['Documente a convenção em um único lugar e compartilhe com a coordenação.'],
    },
    'seguridad-datos': {
        'answer': 'Esta ajuda resume o que o Seven Assistant declara sobre os dados: hospedagem na Alemanha, conformidade com o RGPD, nenhum treinamento da IA com os dados da sua escola e certificações ISO 27001, 9001 e 14001. Ela também lista as perguntas que a escola precisa responder e os cuidados conforme o país. Use este artigo ao avaliar a ferramenta com a direção, a coordenação ou o jurídico.',
        'steps': [
            {'t': 'O que é garantido', 'b': 'São as garantias informadas pelo fornecedor: dados hospedados na Alemanha, conformidade com o RGPD, nenhum treinamento da IA com os seus dados e as certificações ISO 27001, 9001 e 14001. Use-as como ponto de partida para a avaliação, e não como conclusão.'},
            {'t': 'Perguntas que você precisa responder', 'b': 'Antes de usar a ferramenta com estudantes, a escola deve saber onde os dados ficam, quem pode acessá-los, como são protegidos e eliminados e quais dados pessoais são tratados. As respostas podem ser registradas como base da decisão.'},
            {'t': 'Documentação oficial', 'b': 'Para a documentação completa, solicite-a em 7education.com informando o nome da sua escola. Assim a avaliação se apoia no documento, e não só nesta ajuda.'},
            {'t': 'Minimizar os dados dos estudantes', 'b': 'Use identificadores internos, em vez de nomes completos, sempre que for possível. Assim há menos dado pessoal para proteger.'},
            {'t': 'Conformidade local', 'b': 'Brasil (LGPD), México (LFPDPPP) e Chile, cuja legislação de dados pessoais está em atualização, têm exigências próprias. Consulte o jurídico da sua escola antes de decidir.'},
        ],
        'tips': ['Defina quem avisar se uma conta for comprometida e em quanto tempo.'],
        'example': 'Uma escola avalia o Seven Assistant antes de liberar o acesso aos professores. A coordenação pede a documentação, responde por escrito às cinco perguntas e decide usar identificadores internos nos cursos, sem nomes completos dos estudantes. O jurídico confirma as exigências da legislação local antes da liberação.',
    },
    'no-encuentro-seccion': {
        'answer': 'As áreas principais ficam sempre na barra lateral, e o que não aparece ali costuma estar dentro de um curso, na Biblioteca ou no menu da conta. Use este artigo quando procurar algo que não encontra: séries, fichas e tarefas estão na Biblioteca, e os ajustes gerais, no menu da conta. Os ajustes de um curso específico ficam dentro dele, em Definições.',
        'steps': [
            {'t': 'Conferir a barra lateral', 'b': 'Conversas, Cursos, Biblioteca e Modelos estão sempre ali. Se você procura uma dessas áreas, comece por elas.'},
            {'t': 'Procurar na Biblioteca', 'b': 'Séries, fichas e tarefas são criadas a partir da Biblioteca. Se não as encontra em Cursos, provavelmente estão lá.'},
            {'t': 'Conferir o menu da conta', 'b': 'Configurações, Idioma e pastas compartilhadas ficam no avatar, embaixo à esquerda. Ajustes gerais da conta não estão dentro de nenhum curso.'},
        ],
        'tips': ['Procure pelo nome exato da ação no buscador da ajuda, porque ela pode ter mudado de lugar.'],
    },
    'codigo-filtrado': {
        'answer': 'Se um código ou link de inscrição chegou a pessoas que não deveriam entrar, gere um novo código e desative o link público quando ele não for mais necessário. Faça isso quando o código foi compartilhado fora da turma ou quando um link público continua ativo depois do fim do curso. Assim, só entra quem faz parte da sua turma.',
        'steps': [
            {'t': 'Código de inscrição', 'b': 'Fica na aba Definições do curso, onde você troca o código e confere o link público.'},
            {'t': 'Gerar novo código', 'b': 'O código antigo deixa de servir para novas entradas. Compartilhe o novo somente com a turma, e não em grupos abertos.'},
            {'t': 'Revisar o link público', 'b': 'Um link público ativo permite a entrada de quem o tiver. Se você não precisar mais dele, desative-o.'},
        ],
        'tips': ['Se precisar que alguém específico entre, compartilhe o código só com essa pessoa.'],
        'example': 'Uma professora compartilhou o código em um grupo de famílias e alguém de fora da turma entrou. Ela gera um código novo, compartilha-o apenas com a turma e desativa o link público, que já não era necessário.',
    },
    'alumnado-no-entra': {
        'answer': 'Quando um estudante não consegue entrar no curso, quase sempre o problema está no código ou no caminho de entrada. Por isso vale revisar essas duas coisas, nessa ordem. Use este artigo quando uma turma inteira não consegue entrar depois de receber o código, quando um estudante diz que o código não funciona ou quando você quer ver o curso como ele vê antes da primeira aula.',
        'steps': [
            {'t': 'Conferir o código', 'b': 'Compare o código que a turma tem com o que aparece na visão geral do curso. Se ele foi gerado de novo, compartilhe o atual, pois o antigo deixou de servir para novas entradas.'},
            {'t': 'Conferir o caminho', 'b': 'O caminho certo é Entrar em um curso, dentro de Cursos. Se o estudante chegou por outro lugar, peça que refaça o passo a partir daí.'},
            {'t': 'Usar a visão de estudante', 'b': 'Abra "Ver como aluno" para ver o curso como o estudante o vê. Assim você localiza o problema sem depender de tentativa e erro com a turma.'},
        ],
        'tips': ['Confira a visão de estudante antes de compartilhar o código com a turma.'],
        'example': 'No primeiro dia de aula, quatro estudantes digitam o código e recebem um erro. Na visão geral, a professora percebe que o código que eles têm é o antigo, porque ela gerou um novo na semana passada. Ela compartilha o novo, e todos conseguem entrar.',
    },
    'respuesta-no-correcta': {
        'answer': 'O assistente pode dar dados errados ou responder a outra pergunta, por isso a conferência faz parte do uso. Este artigo mostra como revisar uma resposta antes de levá-la para a aula e como pedir uma melhor. Revise principalmente quando a resposta traz números, datas ou citações que você não sabe se são verdadeiros, quando fala de outro nível, país ou formato, ou quando está certa mas não serve para a sua turma.',
        'steps': [
            {'t': 'Revisar os dados', 'b': 'Confira números, datas e informações em uma fonte confiável, como o livro didático, antes de usá-los em aula. Esse é o passo mais importante quando o conteúdo vai direto para os estudantes.'},
            {'t': 'Precisar o contexto', 'b': 'Informe a turma, o nível, o país e o formato que você precisa no novo pedido. Com esses dados, a resposta tende a se encaixar melhor no que você espera.'},
            {'t': 'Gerar de novo', 'b': 'Use a opção de gerar a resposta outra vez quando o problema estiver no texto. Depois, confira de novo os dados que já estavam em dúvida.'},
        ],
        'tips': [
            'Não leve nenhum dado para a aula sem conferi-lo antes, mesmo que a resposta pareça segura.',
            'Mude uma coisa de cada vez ao pedir ajustes.',
        ],
        'example': 'Você pede um resumo da Revolução Francesa para o 9.º ano e a resposta traz uma data que não bate com o livro didático. Você confere a data no livro, pede a correção e acrescenta "alunos de 14 anos, resumo de 10 linhas". A segunda resposta serve.',
    },
    'beta': {
        'answer': 'Cursos está em beta, uma versão que continua sendo melhorada, por isso telas e opções podem mudar de lugar ou de nome. Se algo não coincidir com esta ajuda, isso não é um erro seu. Use este artigo para entender a mudança e saber onde procurar a ação que você precisa.',
        'steps': [
            {'t': 'Procurar a ação', 'b': 'Procure a ação pelo nome no buscador da ajuda ou veja as novidades no menu da conta. Assim você consegue localizar a função mesmo depois de uma mudança.'},
        ],
        'tips': ['Quando algo não coincidir, guarde uma captura de tela: ela ajuda a explicar a mudança para quem dá suporte.'],
    },
    'idioma-no-cambia': {
        'answer': 'Se a interface continua no idioma anterior depois de você escolher outro, o motivo mais comum é que a página aberta ainda não carregou a mudança. Confira primeiro a escolha no menu da conta e depois recarregue a página. Use este artigo quando acabou de trocar o idioma e a tela continua igual, ou quando um colega vê a interface em outro idioma e não sabe por quê.',
        'steps': [
            {'t': 'Escolher o idioma de novo', 'b': 'Repetir a escolha garante que o idioma ficou registrado na sua conta antes de você recarregar a página.'},
            {'t': 'Recarregar a página', 'b': 'Recarregar faz a mudança valer para toda a interface, inclusive para os menus que ainda aparecem no idioma antigo. Faça isso depois de escolher o idioma, e não antes.'},
        ],
        'tips': ['A mudança afeta a interface, não os textos que você já criou.'],
        'example': 'Você muda a interface para espanhol no notebook, mas a aba que já estava aberta continua em português. Você recarrega a página e a mudança vale para toda a interface. Os textos que já escreveu continuam no idioma em que foram criados.',
    },
    'conversacion-modos': {
        'answer': 'O botão Dinâmico, ao lado do campo de escrita, muda o modo da conversa, e cada modo é pensado para um tipo de tarefa. Escolher o modo certo faz o assistente responder de forma mais útil para o que você precisa, seja uma imagem, uma pesquisa atual ou o planejamento de uma sequência. Use este artigo quando não souber qual modo combina com o seu pedido.',
        'steps': [
            {'t': 'Seletor Dinâmico', 'b': 'Fica ao lado do campo de escrita. Confira qual modo está ativo antes de enviar, porque ele muda a forma como o assistente responde.'},
            {'t': 'Escolher o modo', 'b': 'Entre as opções estão Padrão, Criar imagens, Busca na web, Gerenciar biblioteca, Criar H5P, Ler em voz alta, Gerenciar tarefas e Sequência didática. Escolha o modo que corresponde ao resultado que você quer.'},
            {'t': 'Escrever o seu pedido', 'b': 'Com o modo escolhido, descreva o que precisa com etapa, turma e formato. O modo ajuda, mas o contexto continua sendo o que mais define a qualidade da resposta.'},
        ],
        'tips': ['Para buscar informação atual, use Busca na web; para planejar uma sequência, Sequência didática.'],
        'example': 'Uma professora de Biologia precisa de imagens de células para a aula. Ela muda o modo para Criar imagens e descreve o que quer mostrar. Para a sequência de aulas do trimestre, troca para Sequência didática e pede o plano semana a semana.',
    },
    'conversacion-contexto': {
        'answer': 'Um bom contexto (etapa, ano, disciplina, país, tempo disponível e formato) faz o assistente gerar respostas que você pode usar sem reescrever. Essas informações são o que separa uma resposta genérica de uma pronta para a sua turma. Use sempre que pedir materiais, avaliações ou planos de aula, principalmente quando o resultado for levado direto aos estudantes.',
        'steps': [
            {'t': 'Indicar etapa e ano', 'b': 'Diga a etapa e o ano da turma, por exemplo "8.º ano do ensino fundamental" ou "1.ª série do ensino médio". É a informação que mais define o nível do texto e dos exercícios.'},
            {'t': 'Indicar país e escala, se precisar', 'b': 'Informe o país quando a escala de avaliação ou o currículo importar. Assim a rubrica sai na escala certa.'},
            {'t': 'Indicar tempo e formato', 'b': 'Diga quanto tempo a aula ou a atividade terá e em que formato quer o resultado, como um guia de uma página ou uma tabela. Isso evita um material longo demais para o tempo disponível.'},
            {'t': 'Pedir um critério de revisão', 'b': 'Peça que a resposta aponte o que pode confundir os estudantes, por exemplo: "aponte que parte pode confundir um estudante de 12 anos". Essa revisão ajuda a chegar mais rápido ao texto pronto.'},
        ],
        'tips': ['Exemplo: "Atue como professor de matemática do ensino fundamental no Brasil. Prepare um guia de uma página sobre proporcionalidade, com cinco problemas."'],
        'example': 'Uma professora de Geografia pede um material sobre clima para uma turma do 7.º ano, com 50 minutos de aula. Ela informa a etapa, o tempo e o formato, e pede que a resposta aponte os trechos que podem confundir a turma. Com isso, precisa ajustar só os exemplos locais antes de levar o material para a aula.',
    },
    'documentos-nombres': {
        'answer': 'Um nome com disciplina, turma, data e versão deixa claro qual documento está vigente quando há várias versões na Biblioteca. Use esse padrão ao enviar uma versão corrigida, ao compartilhar um material com o departamento ou ao revisar a Biblioteca no início do curso. Assim você evita confundir a versão antiga com a atual.',
        'steps': [
            {'t': 'Usar um formato fixo', 'b': 'Disciplina · turma · data · versão, por exemplo "Matemática · 8.º ano · 2026-11 · v2". Sempre na mesma ordem, o nome fica fácil de ler e de comparar.'},
            {'t': 'Enviar a nova versão', 'b': 'Não reaproveite o nome antigo: o número da versão é o que diferencia os arquivos.'},
            {'t': 'Guardar a anterior só se precisar', 'b': 'Mantenha a versão anterior apenas se for comparar com a nova. Assim fica evidente qual é a vigente.'},
        ],
        'tips': ['Revise todo ano quais documentos ainda estão vigentes.'],
        'example': 'Você tem "Unidade 4 · v1" e "Unidade 4 · v2". Você envia a versão corrigida como "Matemática · 8.º ano · 2026-11 · v2" e guarda a v1 só se precisar compará-las. Assim sabe qual enviar aos estudantes.',
    },
    'serie-campos': {
        'answer': 'Uma série de aulas tem poucos campos: Tema é obrigatório, e os demais ajudam a encontrá-la e a adaptá-la à sua turma. Preencha todos desde o início ao criar uma série, principalmente quando tiver muitas séries e precisar localizá-las por disciplina ou curso. Quanto mais completos os campos, mais útil a série fica para planejar.',
        'steps': [
            {'t': 'Tema', 'b': 'É o objetivo concreto da série. Um tema específico, como "Introdução ao cálculo integral", orienta melhor do que um tema amplo, como "Matemática".'},
            {'t': 'Disciplina e Curso', 'b': 'Servem para encontrar e ordenar a série depois. O campo Curso aceita descrições como "4.º ano", então use o mesmo formato que a sua escola usa.'},
            {'t': 'Idioma', 'b': 'Vem como Espanhol por padrão. Mude se a série for para uma turma que estuda em outro idioma.'},
            {'t': 'Descrição', 'b': 'Registre os objetivos e o conteúdo da série. Quanto mais concreta a descrição, mais a série se encaixa na turma.'},
        ],
    },
    'serie-ajustar': {
        'answer': 'Ajustar uma série de aulas é modificar uma série que você já tem para que ela se encaixe na sua turma. Use quando a primeira versão tiver mais sessões do que você consegue dar, quando o nível não for o da sua turma ou quando a avaliação não coincidir com o seu planejamento. Peça as mudanças em uma conversa e revise a progressão antes de guardar a versão final.',
        'steps': [
            {'t': 'Revisar a progressão', 'b': 'As aulas devem avançar do simples para o complexo. Confira isso antes de mexer em duração ou avaliação, para que os ajustes não quebrem a sequência.'},
            {'t': 'Pedir mudanças uma de cada vez', 'b': 'Peça separadamente a mudança de duração, de nível ou de avaliação. Assim você vê o efeito de cada ajuste e não perde o que estava certo.'},
            {'t': 'Guardar a versão final', 'b': 'Quando a série estiver como você quer, envie-a para Documentos para mantê-la organizada.'},
        ],
        'example': 'A série de "Frações" tem doze sessões e você tem oito. Você pede, em uma conversa, que ela seja reduzida a oito, mantendo a progressão e com a avaliação na sessão 8. Antes de guardar, você revisa a progressão.',
    },
    'tarea-criterios': {
        'answer': 'Um critério observável descreve algo que você consegue ver no trabalho do estudante. Ele permite corrigir com a mesma régua e explicar a nota com clareza. Use quando for corrigir um trabalho com vários aspectos a avaliar ou quando quiser que o estudante entenda por que recebeu cada nota.',
        'steps': [
            {'t': 'Um critério por competência', 'b': 'Separe os critérios por habilidade, como argumentação ou resolução de problemas. Assim cada nota explica uma coisa só, e não uma impressão geral do trabalho.'},
            {'t': 'Descrever o que deve aparecer', 'b': 'Escreva o que precisa estar no trabalho para o critério ser cumprido. Frases que descrevem algo visível são mais fáceis de aplicar com a mesma régua.'},
            {'t': 'Definir níveis com a sua escala', 'b': 'Os níveis devem seguir a escala que você ou a sua escola usa. A Referência traz escalas por país para conferir a correspondência.'},
        ],
        'tips': ['"Argumenta com pelo menos duas evidências" é observável; "boa redação" não é.'],
    },
    'tarea-calibrar': {
        'answer': 'Calibrar é corrigir alguns trabalhos de níveis diferentes e compará-los com a proposta de correção antes de corrigir a turma inteira. Assim os critérios passam a significar a mesma coisa para você e para quem mais corrige a mesma tarefa. Faça isso logo depois de escrever os critérios, antes de corrigir muitos trabalhos seguidos.',
        'steps': [
            {'t': 'Escolher três trabalhos', 'b': 'Pegue um fraco, um médio e um forte. Essa variedade mostra se o critério distingue os níveis de desempenho.'},
            {'t': 'Comparar com a sua avaliação', 'b': 'Confira critério a critério onde a sua avaliação coincidiu e onde divergiu. As divergências mostram onde o texto do critério precisa de mais clareza.'},
            {'t': 'Ajustar os critérios', 'b': 'Se a mesma divergência se repetir, o critério provavelmente não está claro o bastante. Reescreva-o com um exemplo do que conta como cumprido.'},
            {'t': 'Corrigir o restante da turma', 'b': 'Só depois de ajustar os critérios, aplique-os ao restante da turma. Assim a correção fica consistente do primeiro ao último trabalho.'},
        ],
        'tips': ['Guarde os três trabalhos calibrados: eles servem de referência se você tiver dúvidas depois.'],
        'example': 'Uma professora tem 28 redações e critérios para "argumentação". Ela corrige três (uma fraca, uma média e uma forte). Em duas delas não sabe se o critério foi cumprido, então reescreve o critério com um exemplo e corrige o restante da turma com ele.',
    },
    'ficha-densidad': {
        'answer': 'A extensão, a dificuldade e a densidade do texto definem o tamanho e o ritmo de uma ficha. A extensão e o nível ficam no Contexto, e o número de exercícios e a densidade ficam em Análise e ajuste. Ajustar esses itens antes de gerar evita uma ficha longa demais para a aula ou densa demais para a turma.',
        'steps': [
            {'t': 'Extensão', 'b': 'Escolha entre Miniteste, Ficha de exercícios, Material de apoio ou Teste de avaliação. Também defina o número de páginas, que vem com 1 página por padrão.'},
            {'t': 'Número de exercícios', 'b': 'Vem automático por padrão. Desative a opção para escolher a quantidade, e confira o tempo aproximado que o texto mostra.'},
            {'t': 'Densidade do texto', 'b': 'Compacto deixa o texto mais enxuto, Detalhado o deixa mais extenso e Equilibrado, o padrão, fica entre os dois. Escolha pelo uso que a ficha terá.'},
        ],
        'tips': ['Em um teste de avaliação, confira se a quantidade de exercícios cabe no tempo previsto para a prova.'],
        'example': 'Um professor precisa de uma folha de reforço sobre frações. Ele escolhe Material de apoio, densidade Compacto e dificuldade baixa, deixa o número de exercícios no automático e gera a ficha. O resultado é uma folha enxuta, pronta para ser usada como reforço.',
    },
    'ficha-revisar': {
        'answer': 'Revisar uma ficha é resolvê-la antes que ela chegue aos estudantes, para encontrar exercícios mal formulados, respostas erradas ou um nível diferente do da sua turma. Faça isso quando a ficha foi gerada pelo assistente, quando vai usar uma ficha de outro curso ou quando quer garantir que a prática corresponde ao que foi visto antes de uma prova. Esse cuidado evita que um erro chegue à turma.',
        'steps': [
            {'t': 'Resolver dois exercícios', 'b': 'Faça-os como um estudante faria, sem olhar a resposta. Se você travar em algo que a turma não deveria encontrar, o exercício precisa ser ajustado.'},
            {'t': 'Conferir o nível e o idioma', 'b': 'Confirme que o nível e o idioma são os da sua turma. Uma ficha correta, mas em outro idioma ou nível, não serve para a aula.'},
            {'t': 'Usar em um curso', 'b': 'Adicione a ficha à seção certa do curso como Ficha de trabalho, depois de revisada. Assim, o que os estudantes recebem já passou pela sua conferência.'},
        ],
        'tips': ['Se você levar bem mais tempo do que levaria um estudante, a ficha provavelmente está difícil demais.'],
    },
    'plantilla-nombrar': {
        'answer': 'Dar bons nomes aos seus assistentes serve para encontrá-los rapidamente quando você tem vários. Use um padrão com tipo de tarefa e nível, para saber na hora para que cada um serve. Isso vale sobretudo se você compartilha os assistentes com outros docentes ou se criou um para uma tarefa que se repete todo trimestre.',
        'steps': [
            {'t': 'Usar um nome com tipo e nível', 'b': 'Coloque o tipo de tarefa e o nível no começo do nome, como em "Guia de laboratório · ensino médio". Assim o nome já diz para que o assistente serve.'},
            {'t': 'Descrever para que serve', 'b': 'Acrescente uma frase no próprio assistente explicando o uso dele. Ela ajuda você e outros docentes a usá-lo corretamente meses depois.'},
            {'t': 'Revisar a cada trimestre', 'b': 'Retire os assistentes que você não usa mais, para a lista continuar útil. Um nome sem uso só atrapalha na hora de procurar.'},
        ],
    },
    'configuracion-cuenta': {
        'answer': 'Configurações reúne os ajustes gerais da sua conta, e não os de um curso específico. Use quando quiser revisar os seus dados ou mudar algo que vale para toda a conta. Para mudar algo de um curso, como o código de inscrição, use as Definições desse curso.',
        'steps': [
            {'t': 'Menu da conta', 'b': 'O avatar, embaixo à esquerda, é o ponto de entrada para Configurações e para os outros ajustes da conta.'},
            {'t': 'Configurações', 'b': 'Revise os seus dados e as opções gerais da conta. Faça isso ao começar a usar a ferramenta e sempre que seus dados mudarem.'},
            {'t': 'Voltar ao trabalho', 'b': 'Ao terminar, volte para Conversas ou Cursos e retome o que estava fazendo.'},
        ],
        'tips': ['Não confunda Configurações da conta (avatar) com Definições do curso (dentro de Cursos).'],
    },
    'agregar-material-archivo': {
        'answer': 'Um material com arquivo é uma peça que o estudante pode abrir dentro da seção do curso, como um PDF, uma apresentação ou qualquer documento que você já tenha. Use para deixar os recursos da aula onde os estudantes os procuram, por exemplo uma ficha de apoio junto da atividade. Se preferir, deixe-o oculto até o dia da aula.',
        'steps': [
            {'t': 'Material', 'b': 'Use Material para arquivos que você já tem. Se preferir escrever o conteúdo direto na plataforma, o tipo Texto é o caminho.'},
            {'t': 'Enviar o arquivo', 'b': 'Escolha o arquivo no seu computador. Antes de enviar, confira se é a versão vigente, para não distribuir um material antigo.'},
            {'t': 'Escrever o título', 'b': 'Diga no título o que o arquivo contém, e não apenas o nome dele. "Ficha de apoio: partes da célula" é mais claro que "Doc1".'},
            {'t': 'Adicionar', 'b': 'O material aparece na seção. Se a aula ainda não começou, deixe-o oculto e torne-o visível no dia, como no artigo sobre ocultar conteúdo.'},
        ],
        'example': 'Na terça você explica a célula. Você envia "ficha-apoio-celula.pdf" como material na seção "A célula" e o deixa oculto. Quando começar a aula, torna o material visível, e os estudantes já o têm no curso.',
    },
    'visibilidad-entradas': {
        'answer': 'Ocultar uma entrada faz com que ela não seja vista pelos estudantes, mas continue visível para você na visão geral. Use essa função para preparar o conteúdo com antecedência e liberá-lo no momento certo. Antes de cada aula, confira com "Ver como aluno" o que os estudantes realmente veem.',
        'steps': [
            {'t': 'Identificar as entradas ocultas', 'b': 'A etiqueta "Oculto" aparece na entrada e sinaliza o que os estudantes ainda não veem. Antes de uma aula, confira se nenhum item ficou oculto por engano.'},
            {'t': 'Alterar a visibilidade', 'b': 'Use o menu (…) da entrada para ocultá-la ou torná-la visível de novo. Assim você libera um material no momento da aula, sem precisar recriá-lo.'},
            {'t': 'Conferir com "Ver como aluno"', 'b': 'Essa visão mostra o curso como o estudante o vê e não altera nada. É a forma mais segura de checar o que a turma recebe.'},
            {'t': 'Voltar à sua visão', 'b': 'Saia da visão de estudante para voltar à sua própria visão do curso.'},
        ],
        'tips': ['Se um material parecer sumido para a turma, primeiro confira a etiqueta "Oculto" antes de procurar outro problema.'],
        'example': 'Uma professora de Ciências monta no domingo as seções da semana seguinte. Oculta os materiais de cada aula e, na hora de cada encontro, torna visível o que vai usar. Antes de começar, abre "Ver como aluno" para conferir se a turma vai ver o que deve.',
    },
    'entrega': {
        'answer': 'Uma entrega é uma atividade em que o estudante envia arquivos dentro de um prazo, com título, enunciado, data e hora de entrega. Ela pode bloquear a IA até a data limite, para que o trabalho seja feito sem esse apoio. Use quando quiser receber um trabalho em arquivo e deixar claro o que deve ser entregue e até quando.',
        'steps': [
            {'t': 'Escolher Entrega', 'b': 'A opção descreve que o estudante envia arquivos. Use-a quando o trabalho deve chegar a você como arquivo, e não como uma resposta feita em aula.'},
            {'t': 'Preencher o formulário', 'b': 'Escreva no enunciado o que deve ser feito e comparado, e defina a data e a hora limite. Um enunciado claro reduz perguntas e evita entregas fora do que você pediu.'},
            {'t': 'Bloquear a IA, se precisar', 'b': 'Esta opção só funciona com uma data de entrega. Ative-a quando quiser que o estudante faça o trabalho sem o apoio da IA até o prazo.'},
            {'t': 'Adicionar', 'b': 'A entrega aparece na seção, pronta para os estudantes. Confira o título e o prazo antes de confirmar, pois são os dados que a turma vai ver.'},
        ],
        'tips': ['Para ver de uma vez todas as entregas do curso, use a aba Conteúdos compartilhados.'],
        'example': 'Uma professora de Biologia pede um trabalho sobre célula animal e célula vegetal. Ela cria a entrega com um enunciado sobre o que os estudantes devem desenhar e comparar, define o prazo para 4 de dezembro, às 23:59, e bloqueia a IA até essa data. Quando os arquivos chegam, ela os encontra na seção do trabalho.',
    },
    'invitar-alumnado': {
        'answer': 'Os estudantes podem entrar no curso de três formas: com o código de inscrição e a própria conta, com o link público, sem conta, ou com um convite por e-mail. Escolha a que se encaixa na sua turma, pensando em quem já tem conta e em quanto controle você quer sobre quem entra. Use este artigo para decidir o caminho antes de compartilhar qualquer acesso.',
        'steps': [
            {'t': 'Código de inscrição (com conta)', 'b': 'Indicado quando os estudantes já têm conta no Seven Assistant. Você encontra o código no cartão "Convidar alunos" da visão geral ou em Definições, e o nome usado é o da conta.'},
            {'t': 'Link público (sem conta)', 'b': 'Útil para quem ainda não tem conta. O estudante escreve o seu nome e a primeira letra do sobrenome para entrar, e o link fica ativo enquanto estiver ligado.'},
            {'t': 'Convite por e-mail (com conta)', 'b': 'Serve para convidar uma pessoa específica com o papel que você define. Ela só entra depois de aceitar com a própria conta, e até lá aparece como "Convidado".'},
        ],
        'tips': [
            'Com o link público ativado, qualquer pessoa que o tenha pode entrar: desative-o quando terminar a inscrição.',
            'Convidar por e-mail envia um convite de verdade: confira o endereço antes de clicar em Convidar.',
        ],
        'example': 'Um professor de Química abre o curso para uma turma que está começando agora. Ele compartilha o código de inscrição com quem já tem conta e, para os estudantes que ainda não têm, ativa o link público na primeira semana. Ao final dela, desativa o link.',
    },
    'contenidos-compartidos': {
        'answer': 'A aba Conteúdos compartilhados reúne os materiais, entregas, links e notas do curso, agrupados por seção. Use-a quando quiser ver tudo o que foi publicado no curso de uma vez, sem percorrer seção por seção. Ela é especialmente útil para revisar entregas ou localizar um material pelo nome.',
        'steps': [
            {'t': 'Abrir a aba', 'b': 'Cada seção aparece como uma pasta, com a quantidade de entradas que ela contém. Isso dá uma visão do curso por blocos.'},
            {'t': 'Filtrar por tipo', 'b': 'Escolha entre Todos, Material, Entrega, Link e Nota para ver só um tipo de conteúdo. O filtro Entrega, por exemplo, ajuda a acompanhar os trabalhos recebidos.'},
            {'t': 'Pesquisar ou trocar a visualização', 'b': 'O campo "Pesquisar conteúdos" filtra pelo nome, útil em cursos com muitos itens. Os ícones alternam entre lista e mosaico, sem alterar o conteúdo.'},
            {'t': 'Adicionar conteúdo', 'b': 'O botão "Adicionar" cria um conteúdo novo. Confira em qual seção ele vai ficar antes de confirmar.'},
        ],
        'example': 'Uma professora precisa confirmar quais trabalhos já foram entregues antes de fechar a nota do bimestre. Ela abre a aba Conteúdos compartilhados, filtra por Entrega e percorre as seções para ver o que falta.',
    },
    'exportar-curso': {
        'answer': 'Exportar um curso salva uma cópia completa do conteúdo em um arquivo, no formato que a outra ferramenta precisa. Use para ter uma cópia de segurança antes de arquivar um curso, para levá-lo ao Moodle no formato .mbz ou para reaproveitá-lo em outro sistema compatível com IMS Common Cartridge. Assim você tem como recuperar o conteúdo depois.',
        'steps': [
            {'t': 'Exportação', 'b': 'Fica dentro de Definições, na mesma aba onde você ajusta o curso. Confira antes se o conteúdo já está na versão final, porque o arquivo reflete o que existe no curso naquele momento.'},
            {'t': 'Escolher o formato', 'b': 'Escolha pelo destino do arquivo: o Moodle (.mbz) para o Moodle, o IMS Common Cartridge para outro sistema compatível e o ZIP como opção geral.'},
        ],
        'tips': ['Faça uma cópia de segurança ao terminar o curso, antes de arquivá-lo.'],
        'example': 'Uma professora termina o curso do 9.º ano em dezembro. Ela exporta uma cópia no formato do Moodle (.mbz), guarda o arquivo na pasta da escola e, se precisar do curso no Moodle no ano seguinte, importa o arquivo lá.',
    },
    'enlace-y-nota': {
        'answer': 'Um link e uma nota são materiais leves dentro da seção: o link leva a uma página da web com um título, e a nota é um texto breve que o estudante lê sem abrir mais nada. Use o link para indicar uma referência que deve ser consultada, e a nota para lembrar uma fórmula, um aviso ou um prazo sem criar uma atividade. Por serem leves, eles ajudam a manter a seção organizada sem transformar cada referência em uma atividade.',
        'steps': [
            {'t': 'Link (título e endereço)', 'b': 'Use para referências externas que o estudante precisa consultar. Escreva um título que diga o que é a página, para ele saber o que vai encontrar antes de abrir.'},
            {'t': 'Nota', 'b': 'Serve para o que o estudante precisa lembrar, como uma fórmula ou um aviso. Seja breve, porque a nota é lida direto na seção.'},
            {'t': 'Adicionar', 'b': 'O link ou a nota aparece na seção. Confira se ficou no bloco certo, para o estudante encontrá-lo junto da aula.'},
        ],
    },
    'texto-material': {
        'answer': 'Texto cria um material de leitura em uma página própria da plataforma, com um editor de texto formatado. Use quando quiser escrever a explicação ou a leitura diretamente no curso, sem depender de um arquivo. Com títulos e listas, o texto fica mais fácil de percorrer.',
        'steps': [
            {'t': 'Material de leitura, em página própria', 'b': 'Este tipo cria um texto que o estudante lê na própria plataforma. Use quando o conteúdo for seu e não houver um arquivo pronto.'},
            {'t': 'Escrever o título', 'b': 'O título aparece na seção e ajuda o estudante a identificar a leitura. Seja específico, para diferenciá-la das outras da mesma seção.'},
            {'t': 'Escrever o texto', 'b': 'Use Título 2 e Título 3 para dividir o texto em partes, e listas para sequências de passos. Inserir gráfico ajuda quando um dado precisa ser visto, e não apenas lido.'},
            {'t': 'Adicionar', 'b': 'A leitura aparece na seção com o tipo Texto. Antes de adicioná-la, releia como um estudante faria, para conferir o que ficou claro e o que pode confundir.'},
        ],
        'tips': ['Divida o conteúdo em partes curtas, porque um bloco longo tende a ser lido com menos atenção.'],
        'example': 'Um professor de História quer que a turma entenda a Revolução Industrial antes de uma atividade. Ele escreve uma leitura com o título "Leitura: a Revolução Industrial", com subtítulos por tema e uma lista das causas. Depois adiciona a leitura na seção do tema, e os estudantes a encontram ali, junto da atividade.',
    },
    'no-puedo-acceder': {
        'answer': 'Se você não consegue entrar no Seven Assistant, costuma haver uma causa simples, como um e-mail digitado de forma diferente do cadastro, a senha ou dados antigos do navegador. Use este artigo nessa ordem: confira o e-mail, tente em outro navegador ou janela anônima, redefina a senha e, se ainda não der certo, peça ajuda a quem administra a sua escola. Descartar as causas simples antes de pedir ajuda agiliza a solução.',
        'steps': [
            {'t': 'Conferir o e-mail de acesso', 'b': 'Use o e-mail com o qual você foi cadastrado na escola. Se a escola entra com uma conta institucional, é essa conta que deve ser usada.'},
            {'t': 'Tentar em outro navegador ou em janela anônima', 'b': 'Sair da conta e entrar de novo em uma janela anônima descarta cookies e sessões antigas. Se funcionar ali, o problema estava no navegador habitual.'},
            {'t': 'Redefinir a senha', 'b': 'Se a senha não funcionar, use a opção de recuperação de senha na página de entrada.'},
            {'t': 'Pedir ajuda a quem administra a escola', 'b': 'Se nada der certo, a conta pode não estar ativa ou precisar de um acesso especial. Quem administra a escola pode verificar e liberar o acesso, então leve a ele o que você já tentou.'},
        ],
        'tips': [
            'Se você não tem um e-mail de acesso, peça ao coordenador ou ao administrador da escola um convite.',
            'Se você tinha acesso e de repente o perdeu, avise o administrador: a configuração da escola pode ter mudado.',
        ],
        'example': 'Uma professora de Matemática tenta entrar pelo celular e recebe um erro. Ela confere o e-mail, que é o mesmo do cadastro da escola, e tenta em uma janela anônima no computador. Como funciona ali, ela entende que o problema estava no navegador do celular, e segue o trabalho pelo computador.',
    },
}
