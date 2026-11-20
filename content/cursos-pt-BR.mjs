// Cursos, perfis e seções da central de ajuda — Português (Brasil).
// Mesma estrutura, mesmos IDs e mesmas respostas que content/cursos-es.mjs.
// Os nomes de botões em português são traduções: verificar na interface em português antes de publicar.
export default {
  courses: [
    {
      id: 'primeros-pasos',
      slug: 'primeiros-passos',
      title: 'Primeiros passos com o Seven Assistant',
      summary: 'O que é o Seven Assistant, como entrar, escolher o idioma e navegar pela barra lateral desde o primeiro dia.',
      level: 'beginner',
      duration: '20 min',
      audience: ['Professores', 'Coordenação pedagógica', 'Direção de estudos e orientação', 'Responsáveis de TI'],
      roles: ['docente', 'coordinacion', 'jefatura-tutoria', 'responsable-it'],
      objectives: ['Explicar o que o Seven Assistant faz e o que não faz.', 'Mudar o idioma da interface.', 'Localizar cada seção pela barra lateral.'],
      lessons: [
        {
          id: '1.1', slug: 'o-que-e-o-seven-assistant', title: 'O que é o Seven Assistant', duration: '6 min',
          summary: 'A ferramenta, para que serve e como se organiza nas áreas que você vai usar todo dia.',
          objectives: ['Explicar a ferramenta com suas palavras.', 'Identificar as áreas principais da plataforma.'],
          steps: [
            { t: 'Um assistente para o trabalho docente', b: 'O Seven Assistant ajuda você a planejar, criar materiais, redigir e revisar atividades. Ele propõe rascunhos; você decide o que vai para os estudantes.' },
            { t: 'As áreas principais', b: 'Na barra lateral você verá Conversas, Cursos, Biblioteca e Modelos. Cursos reúne os seus cursos. Biblioteca guarda documentos, séries de aulas, tarefas de correção e fichas interativas.' },
            { t: 'O que esperar da fase beta', b: 'A ferramenta Cursos está em beta: algumas telas e opções podem mudar. Esta ajuda é atualizada a cada mudança importante.' },
          ],
          tips: ['Comece por uma necessidade concreta: uma aula da próxima semana, uma rubrica ou uma prova.', 'Revise cada resultado antes de compartilhá-lo com estudantes ou famílias.'],
          quiz: [
            { q: 'Qual é a forma recomendada de usar o que o assistente propõe?', options: ['Publicar do jeito que está, porque já está pronto.', 'Revisar e adaptar à sua turma antes de usar.', 'Usar só se o assistente confirmar que está correto.'], answer: 1, explain: 'O assistente propõe; você valida o conteúdo de acordo com sua turma, seu nível e seu critério.' },
          ],
        },
        {
          id: '1.2', slug: 'sua-conta-e-o-idioma', title: 'Sua conta e o idioma da interface', duration: '6 min',
          summary: 'Como encontrar o menu da conta, mudar o idioma e revisar seu perfil.',
          objectives: ['Abrir o menu da conta.', 'Mudar o idioma da interface.'],
          steps: [
            { t: 'Abra o menu da conta', b: 'Clique no avatar com suas iniciais, na parte de baixo da barra lateral. Ali você encontra Configurações e Idioma.' },
            { t: 'Escolha o idioma', b: 'Em Idioma, escolha espanhol ou português do Brasil para a interface. Os textos que você escreve permanecem no idioma em que foram criados.' },
            { t: 'Revise seu perfil', b: 'Em Configurações, confira seus dados e mantenha-os atualizados se mudar de escola ou de etapa.' },
          ],
          tips: ['Encerre a sessão ao terminar, se usar um computador compartilhado.'],
          quiz: [
            { q: 'Onde você muda o idioma da interface?', options: ['Na barra lateral, com o ícone de Cursos.', 'No menu da conta, dentro de Idioma.', 'Em cada curso, em Definições.'], answer: 1, explain: 'O idioma fica no menu da conta, e não na barra lateral nem dentro de cada curso.' },
          ],
        },
        {
          id: '1.3', slug: 'percurso-pela-interface', title: 'Percurso pela interface', duration: '8 min',
          summary: 'O que há em cada área da barra lateral e onde se cria cada coisa.',
          objectives: ['Escolher a área certa para cada tarefa.', 'Localizar Cursos, Biblioteca e Modelos.'],
          steps: [
            { t: 'Conversas', b: 'É a página inicial e o espaço para perguntar, pedir rascunhos e refinar com o assistente.' },
            { t: 'Cursos', b: 'Aqui você cria cursos, entra em um curso ou o importa. A aba Modelos mostra unidades didáticas que podem ser adotadas.' },
            { t: 'Biblioteca', b: 'Aqui você envia documentos e cria séries de aulas, tarefas de correção e fichas interativas.' },
            { t: 'Modelos', b: 'O ícone de estrelas abre os seus assistentes de IA, com instruções próprias. Não são os modelos de curso.' },
          ],
          tips: ['Se não souber onde trabalhar, pergunte a si mesmo se o resultado será um material, uma conversa ou um curso com estudantes.'],
          quiz: [
            { q: 'Você quer criar um curso com as sessões e os materiais. Por onde começa?', options: ['Em Biblioteca, com Criar rápido.', 'Em Cursos, com Criar curso.', 'Em Modelos, com Criar Plantilla.'], answer: 1, explain: 'Os cursos são criados em Cursos. A Biblioteca guarda materiais avulsos, e Modelos são assistentes de IA.' },
          ],
        },
      ],
    },
    {
      id: 'cursos-crear-organizar',
      slug: 'cursos-criar-e-organizar',
      title: 'Cursos: criar e organizar',
      summary: 'Como criar um curso com o assistente de três passos, organizar o conteúdo em seções e escolher a visualização mais legível.',
      level: 'intermediate',
      duration: '45 min',
      audience: ['Professores', 'Coordenação pedagógica', 'Direção de estudos e orientação'],
      roles: ['docente', 'coordinacion', 'jefatura-tutoria'],
      objectives: ['Criar um curso completo com o assistente.', 'Organizar o conteúdo em seções com uma ordem clara.', 'Escolher a visualização e a navegação do curso.', 'Reaproveitar um curso com modelos.'],
      lessons: [
        {
          id: '2.1', slug: 'o-que-e-um-curso', title: 'O que é um curso no Seven Assistant', duration: '7 min',
          summary: 'Um curso reúne seções, materiais e atividades para uma turma específica, e é compartilhado com os estudantes.',
          objectives: ['Explicar o que um curso contém.', 'Identificar as abas do curso.'],
          steps: [
            { t: 'Um curso para uma turma', b: 'Cada curso é para uma turma e uma disciplina. Dentro há seções, materiais e atividades. Os estudantes entram com um código ou um link.' },
            { t: 'As abas do curso', b: 'Visão geral mostra o conteúdo. Encontros organiza as sessões. Conteúdos compartilhados reúne o que você compartilha. Participantes lista quem faz parte. Definições ajusta o curso.' },
            { t: 'Beta', b: 'A ferramenta Cursos está em beta. Confira as novidades antes de começar um curso longo.' },
          ],
          tips: ['Crie o curso antes do início do período, para ter tempo de revisá-lo.'],
          quiz: [
            { q: 'O que um curso contém?', options: ['Apenas um título e uma data.', 'Seções, materiais e atividades para uma turma.', 'Somente as conversas do professor.'], answer: 1, explain: 'O curso se organiza em seções, com materiais e atividades para a sua turma.' },
          ],
        },
        {
          id: '2.2', slug: 'criar-um-curso-com-o-assistente', title: 'Criar um curso com o assistente de três passos', duration: '10 min',
          summary: 'Dados básicos, conteúdo inicial e revisão: o percurso completo de "Criar curso".',
          objectives: ['Preencher os dados básicos do curso.', 'Escolher o conteúdo inicial.', 'Revisar antes de criar.'],
          steps: [
            { t: 'Passo 1: Dados básicos', b: 'Em Cursos, clique em Criar curso. Escreva o nome do curso, a disciplina, a turma ou série e uma descrição. Você pode adicionar uma capa.' },
            { t: 'Passo 2: Escolher conteúdo', b: 'Escolha como começar: Vazio, Todos os modelos, Copiar ou Planejar com IA. Com Vazio você parte do zero; com um modelo, parte de uma unidade já preparada.' },
            { t: 'Passo 3: Revisar e criar', b: 'Confira os dados. Voltar permite corrigir antes de clicar em Criar.' },
          ],
          tips: ['Use um nome que identifique turma e disciplina, por exemplo "Matemática · 8.º ano".', 'Com Planejar com IA, peça a estrutura por unidades e revise antes de usar.'],
          quiz: [
            { q: 'O que oferece o passo "Escolher conteúdo"?', options: ['Apenas uma capa.', 'Vazio, Todos os modelos, Copiar ou Planejar com IA.', 'A lista de estudantes.'], answer: 1, explain: 'Nesse passo você escolhe por onde começa o conteúdo do curso.' },
          ],
        },
        {
          id: '2.3', slug: 'secoes-e-ordem', title: 'Seções e ordem do conteúdo', duration: '10 min',
          summary: 'Como criar seções, mudar a ordem delas e dar nomes que os estudantes entendam.',
          objectives: ['Criar uma seção.', 'Ordenar o conteúdo.', 'Nomear seções e atividades com clareza.'],
          steps: [
            { t: 'A seção General', b: 'Ao criar um curso aparece a seção General, com o botão Adicionar atividade ou material.' },
            { t: 'Criar seções', b: 'Use Adicionar seção para criar mais seções, por exemplo uma por unidade ou por semana.' },
            { t: 'Ordem', b: 'Organize as seções do conhecido para o novo, e deixe uma aula de revisão antes de cada avaliação.' },
            { t: 'Nomes claros', b: 'Use títulos que digam o que o estudante vai fazer: "Comparar frações com denominadores diferentes" é melhor que "Frações".' },
          ],
          tips: ['Uma seção por unidade é fácil de seguir. Mais de seis seções costuma ser demais para um curso.'],
          quiz: [
            { q: 'Qual botão você usa para criar uma nova seção?', options: ['Adicionar seção.', 'Criar curso.', 'Gerar novo código.'], answer: 0, explain: 'Adicionar seção cria uma nova seção dentro do curso.' },
          ],
        },
        {
          id: '2.4', slug: 'visualizacoes-e-navegacao', title: 'Visualizações do curso e navegação entre conteúdos', duration: '8 min',
          summary: 'Lista, mosaicos e seções como mosaicos: quando usar cada visualização e como ativar a navegação entre conteúdos.',
          objectives: ['Escolher a visualização do curso.', 'Ativar a navegação entre conteúdos.'],
          steps: [
            { t: 'Lista', b: 'Mostra títulos e tipos, um embaixo do outro. É a visualização mais compacta.' },
            { t: 'Lista com pré-visualização', b: 'Mostra as primeiras linhas de cada conteúdo. Útil para revisar sem abrir.' },
            { t: 'Mosaicos e seções como mosaicos', b: 'Mosaicos mostra os conteúdos como cartões. Seções como mosaicos mostra cada seção com a sua própria página.' },
            { t: 'Conteúdo anterior e seguinte', b: 'Se ativar essa opção em Definições, cada página de conteúdo termina com links para o anterior e o seguinte.' },
          ],
          tips: ['Para estudantes do ensino médio, Lista com pré-visualização costuma ser a mais clara.', 'Use "Ver como aluno" para conferir como o curso aparece, sem alterar nada.'],
          quiz: [
            { q: 'Qual visualização mostra cada seção com a sua própria página?', options: ['Lista.', 'Mosaicos.', 'Seções como mosaicos.'], answer: 2, explain: 'Seções como mosaicos leva a uma página para cada seção.' },
          ],
        },
        {
          id: '2.5', slug: 'modelos-copiar-e-importar', title: 'Modelos de curso, copiar e importar', duration: '10 min',
          summary: 'Como adotar uma unidade didática de Modelos, como copiar um curso e como importá-lo de um arquivo.',
          objectives: ['Adotar um modelo de curso.', 'Importar um curso a partir de um arquivo.'],
          steps: [
            { t: 'Modelos de curso', b: 'Em Cursos, abra a aba Modelos. Filtre por país, disciplina, série ou tipo de escola, e clique em Adotar na unidade que precisar.' },
            { t: 'Limitações atuais', b: 'Os modelos atuais são unidades da Espanha, da Alemanha e da Suíça. Adote e adapte ao seu currículo, sem considerá-los válidos sem revisão.' },
            { t: 'Copiar ao criar', b: 'No passo Escolher conteúdo de Criar curso, a opção Copiar reutiliza um curso que você já tem.' },
            { t: 'Importar um curso', b: 'Em Cursos, Importar curso recebe um arquivo do curso e o adiciona à sua lista.' },
          ],
          tips: ['Antes de adotar um modelo, revise as datas e os nomes das atividades.'],
          quiz: [
            { q: 'Onde ficam os modelos de curso?', options: ['Em Modelos, com o ícone de estrelas.', 'Em Cursos, na aba Modelos.', 'Em Biblioteca, com Criar rápido.'], answer: 1, explain: 'Os modelos de curso ficam dentro de Cursos. O ícone de estrelas são assistentes de IA.' },
          ],
        },
      ],
    },
    {
      id: 'cursos-actividades',
      slug: 'cursos-atividades',
      title: 'Cursos: atividades e materiais',
      summary: 'Os tipos de atividade e de material de um curso, quando usar cada um e como escolher conforme o objetivo.',
      level: 'intermediate',
      duration: '50 min',
      audience: ['Professores', 'Coordenação pedagógica'],
      roles: ['docente', 'coordinacion'],
      objectives: ['Distinguir material, atividade e avaliação.', 'Usar cada tipo de atividade com sentido pedagógico.', 'Escolher o tipo adequado para cada objetivo.'],
      lessons: [
        {
          id: '3.1', slug: 'material-e-texto', title: 'Material e texto', duration: '8 min',
          summary: 'Materiais de leitura, arquivos e vídeos para acompanhar a aula, sem avaliação.',
          objectives: ['Enviar um material para uma seção.', 'Escrever um texto de leitura no próprio curso.'],
          steps: [
            { t: 'Material', b: 'Em uma seção, clique em Adicionar atividade ou material e escolha Material: pode ser um arquivo, um vídeo ou um questionário H5P.' },
            { t: 'Texto', b: 'Escolha Texto para um material de leitura que se abre na sua própria página.' },
            { t: 'Quando usar', b: 'Servem para acompanhar a aula: leituras, esquemas ou vídeos. Não são avaliados.' },
          ],
          tips: ['Dê a cada material um título que diga para que serve: "Leitura prévia · ciclo da água".'],
          quiz: [
            { q: 'Qual tipo é para uma leitura que se abre na própria página?', options: ['Nota.', 'Texto.', 'Entrega.'], answer: 1, explain: 'Texto cria um material de leitura em uma página própria.' },
          ],
        },
        {
          id: '3.2', slug: 'ficha-de-trabalho-e-unidade', title: 'Ficha de trabalho e unidade didática', duration: '10 min',
          summary: 'A ficha de trabalho para praticar e a unidade didática para levar uma unidade completa ao curso.',
          objectives: ['Adicionar uma ficha de trabalho.', 'Adicionar uma unidade didática completa.'],
          steps: [
            { t: 'Ficha de trabalho', b: 'Escolha Ficha de trabalho para adicionar uma folha de exercícios ao curso. Serve para treinar em aula ou em casa.' },
            { t: 'Unidade didática', b: 'Escolha Unidade didática para adicionar uma unidade completa, com seu conteúdo, à seção.' },
            { t: 'Revisão', b: 'Depois de adicionar, revise se os títulos e a ordem fazem sentido para o estudante.' },
          ],
          tips: ['Use a ficha de trabalho para prática e a unidade para planejar um bloco inteiro.'],
          quiz: [
            { q: 'Para que serve uma ficha de trabalho no curso?', options: ['Para cobrar uma taxa.', 'Para treinar com exercícios.', 'Para criar o curso.'], answer: 1, explain: 'A ficha de trabalho é um material de treino com exercícios.' },
          ],
        },
        {
          id: '3.3', slug: 'tarefa-com-comentarios-e-entrega', title: 'Tarefa com comentários e entrega', duration: '12 min',
          summary: 'Quando usar uma tarefa com comentários e quando usar uma entrega, e como receber o trabalho dos estudantes.',
          objectives: ['Diferenciar tarefa com comentários e entrega.', 'Configurar a data e a hora de entrega.'],
          steps: [
            { t: 'Tarefa com comentários', b: 'É uma tarefa que pode receber comentários da IA, conforme a configuração. Use quando quiser devolutiva sobre o trabalho.' },
            { t: 'Entrega', b: 'Os estudantes enviam arquivos em uma entrega. Ela tem título, descrição, data e hora limite.' },
            { t: 'Data e hora', b: 'Defina a data e a hora limite ao criar a entrega. Revise antes de publicar.' },
            { t: 'Qual usar', b: 'Use uma entrega quando há um arquivo a receber. Use uma tarefa com comentários quando quiser devolutiva sobre o trabalho.' },
          ],
          tips: ['Escreva na descrição o que o estudante deve entregar e em que formato.'],
          quiz: [
            { q: 'Qual tipo recebe arquivos dos estudantes?', options: ['Nota.', 'Entrega.', 'Texto.'], answer: 1, explain: 'A entrega é o tipo pensado para que os estudantes enviem arquivos.' },
          ],
        },
        {
          id: '3.4', slug: 'agente-link-e-nota', title: 'Agente de IA, link e nota', duration: '10 min',
          summary: 'Um agente de IA para os estudantes, um link para um recurso externo e uma nota breve dentro da seção.',
          objectives: ['Criar um agente de IA para o curso.', 'Adicionar um link e uma nota.'],
          steps: [
            { t: 'Agente de IA', b: 'Escolha Agente de IA para disponibilizar aos estudantes um assistente com instruções suas. Escreva o nome e as instruções.' },
            { t: 'Link', b: 'Escolha Link para apontar para uma página da web. Escreva o texto que o estudante verá e o endereço.' },
            { t: 'Nota', b: 'Escolha Nota para um texto breve diretamente na seção, por exemplo um aviso ou uma instrução.' },
          ],
          tips: ['Um agente de IA para estudantes precisa de instruções claras: que ajuda oferecer e o que não deve resolver diretamente.'],
          quiz: [
            { q: 'Qual tipo adiciona um texto breve diretamente na seção?', options: ['Link.', 'Nota.', 'Agente de IA.'], answer: 1, explain: 'A nota é um texto breve dentro da seção.' },
          ],
        },
        {
          id: '3.5', slug: 'escolher-o-tipo-de-atividade', title: 'Como escolher o tipo de atividade', duration: '8 min',
          summary: 'Um guia para decidir entre material, prática, tarefa e entrega conforme o objetivo que você quer verificar.',
          objectives: ['Escolher o tipo conforme o objetivo.', 'Não usar uma entrega para o que é prática.'],
          steps: [
            { t: 'Quero que o estudante leia ou veja algo', b: 'Material ou Texto.' },
            { t: 'Quero que ele pratique', b: 'Ficha de trabalho.' },
            { t: 'Quero que ele me entregue um arquivo', b: 'Entrega.' },
            { t: 'Quero devolutiva sobre o trabalho', b: 'Tarefa com comentários.' },
            { t: 'Quero um assistente para as dúvidas dele', b: 'Agente de IA, com instruções claras.' },
          ],
          tips: ['Se a atividade não é avaliada nem corrigida, provavelmente é prática ou material.'],
          quiz: [
            { q: 'Você quer que o estudante pratique exercícios. Que tipo escolhe?', options: ['Entrega.', 'Ficha de trabalho.', 'Link.'], answer: 1, explain: 'A ficha de trabalho é o tipo pensado para praticar.' },
          ],
        },
      ],
    },
    {
      id: 'cursos-compartir-seguimiento',
      slug: 'cursos-compartilhar-e-acompanhar',
      title: 'Cursos: compartilhar e acompanhar',
      summary: 'Como convidar os estudantes com código ou link, o que podem fazer com a IA, como ver o curso como estudante e como acompanhar a turma.',
      level: 'intermediate',
      duration: '40 min',
      audience: ['Professores', 'Coordenação pedagógica', 'Direção de estudos e orientação', 'Responsáveis de TI'],
      roles: ['docente', 'coordinacion', 'jefatura-tutoria', 'responsable-it'],
      objectives: ['Convidar alunos com código ou link.', 'Decidir o uso da IA pelos estudantes.', 'Revisar o curso como o estudante o vê.', 'Acompanhar a turma com participantes e encontros.'],
      lessons: [
        {
          id: '4.1', slug: 'codigo-e-link-de-inscricao', title: 'Código e link de inscrição', duration: '8 min',
          summary: 'Como compartilhar um curso com os estudantes e quando vale gerar um código novo.',
          objectives: ['Compartilhar o código e o link.', 'Gerar um código novo, se necessário.'],
          steps: [
            { t: 'O código', b: 'Na visão geral do curso aparece o código de inscrição. O estudante o digita em Entrar em um curso.' },
            { t: 'O link público', b: 'O link de inscrição deixa entrar quem tiver o link, sem conta, apenas com um nome.' },
            { t: 'Gerar um código novo', b: 'Se o link vazar ou a turma mudar, clique em Gerar novo código. O link anterior deixa de funcionar.' },
          ],
          tips: ['Compartilhe o link apenas com a turma. Se for um curso da escola, combine com a coordenação antes de publicar.'],
          quiz: [
            { q: 'O link vazou para pessoas que não são da turma. O que você faz?', options: ['Nada: o link não pode ser trocado.', 'Clicar em Gerar novo código.', 'Excluir o curso.'], answer: 1, explain: 'Gerar novo código substitui o acesso anterior sem excluir o curso.' },
          ],
        },
        {
          id: '4.2', slug: 'entrar-em-um-curso', title: 'Entrar em um curso (visão do estudante)', duration: '6 min',
          summary: 'O que o estudante vê ao entrar com um código e como conferir isso pela visão de estudante.',
          objectives: ['Explicar ao estudante como entrar.', 'Conferir o curso pela visão de estudante.'],
          steps: [
            { t: 'Entrar em um curso', b: 'O estudante vai em Cursos e escolhe Entrar em um curso. Digita o código de inscrição.' },
            { t: 'Visão de estudante', b: 'Com Ver como aluno você vê o curso como o estudante o vê. Aparece o aviso "Aqui não se muda nada".' },
            { t: 'Sair da visão', b: 'Clique em Sair da visão para voltar à sua visão de professor.' },
          ],
          tips: ['Faça o teste com a visão de estudante antes da primeira aula.'],
          quiz: [
            { q: 'O que a visão de estudante permite conferir?', options: ['Como o curso aparece para o estudante, sem alterar nada.', 'As notas de cada aluno.', 'O código de outro curso.'], answer: 0, explain: 'A visão de estudante mostra o curso como o estudante o vê, sem alterar nada.' },
          ],
        },
        {
          id: '4.3', slug: 'ia-para-os-estudantes', title: 'IA para os estudantes e Tutor de IA', duration: '10 min',
          summary: 'Como ativar a IA para os estudantes e o que faz o Tutor de IA: dicas e perguntas, sem resolver tudo.',
          objectives: ['Ativar ou desativar a IA para os estudantes.', 'Explicar o que faz o Tutor de IA.'],
          steps: [
            { t: 'IA para os estudantes', b: 'É uma chave do curso. Se estiver ativa, os estudantes podem perguntar à IA sobre o conteúdo do curso.' },
            { t: 'O que o professor sempre pode usar', b: 'O professor pode usar a IA do curso mesmo que os estudantes não a tenham ativada.' },
            { t: 'Tutor de IA', b: 'O Tutor de IA dá dicas e faz perguntas, mas não dá a solução completa. É útil para que o estudante raciocine.' },
          ],
          tips: ['Explique aos estudantes para que serve o tutor e que tipo de ajuda esperar.', 'Revise algumas conversas dos estudantes para identificar dúvidas comuns.'],
          quiz: [
            { q: 'O que o Tutor de IA oferece ao estudante?', options: ['A solução completa do exercício.', 'Dicas e perguntas, sem a solução completa.', 'A nota do trabalho.'], answer: 1, explain: 'O Tutor de IA foi pensado para orientar o raciocínio, não para dar respostas completas.' },
          ],
        },
        {
          id: '4.4', slug: 'participantes-conteudos-e-encontros', title: 'Participantes, conteúdos compartilhados e encontros', duration: '12 min',
          summary: 'O acompanhamento do curso: quem participa, quais materiais você compartilha e como organizar os encontros com a turma.',
          objectives: ['Revisar os participantes do curso.', 'Gerenciar os conteúdos compartilhados.', 'Criar um encontro do curso.'],
          steps: [
            { t: 'Participantes', b: 'A aba Participantes mostra quem faz parte do curso. Revise no início e no fim.' },
            { t: 'Conteúdos compartilhados', b: 'A aba Conteúdos compartilhados reúne o que você compartilha. Em Adicionar, você inclui materiais.' },
            { t: 'Encontros', b: 'A aba Encontros mostra os próximos. Criar encontro adiciona uma sessão com data, para que a turma a veja no curso.' },
          ],
          tips: ['Revise os participantes toda semana nas primeiras semanas do curso.'],
          quiz: [
            { q: 'Onde você organiza as sessões com data?', options: ['Em Participantes.', 'Em Encontros.', 'Nas configurações do menu da conta.'], answer: 1, explain: 'Os encontros do curso são gerenciados na aba Encontros.' },
          ],
        },
      ],
    },
    {
      id: 'biblioteca-asistente',
      slug: 'biblioteca-assistente',
      title: 'Conversas, Biblioteca e Modelos',
      summary: 'Como conversar com o assistente, enviar documentos, criar séries de aulas, fichas interativas, tarefas de correção e assistentes de IA.',
      level: 'intermediate',
      duration: '55 min',
      audience: ['Professores', 'Coordenação pedagógica', 'Direção de estudos e orientação'],
      roles: ['docente', 'coordinacion', 'jefatura-tutoria'],
      objectives: ['Usar Conversas e as suas ferramentas.', 'Enviar documentos e criar séries de aulas.', 'Criar fichas interativas e tarefas de correção.', 'Criar assistentes de IA em Modelos.'],
      lessons: [
        {
          id: '5.1', slug: 'conversas-e-ferramentas', title: 'Conversas e ferramentas do assistente', duration: '10 min',
          summary: 'A página inicial, o campo de escrita, o modo Dinâmico e as ferramentas do assistente.',
          objectives: ['Escrever um pedido com contexto.', 'Usar uma ferramenta do assistente.', 'Gerar a resposta de novo.'],
          steps: [
            { t: 'A página inicial', b: 'Conversas é a página inicial. Escreva no campo "Pergunte qualquer coisa" e envie.' },
            { t: 'As ferramentas', b: 'Com o botão + você usa ferramentas como Série de aulas, Ficha de trabalho, Diferenciação, Correção ou Texto de áudio.' },
            { t: 'Contexto', b: 'Indique país, etapa, ano, disciplina e tempo. Com esse contexto, a resposta se encaixa na sua turma.' },
            { t: 'Gerar de novo', b: 'Se uma resposta não convencer, você pode gerá-la de novo. O assistente nem sempre acerta: revise sempre o resultado.' },
          ],
          tips: ['Prefira a ferramenta adequada a uma pergunta longa: Série de aulas para planejar, Ficha de trabalho para praticar.'],
          quiz: [
            { q: 'Qual ferramenta do assistente serve para planejar uma sequência de aulas?', options: ['Série de aulas.', 'Texto de áudio.', 'Busca na web.'], answer: 0, explain: 'Série de aulas é pensada para planejar aulas e sequências.' },
          ],
        },
        {
          id: '5.2', slug: 'biblioteca-documentos-e-series', title: 'Biblioteca: documentos e séries de aulas', duration: '12 min',
          summary: 'Enviar documentos para a Biblioteca e criar uma série de aulas com tema, disciplina, curso e idioma.',
          objectives: ['Enviar um documento.', 'Criar uma série de aulas.'],
          steps: [
            { t: 'Biblioteca', b: 'Entre em Biblioteca. Criar rápido mostra Enviar documento, Série de aulas, Tarefa de correção e feedback e Ficha interativa.' },
            { t: 'Enviar documento', b: 'Clique em Enviar documento. Aceita PDF, vídeo ou página da web. Os documentos aparecem em Minha biblioteca.' },
            { t: 'Série de aulas', b: 'Clique em Série de aulas e depois em Criar. Preencha Tema, que é obrigatório, e Disciplina, Curso, Idioma e Descrição. Você também pode usar Gerar com IA.' },
            { t: 'Revisão', b: 'Revise a série antes de usar: as sessões precisam fazer sentido e a avaliação deve estar marcada.' },
          ],
          tips: ['Use um tema concreto: "Proporcionalidade direta · 8.º ano" gera séries melhores que "Matemática".'],
          quiz: [
            { q: 'Qual campo é obrigatório ao criar uma série de aulas?', options: ['Descrição.', 'Tema.', 'Idioma.'], answer: 1, explain: 'O tema é o único campo marcado como obrigatório.' },
          ],
        },
        {
          id: '5.3', slug: 'fichas-interativas', title: 'Fichas interativas: criar folha de trabalho', duration: '12 min',
          summary: 'O assistente de três passos para criar uma ficha interativa: contexto, fontes e análise com ajustes.',
          objectives: ['Configurar o contexto da ficha.', 'Escolher a extensão e a densidade do texto.', 'Revisar a ficha antes de usar.'],
          steps: [
            { t: 'Criar folha de trabalho', b: 'Em Biblioteca, clique em Ficha interativa. Abre-se Criar folha de trabalho, em três passos: Contexto, Fontes e Análise e ajuste.' },
            { t: 'Contexto', b: 'Indique Tema, Disciplina, Nível escolar, Nível de dificuldade, Idioma e a extensão: teste curto, folha de exercícios, material de apoio ou prova.' },
            { t: 'Fontes', b: 'Indique de onde vem o conteúdo da ficha.' },
            { t: 'Análise e ajuste', b: 'Revise o número de exercícios e a densidade do texto: compacta, equilibrada ou detalhada. Depois gere a ficha.' },
          ],
          tips: ['Para crianças pequenas ou estudantes com apoio, use densidade compacta e um nível de dificuldade baixo.'],
          quiz: [
            { q: 'Qual é o primeiro passo de Criar folha de trabalho?', options: ['Contexto.', 'Análise e ajuste.', 'Fontes.'], answer: 0, explain: 'O primeiro passo é Contexto, onde você define o tema, a disciplina e o nível.' },
          ],
        },
        {
          id: '5.4', slug: 'tarefas-de-correcao-e-feedback', title: 'Tarefas de correção e feedback', duration: '12 min',
          summary: 'Criar uma tarefa de correção e feedback pela Biblioteca, com critérios claros e revisão da proposta.',
          objectives: ['Criar uma tarefa de correção.', 'Definir critérios observáveis.', 'Revisar a correção antes de fechá-la.'],
          steps: [
            { t: 'Tarefa de correção e feedback', b: 'Em Biblioteca, clique em Tarefa de correção e feedback. Criar cria uma tarefa e Gerar com IA a propõe a partir do seu pedido.' },
            { t: 'Critérios', b: 'Escreva critérios que possam ser verificados no trabalho: "Argumenta com pelo menos duas evidências" é melhor que "boa redação".' },
            { t: 'Correção', b: 'A plataforma pode corrigir com comentários por critério. Revise cada comentário antes de dar a nota.' },
            { t: 'Calibrar', b: 'Compare a proposta com dois ou três trabalhos corrigidos por você. Assim você ajusta os critérios antes de corrigir a turma.' },
          ],
          tips: ['Revise pessoalmente os casos limite antes de fechar as notas.'],
          quiz: [
            { q: 'O que convém fazer antes de corrigir a turma inteira?', options: ['Publicar as notas.', 'Calibrar com alguns trabalhos de níveis diferentes.', 'Apagar os critérios.'], answer: 1, explain: 'Calibrar evita que a mesma escala seja aplicada de forma diferente em cada trabalho.' },
          ],
        },
        {
          id: '5.5', slug: 'modelos-de-assistente', title: 'Modelos: criar o seu assistente de IA', duration: '10 min',
          summary: 'Modelos é a seção de assistentes de IA com instruções próprias. Aqui você aprende a criar um.',
          objectives: ['Distinguir assistentes de IA e modelos de curso.', 'Criar um assistente com as suas instruções.'],
          steps: [
            { t: 'O que é um modelo de assistente', b: 'É um assistente de IA com instruções próprias, para repetir um pedido nas suas aulas.' },
            { t: 'Criar Plantilla', b: 'Em Modelos, clique em Criar Plantilla. A tela vazia mostra Criar Plantilla ou Nuevo Plantilla quando você já tiver algum.' },
            { t: 'Instruções', b: 'Descreva o papel do assistente, o tipo de resposta e o que ele não deve fazer. Quanto mais concretas, mais útil.' },
            { t: 'Revisão', b: 'Teste o assistente com um pedido real e ajuste as instruções se a resposta não se encaixar.' },
          ],
          tips: ['Não confunda este assistente com os modelos de curso em Cursos → Modelos.'],
          quiz: [
            { q: 'O que o botão Criar Plantilla cria?', options: ['Um curso completo.', 'Um assistente de IA com instruções próprias.', 'Uma lista de estudantes.'], answer: 1, explain: 'Em Modelos são criados assistentes de IA com instruções próprias.' },
          ],
        },
      ],
    },
    {
      id: 'administracion-it',
      slug: 'administracao-de-ti',
      title: 'Administração para responsáveis de TI',
      summary: 'Organize a escola, gerencie participantes e pastas compartilhadas, e revise segurança e privacidade. Este curso não trata de criar conteúdos.',
      level: 'advanced',
      duration: '40 min',
      audience: ['Responsáveis de TI', 'Coordenação pedagógica'],
      roles: ['responsable-it', 'coordinacion'],
      objectives: ['Organizar a escola e os planos de estudo.', 'Gerenciar participantes e permissões.', 'Gerenciar pastas compartilhadas.', 'Revisar segurança, privacidade e localização dos dados.'],
      lessons: [
        {
          id: '6.1', slug: 'organizacao-e-planos-de-estudo', title: 'Organização da escola e planos de estudo', duration: '10 min',
          summary: 'Como estruturar os cursos da escola para que sejam fáceis de encontrar e de governar.',
          objectives: ['Definir um modelo de organização.', 'Combinar nomes comuns de disciplina e série.'],
          steps: [
            { t: 'Modelo de organização', b: 'Cada curso tem uma disciplina e uma turma ou série, preenchidas ao criar o curso.' },
            { t: 'Nomes comuns', b: 'Antes de os professores criarem cursos, combine as disciplinas e as séries da escola, para usar os mesmos nomes.' },
            { t: 'Convenção de títulos', b: 'Defina um formato, por exemplo "Matemática · 8.º ano · 2026".' },
            { t: 'Revisão anual', b: 'Ao fechar cada ano letivo, revise os cursos e reorganize os nomes para o seguinte.' },
          ],
          tips: ['Documente a convenção em um único lugar e compartilhe com a coordenação e os professores.'],
          quiz: [
            { q: 'Quais campos são preenchidos ao criar um curso e ajudam a organizar a escola?', options: ['Disciplina e turma ou série.', 'Apenas a cor da capa.', 'A senha da turma.'], answer: 0, explain: 'Disciplina e turma ou série são a base da organização da escola.' },
          ],
        },
        {
          id: '6.2', slug: 'participantes-e-permissoes', title: 'Participantes e permissões', duration: '10 min',
          summary: 'Quem participa de cada curso e o que cada pessoa precisa, aplicando o mínimo necessário.',
          objectives: ['Aplicar o mínimo privilégio.', 'Revisar os participantes de um curso.', 'Manter entradas, saídas e revisões.'],
          steps: [
            { t: 'Mínimo privilégio', b: 'Dê a cada pessoa as permissões necessárias para a sua função, e nada além disso.' },
            { t: 'Participantes do curso', b: 'A aba Participantes de cada curso mostra quem faz parte. Revise no início e no fim do curso.' },
            { t: 'Entradas e saídas', b: 'Quando uma pessoa entra ou sai da escola, atualize o acesso no mesmo dia.' },
            { t: 'Revisão periódica', b: 'Revise a cada trimestre os participantes e as pastas compartilhadas com a direção.' },
          ],
          tips: ['Evite contas compartilhadas entre várias pessoas: você perde a rastreabilidade.'],
          quiz: [
            { q: 'Que princípio orienta a atribuição de permissões?', options: ['Dar acesso total a todos.', 'O mínimo necessário para cada função.', 'Dar permissões só à direção.'], answer: 1, explain: 'Limitar as permissões ao necessário reduz o impacto de um erro ou de uma conta comprometida.' },
          ],
        },
        {
          id: '6.3', slug: 'pastas-compartilhadas-e-token', title: 'Pastas compartilhadas e acesso com token', duration: '8 min',
          summary: 'Como criar uma pasta compartilhada e como entrar em uma com um token de acesso.',
          objectives: ['Criar uma pasta compartilhada.', 'Entrar em uma pasta com token.'],
          steps: [
            { t: 'Gerenciar pastas compartilhadas', b: 'Fica no menu da conta. Daí você cria uma pasta com Nova pasta.' },
            { t: 'Entrar com token', b: 'Se alguém lhe deu um token de acesso, digite-o em Entrar em pasta com token de acesso e clique em Entrar.' },
            { t: 'Revisar o acesso', b: 'Confira periodicamente quem está em cada pasta e retire o acesso de quem não deve mais tê-lo.' },
          ],
          tips: ['Não compartilhe um token por canais públicos: trate-o como uma senha.'],
          quiz: [
            { q: 'Alguém lhe deu um token de acesso a uma pasta. Onde você o digita?', options: ['Em Entrar em pasta com token de acesso.', 'No campo de busca da Biblioteca.', 'Na visão geral do curso.'], answer: 0, explain: 'Os tokens são usados em Entrar em pasta com token de acesso, no menu da conta.' },
          ],
        },
        {
          id: '6.4', slug: 'seguranca-privacidade-e-dados', title: 'Segurança, privacidade e localização dos dados', duration: '12 min',
          summary: 'O que você deve conseguir responder sobre segurança e privacidade, e como documentar isso para a direção e as famílias.',
          objectives: ['Responder às perguntas básicas sobre dados.', 'Minimizar dados pessoais dos estudantes.', 'Ter um procedimento para incidentes.'],
          steps: [
            { t: 'Perguntas básicas', b: 'Onde os dados ficam armazenados? Quem pode acessá-los? Como são protegidos? Como são eliminados? Quais dados pessoais são tratados?' },
            { t: 'Documentação oficial', b: 'Consulte a documentação de segurança e privacidade publicada pelo Seven Assistant e guarde a versão vigente na pasta de conformidade da escola.' },
            { t: 'Minimize os dados', b: 'Use identificadores internos em vez de nomes completos sempre que possível, e defina quem pode exportar dados.' },
            { t: 'Conformidade local', b: 'Brasil (LGPD), México (LFPDPPP) e Chile (sua legislação de dados pessoais, em atualização) têm exigências próprias. Consulte o jurídico.' },
            { t: 'Incidentes', b: 'Defina quem avisar se uma conta for comprometida e em quanto tempo.' },
          ],
          tips: ['Documente uma vez e revise a cada ano: uma ficha de uma página é mais útil do que uma busca em plena crise.'],
          quiz: [
            { q: 'Qual prática reduz mais o risco com dados dos estudantes?', options: ['Usar nomes completos para facilitar buscas.', 'Minimizar dados e usar identificadores internos.', 'Compartilhar a senha de administração.'], answer: 1, explain: 'Quanto menos dados identificáveis circulam, menor é o impacto de um incidente.' },
          ],
        },
      ],
    },
  ],
  roles: {
    docente: { name: 'Professor(a)', description: 'Planeja, cria cursos e materiais e corrige com critérios claros. Sua trilha combina cursos, conversas, biblioteca e avaliação.', lessons: ['1.1', '1.2', '1.3', '2.2', '3.5', '4.1', '5.1', '5.3', '5.4'] },
    coordinacion: { name: 'Coordenação pedagógica', description: 'Acompanha cursos, planos e escalas do nível. Sua trilha inclui o desenho de cursos, participantes e organização.', lessons: ['1.1', '1.2', '2.1', '2.4', '4.4', '5.2', '6.1', '6.2'] },
    'jefatura-tutoria': { name: 'Direção de estudos e orientação', description: 'Acompanha turmas e avaliações e apoia o corpo docente. Sua trilha inclui IA para os estudantes, participantes e correção.', lessons: ['1.1', '1.3', '4.3', '4.4', '5.1', '5.4'] },
    'responsable-it': { name: 'Responsável de TI', description: 'Organiza a escola, gerencia participantes e pastas compartilhadas, e revisa segurança e privacidade. Você não precisa criar conteúdos para esta trilha.', lessons: ['1.1', '1.2', '4.4', '6.1', '6.2', '6.3', '6.4'] },
  },
  sections: {
    cursos: { name: 'Cursos', short: 'Crie cursos, organize o conteúdo e compartilhe com os estudantes.', summary: 'Cursos é a ferramenta para criar um curso completo: dados básicos, seções, materiais e atividades, e compartilhá-lo com os estudantes. Está em beta.', whenToUse: ['Ao planejar uma unidade ou um trimestre com uma turma.', 'Quando quer que os estudantes entrem em um curso com código ou link.', 'Para acompanhar a turma em participantes e encontros.'], basics: ['Onde fica: barra lateral, ícone Cursos.', 'Crie o curso com o assistente de três passos.', 'Organize o curso em seções e adicione atividades ou materiais.', 'Compartilhe com código ou link.'], lessons: ['2.1', '2.2', '2.3', '2.4', '2.5', '3.5', '4.1', '4.4'] },
    conversaciones: { name: 'Conversas', short: 'Pergunte, peça rascunhos e refine com o assistente.', summary: 'Conversas é a página inicial e o espaço para dialogar com o assistente. As ferramentas do botão + ajudam a planejar, treinar e corrigir.', whenToUse: ['Para pensar uma aula ou buscar ideias de atividades.', 'Para revisar um texto que você escreveu.', 'Para preparar comunicados às famílias.'], basics: ['Onde fica: página inicial (ícone de chat).', 'Dê contexto: país, etapa, ano, disciplina e tempo.', 'Use o botão + para ferramentas como Série de aulas.', 'Gere a resposta de novo se ela não convencer.'], lessons: ['5.1'] },
    documentos: { name: 'Documentos', short: 'Envie documentos e organize-os na Biblioteca.', summary: 'Os documentos ficam na Biblioteca, em Minha biblioteca. Você pode enviar PDF, vídeos ou páginas da web.', whenToUse: ['Quando o material deve ficar guardado para usar depois.', 'Quando outra pessoa precisa ler o material.'], basics: ['Onde fica: Biblioteca, Minha biblioteca.', 'Envie com Enviar documento: PDF, vídeo ou página da web.', 'Nomeie os arquivos com disciplina, turma e data.'], lessons: ['5.2'] },
    'series-de-lecciones': { name: 'Séries de aulas', short: 'Crie sequências de sessões com progressão e avaliação.', summary: 'Uma série de aulas reúne várias sessões com um mesmo objetivo. É criada na Biblioteca, com Tema, Disciplina, Curso, Idioma e Descrição.', whenToUse: ['Para uma sequência de 4 a 10 sessões sobre um mesmo tema.', 'Para adaptar a mesma progressão a várias turmas.'], basics: ['Onde fica: Biblioteca, Série de aulas.', 'Preencha Tema (obrigatório) e os demais campos, ou use Gerar com IA.', 'Ordene as sessões do simples para o complexo.', 'Indique na descrição onde estão as avaliações.'], lessons: ['5.2'] },
    'tareas-de-correccion': { name: 'Tarefa de correção e feedback', short: 'Corrija trabalhos com critérios e devolutiva.', summary: 'A tarefa de correção e feedback é criada na Biblioteca. Você define critérios, calibra com alguns trabalhos e revisa a proposta antes de fechar as notas.', whenToUse: ['Para redações, problemas ou projetos com vários critérios.', 'Quando quer devolutiva específica para cada estudante.'], basics: ['Onde fica: Biblioteca, Tarefa de correção e feedback.', 'Defina critérios observáveis.', 'Calibre com trabalhos de níveis diferentes antes de corrigir tudo.', 'Revise a devolutiva antes de publicá-la.'], lessons: ['5.4'] },
    'fichas-interactivas': { name: 'Fichas interativas', short: 'Crie folhas de trabalho com contexto, fontes e ajustes.', summary: 'As fichas interativas são criadas na Biblioteca com Criar folha de trabalho, em três passos: Contexto, Fontes e Análise e ajuste.', whenToUse: ['Para treinar em aula ou em casa.', 'Para revisar antes de uma avaliação.', 'Para atender ritmos diferentes.'], basics: ['Onde fica: Biblioteca, Ficha interativa.', 'Configure Contexto, Fontes e Análise e ajuste.', 'Comece com uma extensão curta.', 'Revise a ficha antes de compartilhá-la.'], lessons: ['5.3'] },
    plantillas: { name: 'Modelos', short: 'Assistentes de IA com instruções próprias, e modelos de curso.', summary: 'Modelos é a seção de assistentes de IA com instruções próprias. Os modelos de curso ficam dentro de Cursos.', whenToUse: ['Quando você repete o mesmo pedido toda semana.', 'Quando quer adotar uma unidade didática pronta.'], basics: ['Assistentes de IA: ícone de estrelas; Criar Plantilla define as instruções.', 'Modelos de curso: Cursos, aba Modelos.', 'Nomeie cada modelo com tipo e etapa.'], lessons: ['2.5', '5.5'] },
    configuracion: { name: 'Configurações', short: 'Idioma da interface e preferências da sua conta.', summary: 'Configurações e o idioma ficam no menu da conta, no avatar da sua conta, na parte de baixo da barra lateral.', whenToUse: ['Ao começar a usar a plataforma.', 'Quando muda de etapa ou de escola.', 'Quando outra pessoa precisa trabalhar no idioma dela.'], basics: ['Onde fica: menu da conta (avatar, embaixo à esquerda).', 'Idioma: no mesmo menu.', 'Mantenha seu perfil atualizado.'], lessons: ['1.2'] },
  },
};
