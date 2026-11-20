// Genera un único HTML autocontenido del centro de ayuda (artículos en ES y PT-BR), sin servidor.
// Uso: node single/build-single.mjs  ->  single/centro-ayuda.html
import { readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const load = async (rel) => (await import(pathToFileURL(path.join(ROOT, rel)).href)).default;
const ES = await load('content/articulos-es.mjs');
const PT = await load('content/articulos-pt-BR.mjs');
import { UPDATE as UPD_ES, NEW_ES } from '../content/ayuda-actualizaciones-es.mjs';
import { UPDATE2 as UPD2_ES } from '../content/ayuda-actualizaciones-2-es.mjs';
import { UPDATE2 as UPD2_PT } from '../content/ayuda-actualizaciones-2-pt-BR.mjs';
import { UPDATE3_ES as UPD3_ES, UPDATE3_PT as UPD3_PT } from '../content/ayuda-actualizaciones-3.mjs';
import { UPDATE as UPD_PT, NEW_PT } from '../content/ayuda-actualizaciones-pt-BR.mjs';
function mergeArticles(base, upd, news) {
  const list = base.articles.map((a) => ({ ...a }));
  for (const [id, fields] of Object.entries(upd)) {
    const i = list.findIndex((a) => a.id === id);
    if (i >= 0) list[i] = { ...list[i], ...fields, id };
    else list.push({ id, steps: [], tips: [], img: [], related: [], ...fields });
  }
  for (const n of news) {
    if (!list.some((a) => a.id === n.id)) list.push({ tips: [], img: [], related: [], ...n });
    else list[list.findIndex((a) => a.id === n.id)] = { ...list.find((a) => a.id === n.id), ...n };
  }
  return { ...base, articles: list };
}

const ES_M = mergeArticles(mergeArticles(mergeArticles(ES, UPD_ES, NEW_ES), UPD2_ES, []), UPD3_ES, []);
const PT_M = mergeArticles(mergeArticles(mergeArticles(PT, UPD_PT, NEW_PT), UPD2_PT, []), UPD3_PT, []);


// Capturas por idioma: cada idioma muestra su propia interfaz (ES en español, PT en portugués de la aplicación).
const IMG_OVERRIDE = {
  es: { 'participantes-citas': ['es-cita-pestana', 'es-cita-formulario', 'es-cita-guardada'], 'invitar-alumnado': ['es-invitar-tarjeta'], 'hacer-pregunta': ['es-conversa-inicio', 'es-conversa-respuesta'], 'serie-de-lecciones': ['es-serie-lista', 'es-serie-completo'], 'tarea-correccion-biblioteca': ['es-tarea-lista', 'es-tarea-formulario'], 'crear-asistente': ['es-asistente-formulario', 'es-asistente-guardado'] },
  pt: { 'participantes-citas': ['pt-cita-pestana', 'pt-cita-formulario', 'pt-cita-guardada'], 'invitar-alumnado': ['pt-invitar-tarjeta'], 'hacer-pregunta': ['pt-conversa-inicio', 'pt-conversa-respuesta'], 'serie-de-lecciones': ['pt-serie-lista', 'pt-serie-completo'], 'tarea-correccion-biblioteca': ['pt-tarea-lista', 'pt-tarea-formulario'], 'crear-asistente': ['pt-asistente-formulario', 'pt-asistente-guardado'] },
};
for (const [key, src] of [['es', ES_M], ['pt', PT_M]]) {
  for (const a of src.articles) if (IMG_OVERRIDE[key][a.id]) a.img = IMG_OVERRIDE[key][a.id];
}

// Taxonomía alineada con la ayuda pública (sevenai.es/es/ayuda): mismas secciones y orden.
const TAX_ORDER = ['empezar', 'cursos-docentes', 'series', 'fichas', 'tareas', 'conversaciones', 'documentos', 'plantillas', 'configuracion', 'it'];
// La sección de referencias se retira de la ayuda: sus artículos no se publican.
const TAX_NAMES = {
  es: { empezar: 'Primeros pasos', series: 'Series de lecciones', fichas: 'Fichas interactivas', tareas: 'Tareas de corrección y feedback', conversaciones: 'Conversaciones', documentos: 'Documentos', plantillas: 'Plantillas y asistentes', 'cursos-docentes': 'Cursos', configuracion: 'Cuenta y configuración', it: 'Para centros', problemas: 'Preguntas frecuentes', referencia: 'Referencia' },
  pt: { empezar: 'Primeiros passos', series: 'Séries de aulas', fichas: 'Fichas interativas', tareas: 'Tarefas de correção e feedback', conversaciones: 'Conversas', documentos: 'Documentos', plantillas: 'Modelos e assistentes', 'cursos-docentes': 'Cursos', configuracion: 'Conta e configuração', it: 'Para escolas', problemas: 'Perguntas frequentes', referencia: 'Referência' },
};
const TAX_DESC = {
  es: { 'cursos-docentes': 'Crear un curso, organizar secciones y contenidos, invitar al alumnado, citas, evaluación y configuración.', 'cursos-estudiantes': 'Unirte a un curso con código, enlace o invitación, y trabajar con sus contenidos.', series: 'Planificar secuencias de sesiones con tema, progresión y evaluación.', fichas: 'Crear hojas de trabajo con contexto, fuentes y ajustes.', tareas: 'Corregir trabajos con criterios, calibrar y devolver retroalimentación.', conversaciones: 'Preguntar al asistente, elegir el modo y las herramientas, y mejorar sus respuestas.', documentos: 'Subir, nombrar y encontrar documentos en la Biblioteca.', plantillas: 'Asistentes de IA con instrucciones propias.', configuracion: 'Menú de cuenta, configuración e idioma de la interfaz.', it: 'Carpetas compartidas, participantes, organización de la escuela y seguridad de los datos.', problemas: 'Respuestas a las dudas más habituales.', referencia: 'Escalas de calificación por país y glosario de términos.', empezar: 'Lo básico para entrar, orientarte y empezar a trabajar.' },
  pt: { 'cursos-docentes': 'Criar um curso, organizar seções e conteúdos, convidar os alunos, compromissos, avaliação e configurações.', 'cursos-estudiantes': 'Entrar em um curso com código, link ou convite, e trabalhar com os conteúdos.', series: 'Planejar sequências de aulas com tema, progressão e avaliação.', fichas: 'Criar folhas de trabalho com contexto, fontes e ajustes.', tareas: 'Corrigir trabalhos com critérios, calibrar e devolver feedback.', conversaciones: 'Fazer perguntas ao assistente, escolher o modo e as ferramentas.', documentos: 'Enviar, nomear e encontrar documentos na Biblioteca.', plantillas: 'Assistentes de IA com instruções próprias.', configuracion: 'Menu da conta, configuração e idioma da interface.', it: 'Pastas compartilhadas, participantes, organização da escola e segurança dos dados.', problemas: 'Respostas para as dúvidas mais comuns.', referencia: 'Escalas de avaliação por país e glossário de termos.', empezar: 'O básico para entrar, se orientar e começar a trabalhar.' },
};
const TAX_MOVE_STUDENT = ['unirse-curso', 'alumnado-no-entra'];
// Preguntas frecuentes se reparte por función: el usuario busca por lo que no le funciona.
const TAX_MOVE_FUNC = { 'codigo-filtrado': 'cursos-docentes', 'beta': 'cursos-docentes', 'respuesta-no-correcta': 'conversaciones', 'no-encuentro-seccion': 'empezar', 'no-puedo-acceder': 'empezar' };
const TAX_MAP = { cursos: 'cursos-docentes', plantillas: 'plantillas', series: 'series', fichas: 'fichas', tareas: 'tareas', conversaciones: 'conversaciones', documentos: 'documentos', configuracion: 'configuracion', it: 'it', problemas: 'problemas', referencia: 'referencia', empezar: 'empezar' };
// Artículos integrados en otro: su enlace antiguo sigue abriendo el destino.
const ALIASES = { 'documentos-formatos': 'subir-documento', 'ver-como-estudiante': 'visibilidad-entradas' };
function applyAliases(src) {
  const remap = (ids) => [...new Set((ids || []).map((id) => ALIASES[id] || id))];
  const articles = src.articles.filter((a) => !ALIASES[a.id]).map((a) => ({ ...a, related: remap(a.related).filter((r) => r !== a.id) }));
  return { ...src, articles };
}
function applyTaxonomy(src, lang) {
  const names = TAX_NAMES[lang], descs = TAX_DESC[lang];
  const categories = TAX_ORDER.map((id) => ({ id, name: names[id], desc: descs[id] }));
  const articles = src.articles.filter((a) => a.cat !== 'referencia').map((a) => {
    let cat = TAX_MAP[a.cat] || a.cat;
    if (TAX_MOVE_STUDENT.includes(a.id)) cat = 'cursos-docentes';
    if (a.id === 'plantillas-de-curso') cat = 'cursos-docentes';
    if (TAX_MOVE_FUNC[a.id]) cat = TAX_MOVE_FUNC[a.id];
    return { ...a, cat };
  });
  return { ...src, categories, articles };
}

// Capturas en portugués: pt-<nombre>.jpg (interfaz en portugués). Si una captura no existe, esa imagen se omite en PT.
const PT_ALT_FILE = path.join(ROOT, 'single', 'shots-pt-alt.json');
const PT_ALT = existsSync(PT_ALT_FILE) ? JSON.parse(await readFile(PT_ALT_FILE, 'utf8')) : {};
// Capturas con contenido de demostración en español (listas heredadas de la cuenta) o con etiquetas en inglés: no se usan en PT.
const PT_EXCLUDE = new Set(['pt-asistente-guardado', 'pt-plantilla-guardada', 'pt-plantillas-asistentes', 'pt-serie-lista', 'pt-serie-creada', 'pt-serie-relleno', 'pt-series-crear', 'pt-serie-formulario-completo', 'pt-serie-completo', 'pt-biblioteca-series-lista', 'pt-biblioteca-documentos', 'pt-biblioteca-inicio', 'pt-biblioteca', 'pt-carpeta-creada', 'pt-carpeta-nueva-relleno', 'pt-carpetas-compartidas', 'pt-tarea-elegida', 'pt-tarea-elegir-biblioteca', 'pt-form-tarea-comentarios', 'pt-tareas-lista', 'pt-tareas-correccion', 'pt-tarea-feedback-creada', 'pt-tarea-formulario', 'pt-tarea-feedback-relleno', 'pt-tarea-lista', 'pt-cursos-lista', 'pt-importar-curso-dialogo', 'pt-unirse-curso-dialogo', 'pt-plantillas-curso', 'pt-inicio', 'pt-conversa-inicio', 'pt-conversaciones', 'pt-herramientas-asistente', 'pt-modos-conversacion', 'pt-menu-cuenta', 'pt-menu-idioma', 'pt-ficha-paso2-fuentes', 'pt-ficha-paso3-analisis', 'pt-ficha-paso3-analisis-paso2']);
function ptImages(list) {
  return (list || []).map((n) => { const name = n.startsWith('pt-') ? n : (PT_ALT[n] && existsSync(path.join(ROOT, 'single', 'shots', `pt-${n}.jpg`)) ? `pt-${n}` : null); return name && !PT_EXCLUDE.has(name) ? name : null; }).filter(Boolean);
}

// Ajustes de recorridos (revisión de Customer Success):
// - Artículo de acceso con palabras clave equivalentes a las consultas reales.
// - Invitaciones en una sola guía: "compartir-curso" pasa a "invitar-alumnado".
const ACCESS_NEW = {
  es: { id: 'no-puedo-acceder', cat: 'problemas', title: 'No puedo acceder a Seven Assistant',
    answer: 'Revisa el correo y la contraseña, prueba en una ventana de incógnito y, si sigues bloqueado, pide ayuda a quien administra tu centro.',
    keywords: ['no puedo entrar', 'no puedo acceder', 'no puedo iniciar sesión', 'no funciona el acceso', 'login', 'contraseña', 'acceso bloqueado', 'cuenta bloqueada'],
    steps: [
      { t: 'Revisa el correo de acceso', b: 'Usa el correo con el que te dieron de alta en tu centro. Si el centro entra con una cuenta institucional, usa esa misma cuenta.' },
      { t: 'Prueba en otro navegador o en incógnito', b: 'Cierra sesión, abre una ventana de incógnito y vuelve a entrar. Así descartas cookies y sesiones antiguas.' },
      { t: 'Restablece la contraseña', b: 'Si la contraseña no funciona, usa la opción de recuperación de contraseña de la página de inicio de sesión.' },
      { t: 'Pide ayuda a quien administra el centro', b: 'Si sigues bloqueado, tu cuenta puede no estar activa o necesitar un acceso especial. Quien administra el centro puede revisarlo y dártelo.' }],
    tips: ['Si no tienes correo de acceso, pide a tu coordinador o al administrador del centro que te envíe una invitación.', 'Si tenías acceso y de repente lo has perdido, avisa al administrador: la configuración del centro pudo cambiar.'],
    related: ['unirse-curso', 'codigo-filtrado'] },
  'pt-BR': { id: 'no-puedo-acceder', cat: 'problemas', title: 'Não consigo acessar o Seven Assistant',
    answer: 'Confira o e-mail e a senha, tente em uma janela anônima e, se continuar bloqueado, peça ajuda a quem administra a sua escola.',
    keywords: ['não consigo entrar', 'não consigo acessar', 'não consigo entrar na conta', 'não consigo fazer login', 'login', 'senha', 'acesso bloqueado', 'conta bloqueada'],
    steps: [
      { t: 'Confira o e-mail de acesso', b: 'Use o e-mail com o qual você foi cadastrado na escola. Se a escola entra com uma conta institucional, use essa mesma conta.' },
      { t: 'Tente em outro navegador ou em janela anônima', b: 'Saia da conta, abra uma janela anônima e entre de novo. Assim você descarta cookies e sessões antigas.' },
      { t: 'Redefina a senha', b: 'Se a senha não funcionar, use a opção de recuperação de senha na página de entrada.' },
      { t: 'Peça ajuda a quem administra a escola', b: 'Se continuar bloqueado, sua conta pode não estar ativa ou precisar de um acesso especial. Quem administra a escola pode verificar e liberar o acesso.' }],
    tips: ['Se você não tem um e-mail de acesso, peça ao coordenador ou ao administrador da escola um convite.', 'Se você tinha acesso e de repente o perdeu, avise o administrador: a configuração da escola pode ter mudado.'],
    related: ['unirse-curso', 'codigo-filtrado'] },
};
function applyRecorridos(src, lang) {
  const key = lang === 'es' ? 'es' : 'pt-BR';
  let articles = src.articles.filter((a) => a.id !== 'compartir-curso').map((a) => {
    if (a.id === 'vistas-del-curso') return { ...a, img: lang === 'es' ? ['es-vistas-visualizacion'] : ['vistas-visualizacion'] };
    if (a.id === 'tarea-criterios') return { ...a, img: lang === 'es' ? ['es-tarea-criterio'] : ['tarea-criterio'] };
    if (a.id === 'ficha-revisar') return { ...a, img: [] };
    if (a.id === 'subir-documento') return { ...a, title: lang === 'es' ? 'Añadir archivos y páginas web a la Biblioteca' : 'Adicionar arquivos e páginas da web à Biblioteca' };
    if (a.id === 'ver-como-estudiante') return { ...a, related: [...(a.related || []), 'visibilidad-entradas'] };
    if (['documentos-formatos', 'documentos-nombres', 'no-encuentro-seccion'].includes(a.id)) return { ...a, img: [] };
    if (a.id === 'seguridad-datos') {
      const es = lang === 'es';
      return { ...a,
        answer: es ? 'Tus datos se alojan en Alemania, cumplimos el RGPD, no entrenamos la IA con tus datos y contamos con certificaciones ISO 27001, 9001 y 14001.' : 'Seus dados são hospedados na Alemanha, cumprimos o RGPD, não treinamos a IA com os seus dados e temos as certificações ISO 27001, 9001 e 14001.',
        steps: [
          { t: es ? 'Lo que garantizamos' : 'O que garantimos', b: es ? 'Datos alojados en Alemania, cumplimiento del RGPD y ninguna IA entrenada con tus datos. Certificaciones ISO 27001, 9001 y 14001.' : 'Dados hospedados na Alemanha, conformidade com o RGPD e nenhuma IA treinada com os seus dados. Certificações ISO 27001, 9001 e 14001.' },
          ...a.steps.map((st) => st.t.startsWith('Documentación oficial') || st.t.startsWith('Documentação oficial')
            ? { t: st.t, b: es ? 'Para la documentación completa, solicítala a través de 7education.com indicando el nombre de tu centro.' : 'Para a documentação completa, solicite-a em 7education.com informando o nome da sua escola.' }
            : st)] };
    }
    if (a.id === 'invitar-alumnado') return { ...a, table: lang === 'es'
      ? { head: ['Método', 'Cuándo usarlo', 'Qué necesita el alumnado'], rows: [
          ['Código de inscripción', 'Cuando el alumnado tiene cuenta y está en clase.', 'Cuenta iniciada y el código. No pide nombre: usa el de su cuenta.'],
          ['Enlace público', 'Cuando el alumnado no tiene cuenta. Compártelo solo con quien deba entrar. Hay que activarlo en Configuración.', 'Sin cuenta: escribe su nombre y la primera letra de su apellido.'],
          ['Invitación por correo', 'Cuando quieres invitar a una persona concreta.', 'Cuenta con el mismo correo. Hasta que acepte aparece como "Invitado".']] }
      : { head: ['Método', 'Quando usar', 'O que o aluno precisa'], rows: [
          ['Código de inscrição', 'Quando o aluno já tem conta e você quer compartilhar o mesmo código com a turma.', 'Entre na sua conta e tenha o código de inscrição em mãos. Não pede nome: usa o da conta.'],
          ['Link público', 'Quando o aluno não tem conta. Compartilhe só com quem deve entrar. É preciso ativá-lo em Definições.', 'Sem conta: escreva o nome e a primeira letra do sobrenome.'],
          ['Convite por e-mail', 'Quando você quer convidar uma pessoa específica.', 'Conta com o mesmo e-mail. Até aceitar, aparece como "Convidado".']] },
      keywords: lang === 'es' ? ['invitar alumnos', 'invitar alumnado', 'compartir curso', 'código de inscripción', 'enlace de inscripción', 'correo', 'añadir alumno'] : ['convidar alunos', 'compartilhar curso', 'código de inscrição', 'link de inscrição', 'e-mail', 'adicionar aluno'] };
    return a;
  });
  articles = articles.concat([{ ...ACCESS_NEW[key], img: [], tips: ACCESS_NEW[key].tips }]);
  return { ...src, articles };
}

// Agrupación interna de la categoría Cursos (una página más útil sin añadir opciones a la cabecera).
const COURSE_GROUPS = {
  es: [
    { name: 'Crear y organizar', ids: ['crear-curso', 'que-es-un-curso-ayuda', 'secciones', 'actividades', 'tipo-de-actividad', 'vistas-del-curso', 'configuracion-del-curso', 'plantillas-de-curso', 'importar-curso', 'exportar-curso', 'agregar-material-archivo', 'texto-material', 'enlace-y-nota', 'entrega', 'tarea-con-comentarios', 'agente-de-ia', 'ficha-de-trabajo-curso', 'contenidos-compartidos', 'visibilidad-entradas', 'ia-alumnado', 'beta'] },
    { name: 'Invitar y gestionar participantes', ids: ['invitar-alumnado', 'participantes-permisos', 'codigo-filtrado', 'unirse-curso', 'ver-como-estudiante', 'alumnado-no-entra'] },
    { name: 'Citas y seguimiento', ids: ['participantes-citas'] },
  ],
  pt: [
    { name: 'Criar e organizar', ids: ['crear-curso', 'que-es-un-curso-ayuda', 'secciones', 'actividades', 'tipo-de-actividad', 'vistas-del-curso', 'configuracion-del-curso', 'plantillas-de-curso', 'importar-curso', 'exportar-curso', 'agregar-material-archivo', 'texto-material', 'enlace-y-nota', 'entrega', 'tarea-con-comentarios', 'agente-de-ia', 'ficha-de-trabajo-curso', 'contenidos-compartidos', 'visibilidad-entradas', 'ia-alumnado', 'beta'] },
    { name: 'Convidar e gerenciar participantes', ids: ['invitar-alumnado', 'participantes-permisos', 'codigo-filtrado', 'unirse-curso', 'ver-como-estudiante', 'alumnado-no-entra'] },
    { name: 'Compromissos e acompanhamento', ids: ['participantes-citas'] },
  ],
};
function courseGroupsFor(loc, src) {
  const key = loc === 'es' ? 'es' : 'pt';
  const ids = src.articles.filter((a) => a.cat === 'cursos-docentes').map((a) => a.id);
  const groups = COURSE_GROUPS[key].map((g) => ({ name: g.name, ids: g.ids.filter((id) => ids.includes(id)) }));
  const placed = new Set(groups.flatMap((g) => g.ids));
  const rest = ids.filter((id) => !placed.has(id));
  if (rest.length) groups[0].ids.push(...rest);
  return groups;
}

// Cadenas de interfaz del centro (no son contenido de artículos).
const UI = {
  es: {
    center: 'Centro de ayuda', search: 'Buscar en la ayuda', searchPh: 'Crear un curso, invitar al alumnado, subir un documento…', searchBtn: 'Buscar',
    home: 'Inicio', language: 'Idioma', kicker: 'Centro de ayuda', heroTitle: 'Centro de ayuda de Seven Assistant',
    heroText: 'Respuestas rápidas, pasos claros y capturas reales de la herramienta. Busca lo que necesitas o elige una categoría.',
    intentsTitle: '¿Qué quieres hacer?', categories: 'Categorías', categoriesText: '', popularTitle: 'Artículos más consultados',
    articlesWord: 'artículos', categoryWord: 'Categoría', inSummary: 'En resumen', example: 'Ejemplo', steps: 'Pasos', tips: 'Consejos', related: 'Artículos relacionados',
    backTo: 'Volver a', lastUpdated: 'Actualizado', footer: 'Seven Assistant',
    searchIntro: 'Escribe una palabra: curso, enlace, documento, escala, idioma…', noResults: 'No encontramos artículos para esa búsqueda.', noResultsHint: 'Prueba con otra palabra o explora las categorías.',
    resultWord: 'resultado', resultWord: 'resultado', resultsWord: 'resultados', notFound: 'Página no encontrada', notFoundText: 'El artículo no existe o ha cambiado de sitio.',
    intents: [
      { id: 'crear-curso', label: 'Quiero crear un curso' },
      { id: 'compartir-curso', label: 'Quiero que mi alumnado entre al curso' },
      { id: 'tarea-correccion-biblioteca', label: 'Quiero corregir trabajos con criterios' },
      { id: 'carpetas-compartidas', label: 'Quiero gestionar accesos del centro' },
    ],
    popular: ['crear-curso', 'invitar-alumnado', 'subir-documento', 'hacer-pregunta', 'no-puedo-acceder', 'codigo-filtrado'],
  },
  'pt-BR': {
    center: 'Central de ajuda', search: 'Pesquisar na ajuda', searchPh: 'Criar um curso, convidar alunos, enviar um documento…', searchBtn: 'Pesquisar',
    home: 'Início', language: 'Idioma', kicker: 'Central de ajuda', heroTitle: 'Central de ajuda do Seven Assistant',
    heroText: 'Respostas rápidas, passos claros e capturas reais da ferramenta. Pesquise o que precisa ou escolha uma categoria.',
    intentsTitle: 'O que você quer fazer?', categories: 'Categorias', categoriesText: '', popularTitle: 'Artigos mais consultados',
    articlesWord: 'artigos', categoryWord: 'Categoria', inSummary: 'Em resumo', example: 'Exemplo', steps: 'Passos', tips: 'Dicas', related: 'Artigos relacionados',
    backTo: 'Voltar para', lastUpdated: 'Atualizado', footer: 'Seven Assistant',
    searchIntro: 'Digite uma palavra: curso, link, documento, escala, idioma…', noResults: 'Não encontramos artigos para essa pesquisa.', noResultsHint: 'Tente outra palavra ou explore as categorias.',
    resultWord: 'resultado', resultWord: 'resultado', resultsWord: 'resultados', notFound: 'Página não encontrada', notFoundText: 'O artigo não existe ou mudou de lugar.',
    intents: [
      { id: 'crear-curso', label: 'Quero criar um curso' },
      { id: 'compartir-curso', label: 'Quero que meus estudantes entrem no curso' },
      { id: 'tarea-correccion-biblioteca', label: 'Quero corrigir trabalhos com critérios' },
      { id: 'carpetas-compartidas', label: 'Quero gerenciar os acessos da escola' },
    ],
    popular: ['crear-curso', 'invitar-alumnado', 'subir-documento', 'hacer-pregunta', 'no-puedo-acceder', 'codigo-filtrado'],
  },
};

// Capturas reales de la interfaz (cuenta demo). La interfaz mostrada es la de español.
const SHOTS = {
  'invitar-correo-relleno': { file: 'invitar-correo-relleno.jpg', es: 'Invitar por correo electrónico: correo y rol Estudiante', pt: 'Convidar por e-mail: e-mail e papel Estudante (captura em espanhol)' },
  'invitar-correo-enviada': { file: 'invitar-correo-enviada.jpg', es: 'Invitación enviada por correo', pt: 'Convite enviado por e-mail (captura em espanhol)' },
  'participantes-tras-invitar': { file: 'participantes-tras-invitar.jpg', es: 'Participantes con la invitación pendiente en Invitaciones', pt: 'Participantes com o convite pendente em Convites (captura em espanhol)' },
  'cita-rellena': { file: "cita-rellena.jpg", es: "Formulario Crear cita relleno: título, fecha, horario, lugar y nota", pt: "Formulário Criar encontro preenchido: título, data, horário, local e nota (captura em espanhol)" },
  'cita-guardada': { file: "cita-guardada.jpg", es: "Cita guardada en Próximas con día, horario y lugar", pt: "Encontro salvo em Próximos com dia, horário e local (captura em espanhol)" },
  'serie-relleno': { file: "serie-relleno.jpg", es: "Formulario de serie de lecciones relleno", pt: "Formulário de série de aulas preenchido (captura em espanhol)" },
  'serie-creada': { file: "serie-creada.jpg", es: "Serie de lecciones creada en la lista", pt: "Série de aulas criada na lista (captura em espanhol)" },
  'tarea-feedback-relleno': { file: "tarea-feedback-relleno.jpg", es: "Tarea de feedback con solución modelo y criterios con puntos", pt: "Tarefa de feedback com solução modelo e critérios com pontos (captura em espanhol)" },
  'tarea-feedback-creada': { file: "tarea-feedback-creada.jpg", es: "Tarea de feedback creada", pt: "Tarefa de feedback criada (captura em espanhol)" },
  'tarea-elegir-biblioteca': { file: "tarea-elegir-biblioteca.jpg", es: "Elegir de la biblioteca al añadir una tarea con comentarios", pt: "Escolher da biblioteca ao adicionar uma tarefa com comentários (captura em espanhol)" },
  'tarea-elegida': { file: "tarea-elegida.jpg", es: "Tarea seleccionada de la biblioteca", pt: "Tarefa selecionada da biblioteca (captura em espanhol)" },
  'bio-vista-general-con-tarea': { file: "bio-vista-general-con-tarea.jpg", es: "Vista general con la tarea añadida a la sección", pt: "Visão geral com a tarefa adicionada à seção (captura em espanhol)" },
  'crear-material-archivo-relleno': { file: "crear-material-archivo-relleno.jpg", es: "Material con archivo PDF y título", pt: "Material com arquivo PDF e título (captura em espanhol)" },
  'crear-enlace-relleno': { file: "crear-enlace-relleno.jpg", es: "Formulario de enlace con título y dirección", pt: "Formulário de link com título e endereço (captura em espanhol)" },
  'crear-agente-relleno': { file: "crear-agente-relleno.jpg", es: "Agente de IA con título e instrucciones", pt: "Agente de IA com título e instruções (captura em espanhol)" },
  'crear-entrega-relleno': { file: "crear-entrega-relleno.jpg", es: "Entrega con enunciado, fecha y hora", pt: "Entrega com enunciado, data e hora (captura em espanhol)" },
  'plantilla-relleno': { file: "plantilla-relleno.jpg", es: "Plantilla de asistente rellena: nombre e instrucción", pt: "Modelo de assistente preenchido: nome e instrução (captura em espanhol)" },
  'plantilla-guardada': { file: "plantilla-guardada.jpg", es: "Plantilla guardada en la lista", pt: "Modelo salvo na lista (captura em espanhol)" },
  'carpeta-nueva-relleno': { file: "carpeta-nueva-relleno.jpg", es: "Nueva carpeta compartida con nombre y descripción", pt: "Nova pasta compartilhada com nome e descrição (captura em espanhol)" },
  'carpeta-creada': { file: "carpeta-creada.jpg", es: "Carpeta compartida creada", pt: "Pasta compartilhada criada (captura em espanhol)" },
  'texto-relleno': { file: "texto-relleno.jpg", es: "Material de lectura con título y texto", pt: "Material de leitura com título e texto (captura em espanhol)" },
  'texto-formulario': { file: "texto-formulario.jpg", es: "Formulario de material de lectura con editor de texto", pt: "Formulário de material de leitura com editor de texto (captura em espanhol)" },
  'bio-vista-general-tras-crear': { file: "bio-vista-general-tras-crear.jpg", es: "Vista general del curso con el contenido creado", pt: "Visão geral do curso com o conteúdo criado (captura em espanhol)" },
  'inicio': { file: 'inicio.jpg', es: 'Pantalla de inicio: campo de conversación y barra lateral', pt: 'Tela inicial: campo de conversa e barra lateral (captura em espanhol)' },
  'cursos-lista': { file: 'cursos-lista-real.jpg', es: 'Pantalla de Cursos con los cursos de tu cuenta', pt: 'Tela de Cursos com os cursos da sua conta (captura em espanhol)' },
  'curso-crear-paso1': { file: 'curso-crear-paso1.jpg', es: 'Crear curso, paso 1: datos básicos', pt: 'Criar curso, passo 1: dados básicos (captura em espanhol)' },
  'curso-crear-paso2': { file: 'curso-crear-paso2.jpg', es: 'Crear curso, paso 2: elegir contenido', pt: 'Criar curso, passo 2: escolher conteúdo (captura em espanhol)' },
  'curso-vista-general': { file: 'bio-vista-general.jpg', es: 'Vista general del curso: invitación, cita y secciones', pt: 'Visão geral do curso: convite, encontro e seções (captura em espanhol)' },
  'curso-anadir-actividad': { file: 'bio-anadir-menu.jpg', es: 'Añadir actividad o material dentro de una sección', pt: 'Adicionar atividade ou material dentro de uma seção (captura em espanhol)' },
  'curso-vista-estudiante': { file: 'bio-vista-estudiante.jpg', es: 'Vista de estudiante del curso', pt: 'Visão de estudante do curso (captura em espanhol)' },
  'curso-configuracion': { file: 'bio-configuracion.jpg', es: 'Configuración del curso: apartado General', pt: 'Configurações do curso: seção Geral (captura em espanhol)' },
  'plantillas-curso': { file: 'plantillas-curso.jpg', es: 'Cursos, pestaña Plantillas: unidades didácticas para adoptar', pt: 'Cursos, aba Modelos: unidades didáticas para adotar (captura em espanhol)' },
  'conversaciones': { file: 'conversaciones.jpg', es: 'Conversación con el campo para preguntar', pt: 'Conversa com o campo para perguntar (captura em espanhol)' },
  'herramientas-asistente': { file: 'herramientas-asistente.jpg', es: 'Plantillas de Seven Assistant: herramientas del asistente', pt: 'Modelos do Seven Assistant: ferramentas do assistente (captura em espanhol)' },
  'modos-conversacion': { file: 'modos-conversacion.jpg', es: 'Modos de conversación del botón Dinámico', pt: 'Modos de conversa do botão Dinâmico (captura em espanhol)' },
  'biblioteca': { file: 'biblioteca.jpg', es: 'Biblioteca con el bloque Crear rápido', pt: 'Biblioteca com o bloco Criar rápido (captura em espanhol)' },
  'series-crear': { file: 'serie-formulario-completo.jpg', es: 'Formulario de serie de lecciones', pt: 'Formulário de série de aulas (captura em espanhol)' },
  'ficha-crear': { file: 'ficha-paso1.jpg', es: 'Crear hoja de trabajo, paso 1: contexto', pt: 'Criar folha de trabalho, passo 1: contexto (captura em espanhol)' },
  'tareas-correccion': { file: 'tareas-lista.jpg', es: 'Tareas de corrección y feedback', pt: 'Tarefas de correção e feedback (captura em espanhol)' },
  'plantillas-asistentes': { file: 'plantillas-asistentes.jpg', es: 'Plantillas (asistentes de IA)', pt: 'Modelos (assistentes de IA) (captura em espanhol)' },
  'menu-cuenta': { file: 'menu-cuenta.jpg', es: 'Menú de cuenta', pt: 'Menu da conta (captura em espanhol)' },
  'menu-idioma': { file: 'menu-idioma.jpg', es: 'Menú de cuenta con la opción Idioma', pt: 'Menu da conta com a opção Idioma (captura em espanhol)' },
  'carpetas-compartidas': { file: 'carpetas-compartidas.jpg', es: 'Gestionar carpetas compartidas', pt: 'Gerenciar pastas compartilhadas (captura em espanhol)' },
  'adoptar-confirmar': { file: 'adoptar-confirmar.jpg', es: 'Confirmación al adoptar una plantilla de curso', pt: 'Confirmação ao adotar um modelo de curso (captura em espanhol)' },
  'bio-vista-general': { file: 'bio-vista-general.jpg', es: 'Vista general del curso: invitación, cita y secciones', pt: 'Visão geral do curso: convite, encontro e seções (captura em espanhol)' },
  'bio-anadir-menu': { file: 'bio-anadir-menu.jpg', es: 'Añadir actividad o material dentro de una sección', pt: 'Adicionar atividade ou material dentro de uma seção (captura em espanhol)' },
  'bio-vista-estudiante': { file: 'bio-vista-estudiante.jpg', es: 'Vista de estudiante del curso', pt: 'Visão de estudante do curso (captura em espanhol)' },
  'bio-configuracion': { file: 'bio-configuracion.jpg', es: 'Configuración del curso: apartado General', pt: 'Configurações do curso: seção Geral (captura em espanhol)' },
  'bio-participantes': { file: 'bio-participantes.jpg', es: 'Pestaña Participantes con filtros y lista de miembros', pt: 'Aba Participantes com filtros e lista de membros (captura em espanhol)' },
  'bio-citas': { file: 'bio-citas.jpg', es: 'Pestaña Citas, vacía, con el botón Crear cita', pt: 'Aba Encontros, vazia, com o botão Criar encontro (captura em espanhol)' },
  'bio-crear-cita': { file: 'bio-crear-cita.jpg', es: 'Pestaña Citas con el botón Crear cita', pt: 'Aba Encontros com o botão Criar encontro (captura em espanhol)' },
  'bio-contenidos-compartidos': { file: 'bio-contenidos-compartidos.jpg', es: 'Pestaña Contenidos compartidos con filtros por tipo', pt: 'Aba Conteúdos compartilhados com filtros por tipo (captura em espanhol)' },
  'form-material': { file: 'form-material.jpg', es: 'Formulario Material: subir archivo o elegir de la biblioteca', pt: 'Formulário Material: enviar arquivo ou escolher da biblioteca (captura em espanhol)' },
  'form-texto': { file: 'form-texto.jpg', es: 'Formulario de Texto para un material de lectura', pt: 'Formulário de Texto para um material de leitura (captura em espanhol)' },
  'form-entrega': { file: 'form-entrega.jpg', es: 'Formulario de Entrega: título, enunciado, fecha y hora', pt: 'Formulário de Entrega: título, enunciado, data e hora (captura em espanhol)' },
  'form-tarea-comentarios': { file: 'form-tarea-comentarios.jpg', es: 'Tarea con comentarios: elegir de la biblioteca', pt: 'Tarefa com comentários: escolher da biblioteca (captura em espanhol)' },
  'form-unidad': { file: 'form-unidad.jpg', es: 'Formulario de Unidad didáctica', pt: 'Formulário de Unidade didática (captura em espanhol)' },
  'form-agente': { file: 'form-agente.jpg', es: 'Formulario de Agente de IA: nombre e instrucciones', pt: 'Formulário de Agente de IA: nome e instruções (captura em espanhol)' },
  'form-enlace': { file: 'form-enlace.jpg', es: 'Formulario de Enlace: texto y dirección', pt: 'Formulário de Link: texto e endereço (captura em espanhol)' },
  'form-nota': { file: 'form-nota.jpg', es: 'Formulario de Nota: texto breve', pt: 'Formulário de Nota: texto breve (captura em espanhol)' },
  'unirse-curso-dialogo': { file: 'unirse-curso-dialogo.jpg', es: 'Diálogo Unirse a un curso con el código de inscripción', pt: 'Diálogo Entrar em um curso com o código de inscrição (captura em espanhol)' },
  'importar-curso-dialogo': { file: 'importar-curso-dialogo.jpg', es: 'Diálogo Importar curso', pt: 'Diálogo Importar curso (captura em espanhol)' },
  'invitar-personas': { file: 'invitar-personas.jpg', es: 'Diálogo Invitar al alumnado: código e invitación por correo', pt: 'Diálogo Convidar alunos: código e convite por e-mail (captura em espanhol)' },
  'biblioteca-inicio': { file: 'biblioteca-inicio.jpg', es: 'Biblioteca: Crear rápido y buscador', pt: 'Biblioteca: Criar rápido e buscador (captura em espanhol)' },
  'biblioteca-documentos': { file: 'biblioteca-documentos.jpg', es: 'Mi biblioteca: lista de documentos', pt: 'Minha biblioteca: lista de documentos (captura em espanhol)' },
  'biblioteca-series-lista': { file: 'biblioteca-series-lista.jpg', es: 'Series de lecciones con Generar con IA y Crear', pt: 'Séries de aulas com Gerar com IA e Criar (captura em espanhol)' },
  'serie-formulario-completo': { file: 'serie-formulario-completo.jpg', es: 'Formulario Crear serie de lecciones', pt: 'Formulário Criar série de aulas (captura em espanhol)' },
  'tareas-lista': { file: 'tareas-lista.jpg', es: 'Tareas de corrección y feedback: lista con Generar con IA y Crear', pt: 'Tarefas de correção e feedback: lista com Gerar com IA e Criar (captura em espanhol)' },
  'tarea-formulario': { file: 'tarea-formulario.jpg', es: 'Formulario Crear tarea de feedback: rigor, subidas, solución y criterios', pt: 'Formulário Criar tarefa de feedback: rigor, envios, solução e critérios (captura em espanhol)' },
  'ficha-paso1': { file: 'ficha-paso1.jpg', es: 'Crear hoja de trabajo, paso 1: contexto', pt: 'Criar folha de trabalho, passo 1: contexto (captura em espanhol)' },
  'ficha-paso2-fuentes': { file: 'ficha-paso2-fuentes.jpg', es: 'Crear hoja de trabajo, paso 2: fuentes', pt: 'Criar folha de trabalho, passo 2: fontes (captura em espanhol)' },
  'plantilla-crear-formulario': { file: 'plantilla-crear-formulario.jpg', es: 'Plantillas: formulario de creación de asistente', pt: 'Modelos: formulário de criação de assistente (captura em espanhol)' },
  'cfg-ia': { file: 'cfg-ia.jpg', es: 'Configuración: apartado IA en el curso', pt: 'Configurações: seção IA no curso (captura em espanhol)' },
  'cfg-codigo': { file: 'cfg-codigo.jpg', es: 'Configuración: código de inscripción y enlace público', pt: 'Configurações: código de inscrição e link público (captura em espanhol)' },
  'cfg-visualizacion': { file: 'cfg-visualizacion.jpg', es: 'Configuración: apartado Visualización', pt: 'Configurações: seção Visualização (captura em espanhol)' },
  'cfg-exportacion': { file: 'cfg-exportacion.jpg', es: 'Configuración: apartado Exportación', pt: 'Configurações: seção Exportação (captura em espanhol)' },
  'es-tarea-criterio': { file: 'es-tarea-criterio.jpg', es: 'Criterio de calificación rellenado en el formulario de tarea de feedback', pt: 'Criterio de calificación rellenado en el formulario de tarea de feedback' },
  'es-vistas-visualizacion': { file: 'es-vistas-visualizacion.jpg', es: 'Sección Visualización del curso con las cuatro vistas de la vista general', pt: 'Sección Visualización del curso con las cuatro vistas de la vista general' },
  'es-cita-pestana': { file: 'es-cita-pestana.jpg', es: 'Pestaña Citas del curso, con el botón Crear cita', pt: 'Pestaña Citas del curso, con el botón Crear cita' },
  'es-cita-formulario': { file: 'es-cita-formulario.jpg', es: 'Formulario Crear cita con título, fecha, horario, lugar y nota', pt: 'Formulario Crear cita con título, fecha, horario, lugar y nota' },
  'es-cita-guardada': { file: 'es-cita-guardada.jpg', es: 'La cita guardada aparece en la lista de próximas', pt: 'La cita guardada aparece en la lista de próximas' },
  'es-invitar-tarjeta': { file: 'es-invitar-tarjeta.jpg', es: 'Vista general del curso con la tarjeta Invitar al alumnado', pt: 'Vista general del curso con la tarjeta Invitar al alumnado' },
  'es-invitar-codigo': { file: 'es-invitar-codigo.jpg', es: 'Código de inscripción copiado desde la tarjeta de invitación', pt: 'Código de inscripción copiado desde la tarjeta de invitación' },
  'es-conversa-inicio': { file: 'es-conversa-inicio.jpg', es: 'Conversaciones: cuadro de mensaje y herramientas', pt: 'Conversaciones: cuadro de mensaje y herramientas' },
  'es-conversa-respuesta': { file: 'es-conversa-respuesta.jpg', es: 'Respuesta del asistente a una pregunta de clase', pt: 'Respuesta del asistente a una pregunta de clase' },
  'es-serie-lista': { file: 'es-serie-lista.jpg', es: 'Lista de series de lecciones', pt: 'Lista de series de lecciones' },
  'es-serie-completo': { file: 'es-serie-completo.jpg', es: 'Formulario de serie de lecciones con tema, asignatura, curso y objetivos', pt: 'Formulario de serie de lecciones con tema, asignatura, curso y objetivos' },
  'es-tarea-lista': { file: 'es-tarea-lista.jpg', es: 'Lista de tareas de corrección y feedback', pt: 'Lista de tareas de corrección y feedback' },
  'es-tarea-formulario': { file: 'es-tarea-formulario.jpg', es: 'Formulario de tarea de feedback con título y descripción', pt: 'Formulario de tarea de feedback con título y descripción' },
  'es-asistente-formulario': { file: 'es-asistente-formulario.jpg', es: 'Formulario Crear plantilla: nombre, herramientas e instrucción', pt: 'Formulario Crear plantilla: nombre, herramientas e instrucción' },
  'es-asistente-guardado': { file: 'es-asistente-guardado.jpg', es: 'Lista de plantillas con el asistente creado', pt: 'Lista de plantillas con el asistente creado' },
  'pt-cita-pestana': { file: 'pt-cita-pestana.jpg', es: 'Aba Compromissos do curso, com o botão Criar compromisso', pt: 'Aba Compromissos do curso, com o botão Criar compromisso' },
  'pt-cita-formulario': { file: 'pt-cita-formulario.jpg', es: 'Formulário Criar compromisso com título, data, horário, local e nota', pt: 'Formulário Criar compromisso com título, data, horário, local e nota' },
  'pt-cita-guardada': { file: 'pt-cita-guardada.jpg', es: 'O compromisso salvo aparece na lista de próximos', pt: 'O compromisso salvo aparece na lista de próximos' },
  'pt-invitar-tarjeta': { file: 'pt-invitar-tarjeta.jpg', es: 'Vista geral do curso com o cartão de convite', pt: 'Vista geral do curso com o cartão de convite' },
  'pt-invitar-codigo': { file: 'pt-invitar-codigo.jpg', es: 'Código de inscrição copiado do cartão de convite', pt: 'Código de inscrição copiado do cartão de convite' },
  'pt-conversa-inicio': { file: 'pt-conversa-inicio.jpg', es: 'Conversas: caixa de mensagem e ferramentas', pt: 'Conversas: caixa de mensagem e ferramentas' },
  'pt-conversa-respuesta': { file: 'pt-conversa-respuesta.jpg', es: 'Resposta do assistente a uma pergunta de aula', pt: 'Resposta do assistente a uma pergunta de aula' },
  'pt-serie-lista': { file: 'pt-serie-lista.jpg', es: 'Lista de séries de aulas', pt: 'Lista de séries de aulas' },
  'pt-serie-completo': { file: 'pt-serie-completo.jpg', es: 'Formulário da série de aulas com tema, disciplina, ano e objetivos', pt: 'Formulário da série de aulas com tema, disciplina, ano e objetivos' },
  'pt-tarea-lista': { file: 'pt-tarea-lista.jpg', es: 'Lista de tarefas de correção e feedback', pt: 'Lista de tarefas de correção e feedback' },
  'pt-tarea-formulario': { file: 'pt-tarea-formulario.jpg', es: 'Formulário da tarefa de feedback com título e descrição', pt: 'Formulário da tarefa de feedback com título e descrição' },
  'pt-asistente-formulario': { file: 'pt-asistente-formulario.jpg', es: 'Formulário Novo Modelo: nome, ferramentas e instrução', pt: 'Formulário Novo Modelo: nome, ferramentas e instrução' },
  'pt-asistente-guardado': { file: 'pt-asistente-guardado.jpg', es: 'Lista de modelos com o assistente criado', pt: 'Lista de modelos com o assistente criado' },
};

for (const [n, alt] of Object.entries(PT_ALT)) {
  if (existsSync(path.join(ROOT, 'single', 'shots', `pt-${n}.jpg`))) SHOTS[`pt-${n}`] = { file: `pt-${n}.jpg`, es: alt, pt: alt };
}
const shotUri = async (file) => 'data:image/jpeg;base64,' + (await readFile(path.join(ROOT, 'single', 'shots', file))).toString('base64');

// Vídeos tutoriales: URLs de assets (subidos al artefacto) y subtítulos embebidos.
import { existsSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { VIDEO_FOR_ARTICLE } from './video-map.mjs';
const VIDEO_ASSETS_FILE = path.join(ROOT, 'single', 'video-assets.json');
const VIDEO_ASSETS = existsSync(VIDEO_ASSETS_FILE) ? JSON.parse(await readFile(VIDEO_ASSETS_FILE, 'utf8')) : {};
const PUBLIC_SITE = process.env.PUBLIC_SITE === '1';
const LANG_DIR = { es: 'es', 'pt-BR': 'pt-br' };
const SRCLANG = { es: 'es', 'pt-BR': 'pt-BR' };
const TRACK_LABEL = { es: 'Español', 'pt-BR': 'Português (Brasil)' };
// Portada: titular de marketing y texto de beneficio (textos adaptados del díptico).
Object.assign(UI.es, {"kicker": "", "heroTitle": "Centro de ayuda", "heroAccent": "De la primera idea a tu próxima clase", "heroText": "Descubre cómo crear materiales con IA, organizar tus cursos y compartirlos con tu alumnado en Seven Assistant."});
Object.assign(UI['pt-BR'], {"kicker": "", "heroTitle": "Central de ajuda", "heroAccent": "Da primeira ideia à sua próxima aula", "heroText": "Descubra como criar materiais com IA, organizar seus cursos e compartilhá-los com seus alunos no Seven Assistant."});

Object.assign(UI.es, { topics: 'Temas', exploreTopics: 'Explorar temas', quickLabel: 'Accesos rápidos', quick: [{ l: 'Crear un curso', id: 'crear-curso' }, { l: 'Invitar al alumnado', id: 'invitar-alumnado' }, { l: 'Subir un documento', id: 'subir-documento' }, { l: 'No puedo acceder', id: 'no-puedo-acceder' }] });
Object.assign(UI['pt-BR'], { topics: 'Temas', exploreTopics: 'Explorar temas', quickLabel: 'Acessos rápidos', quick: [{ l: 'Criar um curso', id: 'crear-curso' }, { l: 'Convidar os alunos', id: 'invitar-alumnado' }, { l: 'Enviar um documento', id: 'subir-documento' }, { l: 'Não consigo acessar', id: 'no-puedo-acceder' }] });
Object.assign(UI.es, { video: 'Vídeo tutorial', videoHint: 'Activa los subtítulos con el botón CC del reproductor.' });
Object.assign(UI['pt-BR'], { featuredVideos: 'Vídeos tutoriais', video: 'Vídeo tutorial', videoHint: 'Ative as legendas pelo botão CC do player.', vpControls: 'Controles do vídeo', vpCC: 'CC Legendas', vpSpeed: 'Velocidade', vpFallback: 'Não foi possível carregar o vídeo.', vpOpen: 'Abrir o vídeo' });
Object.assign(UI.es, { footHelp: 'Centro de ayuda', footProduct: 'Seven Assistant', footProductLink: 'Funcionalidades de Seven Assistant', footCompany: 'Seven Education', footCopy: 'Copyright © Seven Education 2026' });
Object.assign(UI['pt-BR'], { footHelp: 'Central de ajuda', footProduct: 'Seven Assistant', footProductLink: 'Recursos do Seven Assistant', footCompany: 'Seven Education', footCopy: 'Copyright © Seven Education 2026' });
Object.assign(UI.es, { faqRelated: 'Preguntas frecuentes relacionadas' });
Object.assign(UI['pt-BR'], { faqRelated: 'Perguntas frequentes relacionadas' });
Object.assign(UI.es, { featuredVideos: 'Vídeos tutoriales', vpControls: 'Controles del vídeo', vpCC: 'CC Subtítulos', vpSpeed: 'Velocidad', vpFallback: 'No se pudo cargar el vídeo.', vpOpen: 'Abrir el vídeo' });
const durText = (sec) => (sec >= 60 ? Math.floor(sec / 60) + ' min ' + (sec % 60) + ' s' : sec + ' s');
async function videosFor(loc, src) {
  const out = {};
  for (const [articleId, v] of Object.entries(VIDEO_FOR_ARTICLE)) {
    if (!src.articles.some((a) => a.id === articleId)) throw new Error(`vídeo para artículo inexistente: ${articleId}`);
    const dir = LANG_DIR[loc];
    const url = PUBLIC_SITE ? `videos/${dir}-${v.file}.mp4` : VIDEO_ASSETS[`${dir}/${v.file}.mp4`];
    if (!url) continue;
    const base = path.join(ROOT, 'video', 'review', dir, v.file);
    const dur = Math.round(parseFloat(execFileSync('ffprobe', ['-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', base + '.mp4']).toString()));
    const vtt = 'data:text/vtt;base64,' + (await readFile(base + '.vtt')).toString('base64');
    const poster = PUBLIC_SITE ? `videos/${dir}-${v.file}.jpg` : '';
    const narr = loc === 'es' ? 'Narración en español' : 'Narração em português (Brasil)';
    out[articleId] = { src: url, vtt, poster, narr, srclang: SRCLANG[loc], label: TRACK_LABEL[loc], dur: durText(dur), title: v.label[loc === 'es' ? 'es' : 'pt'], after: !!v.after };
  }
  return out;
}

const data = {};
for (const [loc, src0] of [['es', ES_M], ['pt-BR', PT_M]]) {
  const src = applyAliases(applyTaxonomy(applyRecorridos(src0, loc === 'es' ? 'es' : 'pt'), loc === 'es' ? 'es' : 'pt'));
  if (loc !== 'es') for (const a of src.articles) a.img = ptImages(a.img);
  const key = loc === 'es' ? 'es' : 'pt';
  const shots = {}, alt = {};
  for (const [name, s] of Object.entries(SHOTS)) {
    const used = src.articles.some((a) => (a.img || []).includes(name));
    if (!used) continue;
    shots[name] = await shotUri(s.file);
    alt[name] = s[key];
  }
  data[loc] = { updated: src.updated, ui: UI[loc], categories: src.categories, articles: src.articles, shots, alt, videos: await videosFor(loc, src), courseGroups: courseGroupsFor(loc, src), aliases: ALIASES };
}

// Comprobaciones: cada captura referenciada existe y cada categoría de artículo está definida.
for (const loc of ['es', 'pt-BR']) {
  for (const a of data[loc].articles) {
    for (const n of a.img || []) if (!data[loc].shots[n]) throw new Error(`captura inexistente en ${loc}/${a.id}: ${n}`);
    if (!data[loc].categories.some((c) => c.id === a.cat)) throw new Error(`categoría inexistente en ${loc}/${a.id}`);
  }
}

const json = JSON.stringify(data).replace(/<\//g, '<\\/');
const tpl = await readFile(path.join(ROOT, 'single', 'template.html'), 'utf8');
if (!tpl.includes('/*__DATA__*/null')) throw new Error('plantilla sin marcador de datos');
const LOGO = 'data:image/png;base64,' + (await readFile(path.join(ROOT, 'single', 'logo-seven-education.png'))).toString('base64');
const LOGO_FOOT = 'data:image/png;base64,' + (await readFile(path.join(ROOT, 'single', 'logo-seven-education-footer.png'))).toString('base64');
const LOGO_ASSISTANT = 'data:image/png;base64,' + (await readFile(path.join(ROOT, 'single', 'logo-seven-assistant.png'))).toString('base64');
const out = tpl.replace('/*__DATA__*/null', json).replace('__LOGO_ASSISTANT__', LOGO_ASSISTANT).split('__LOGO_FOOT__').join(LOGO_FOOT).split('__LOGO__').join(LOGO);
const outFile = PUBLIC_SITE ? path.join(ROOT, 'site', 'index.html') : path.join(ROOT, 'single', 'centro-ayuda.html');
await (await import('node:fs/promises')).mkdir(path.dirname(outFile), { recursive: true });
await writeFile(outFile, out, 'utf8');
if (PUBLIC_SITE) {
  const { copyFile } = await import('node:fs/promises');
  await (await import('node:fs/promises')).mkdir(path.join(ROOT, 'site', 'videos'), { recursive: true });
  for (const dir of ['es', 'pt-br']) for (const f of [...new Set(Object.values(VIDEO_FOR_ARTICLE).map((v) => v.file))]) {
    const src = path.join(ROOT, 'video', 'review', dir, `${f}.mp4`);
    if (existsSync(src) && (out.includes(`videos/${dir}-${f}.mp4`))) await copyFile(src, path.join(ROOT, 'site', 'videos', `${dir}-${f}.mp4`));
    const poster = path.join(ROOT, 'video', 'review', dir, `${f}.jpg`);
    if (existsSync(poster) && out.includes(`videos/${dir}-${f}.jpg`)) await copyFile(poster, path.join(ROOT, 'site', 'videos', `${dir}-${f}.jpg`));
  }
}
console.log(`✓ single/centro-ayuda.html (${(Buffer.byteLength(out) / 1024).toFixed(0)} KB) · ${data.es.articles.length} artículos por idioma`);
