// Tercera tanda: participantes por invitación de correo (probado en la cuenta demo, 17-nov-2026).
export const UPDATE3_ES = {

  'participantes-permisos': { cat: 'cursos', title: 'Participantes: quién tiene acceso al curso', answer: 'En Participantes ves quién tiene acceso al curso, separado en docentes y estudiantes. Las invitaciones que aún no se han aceptado aparecen como "Invitado".',
    steps: [
      { t: 'Abre Participantes', b: 'Verás el buscador, el botón "Invitar a personas" y los filtros Todos, Docentes y Estudiantes, cada uno con su número.' },
      { t: 'Distingue los roles', b: 'Cada persona aparece con su rol: Docente o Estudiante. "Usted" marca tu propio perfil.' },
      { t: 'Comprueba las invitaciones pendientes', b: 'En "Invitaciones" aparecen las personas invitadas por correo, con su rol y la etiqueta "Invitado", hasta que aceptan.' } ],
    tips: ['Para invitar a alguien, consulta "Invitar al alumnado": allí están las tres formas de entrar.'],
    img: ['bio-participantes', 'participantes-tras-invitar'], related: ['invitar-alumnado', 'participantes-citas'] },
};
export const UPDATE3_PT = {
  'participantes-permisos': { cat: 'cursos', title: 'Participantes: quem tem acesso ao curso', answer: 'Em Participantes você vê quem tem acesso ao curso, separado em docentes e estudantes. Os convites que ainda não foram aceitos aparecem como "Convidado".',
    steps: [
      { t: 'Abra Participantes', b: 'Você verá o buscador, o botão "Convidar pessoas" e os filtros Todos, Docentes e Estudantes, cada um com o seu número.' },
      { t: 'Distinga os papéis', b: 'Cada pessoa aparece com o seu papel: Docente ou Estudante. "Você" marca o seu próprio perfil.' },
      { t: 'Confira os convites pendentes', b: 'Em "Convites" aparecem as pessoas convidadas por e-mail, com o seu papel e a etiqueta "Convidado", até que aceitem.' } ],
    tips: ['Para convidar alguém, consulte "Convidar alunos": ali estão as três formas de entrar.'],
    img: ['bio-participantes', 'participantes-tras-invitar'], related: ['invitar-alumnado', 'participantes-citas'] },
};
