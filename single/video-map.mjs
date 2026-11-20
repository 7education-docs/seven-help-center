// Vídeo que se muestra en cada artículo (mismo id en ES y PT-BR).
// file = nombre base en video/review/<es|pt-br>/. Los casos de uso sustituyen a los recorridos en su artículo.
export const VIDEO_FOR_ARTICLE = {
  // Consulta rápida: los pasos van primero y el vídeo después (after: true).
  'participantes-citas': { file: 'cita', label: { es: 'Crear una cita', pt: 'Criar um compromisso' } },
  'serie-de-lecciones': { file: 'serie', label: { es: 'Crear una serie de lecciones', pt: 'Criar uma série de aulas' } },
  'tarea-correccion-biblioteca': { file: 'tarea', label: { es: 'Crear una tarea de corrección', pt: 'Criar uma tarefa de correção' } },
  'crear-asistente': { file: 'asistente', label: { es: 'Crear un asistente', pt: 'Criar um assistente' } },
  'crear-curso': { file: 'crear-curso', label: { es: 'Crear un curso', pt: 'Criar um curso' } },
  'secciones': { file: 'secciones', label: { es: 'Organizar el curso', pt: 'Organizar o curso' } },
  'agregar-material-archivo': { file: 'material-archivo', label: { es: 'Añadir un material', pt: 'Adicionar um material' } },
  'texto-material': { file: 'texto-lectura', label: { es: 'Escribir un material de lectura', pt: 'Escrever um material de leitura' } },
  'entrega': { file: 'entrega-archivo', label: { es: 'Crear una entrega', pt: 'Criar uma entrega' } },
  'tarea-con-comentarios': { file: 'tarea-comentarios', label: { es: 'Tarea con comentarios', pt: 'Tarefa com feedback' } },
  'agente-de-ia': { file: 'agente-ia', label: { es: 'Crear un agente de IA', pt: 'Criar um agente de IA' } },
  'que-es-un-curso-ayuda': { file: 'C-1', label: { es: 'Pestañas de un curso', pt: 'Abas de um curso' } },
  'subir-documento': { file: 'documentos', label: { es: 'Documentos', pt: 'Documentos' } },
  'ficha-interactiva': { file: 'fichas-interactivas', label: { es: 'Crear una ficha interactiva', pt: 'Criar uma ficha interativa' } },
  'visibilidad-entradas': { file: 'ver-alumno', label: { es: 'Qué ve el alumnado en mi curso', pt: 'O que o aluno vê no meu curso' } },
};
