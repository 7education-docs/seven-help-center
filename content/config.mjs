// Configuración global del centro de ayuda.
// Los textos viven en content/es.mjs y content/pt-BR.mjs (mismos IDs, mismo orden).
export const SITE = {
  productName: 'Seven Assistant',
  origin: process.env.HELP_ORIGIN ?? 'https://sevenai.es',
  // Ruta pública del centro de ayuda. En local se usa HELP_BASE="" para servir desde la raíz.
  basePath: process.env.HELP_BASE ?? '/ayuda',
  defaultLocale: 'es',
  locales: {
    es: {
      code: 'es',
      urlSegment: 'es',
      htmlLang: 'es',
      hreflang: 'es-419',
      label: 'Español',
      // Videos, subtítulos y búsqueda se generan por idioma.
    },
    'pt-BR': {
      code: 'pt-BR',
      urlSegment: 'pt-br',
      htmlLang: 'pt-BR',
      hreflang: 'pt-BR',
      label: 'Português (Brasil)',
    },
  },
  // IDs estables compartidos por ambos idiomas.
  sectionIds: [
    'cursos',
    'conversaciones',
    'documentos',
    'series-de-lecciones',
    'tareas-de-correccion',
    'fichas-interactivas',
    'plantillas',
    'configuracion',
  ],
  roleIds: ['docente', 'coordinacion', 'jefatura-tutoria', 'responsable-it'],
  courseIds: [
    'primeros-pasos',
    'cursos-crear-organizar',
    'cursos-actividades',
    'cursos-compartir-seguimiento',
    'biblioteca-asistente',
    'administracion-it',
  ],
};
