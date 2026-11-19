#!/usr/bin/env python3
"""Reagrupa la sección de Cursos en 5 grupos (misma información, sin fusionar artículos).

Antes: "Crear y organizar" (20 artículos), "Invitar y gestionar participantes" (5), "Citas y seguimiento" (1).
Después: cada grupo responde a una tarea del docente. Los artículos y sus capturas no cambian.
"""

GROUPS = {
    'es': [
        ('Crear el curso', ['crear-curso', 'importar-curso', 'plantillas-de-curso', 'que-es-un-curso-ayuda']),
        ('Organizar el contenido', ['secciones', 'actividades', 'tipo-de-actividad', 'vistas-del-curso',
                                    'visibilidad-entradas', 'contenidos-compartidos']),
        ('Materiales y entregas', ['agregar-material-archivo', 'texto-material', 'enlace-y-nota',
                                   'entrega', 'tarea-con-comentarios']),
        ('IA y ajustes', ['ia-alumnado', 'agente-de-ia', 'configuracion-del-curso', 'exportar-curso']),
        ('Participantes y citas', ['invitar-alumnado', 'participantes-permisos', 'unirse-curso', 'participantes-citas']),
    ],
    'pt-BR': [
        ('Criar o curso', ['crear-curso', 'importar-curso', 'plantillas-de-curso', 'que-es-un-curso-ayuda']),
        ('Organizar o conteúdo', ['secciones', 'actividades', 'tipo-de-actividad', 'vistas-del-curso',
                                  'visibilidad-entradas', 'contenidos-compartidos']),
        ('Materiais e entregas', ['agregar-material-archivo', 'texto-material', 'enlace-y-nota',
                                  'entrega', 'tarea-con-comentarios']),
        ('IA e ajustes', ['ia-alumnado', 'agente-de-ia', 'configuracion-do-curso', 'exportar-curso']),
        ('Participantes e compromissos', ['invitar-alumnado', 'participantes-permisos', 'unirse-curso', 'participantes-citas']),
    ],
}


def apply_course_overlay(merged: dict) -> None:
    for loc, groups in GROUPS.items():
        d = merged[loc]
        ids = {a['id'] for a in d['articles'] if a.get('cat') == 'cursos-docentes'}
        wanted = [i for _, items in groups for i in items]
        # pt usa el id 'configuracion-del-curso' (mismo id en ambos idiomas)
        wanted = [('configuracion-del-curso' if i == 'configuracion-do-curso' else i) for i in wanted]
        missing = [i for i in wanted if i not in ids]
        assert not missing, (loc, missing)
        leftover = ids - set(wanted)
        assert not leftover, (loc, 'sin grupo:', leftover)
        d['courseGroups'] = [{'name': name, 'ids': [('configuracion-del-curso' if i == 'configuracion-do-curso' else i) for i in items]}
                             for name, items in groups]
    print('  course overlay: 5 grupos en es y pt-BR')
