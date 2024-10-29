{
    'name': 'Gestión Estudiantil',
    'version': '1.0.0',
    'summary': 'Gestión de alumnos, programas e inscripciones.',
    'sequence': 5,
    'description': """
        Este módulo permite gestionar los datos de alumnos, programas e inscripciones.
        Incluye un modelo de Alumnos con información completa del estudiante, un modelo de Programas con su descripción y 
        un modelo de Inscripción que asocia alumnos con programas.
    """,
    'author': 'Agustin Lorca',
    'company': 'ADEN',
    'website': '',
    'category': 'Educación',
    'depends': ['base'],
    'data': [
        #'security/ir.model.access.csv',
    ],
    'application': True,
}
