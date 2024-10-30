from odoo import http
from odoo.http import request


class InscripcionController(http.Controller):
    @http.route('/gestion_estudiantil/programa/<int:programa_id>/alumnos', auth='user', methods=['GET'])
    def alumnos_por_programa(self, programa_id):
        programa = request.env['gestion_estudiantil.programa'].browse(
            programa_id)
        if not programa.exists():
            return request.make_json_response({'error': 'El programa no existe'})

        inscripciones = request.env['gestion_estudiantil.inscripcion'].search(
            [('programa_id', '=', programa.id)]
        ).mapped('alumno_id')
        alumnos_data = []
        for alumno in inscripciones:
            alumnos_data.append({
                'nombre': alumno.nombre,
                'apellido': alumno.apellido,
                'fecha_nacimiento': alumno.fecha_nacimiento,
                'nro_legajo': alumno.legajo,
                'email': alumno.email,
                'telefono': alumno.telefono,
                'direccion': alumno.direccion,
                'pais': alumno.pais,
            })
        if not alumnos_data:
            return request.make_json_response({'error': 'No hay inscriptos en este programa'})
        return request.make_json_response(alumnos_data)
