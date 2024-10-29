from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Inscripcion(models.Model):
    _name = 'gestion_estudiantil.inscripcion'
    _description = 'Inscripciones a programas'

    """
    Cada inscripción está relacionada con un único alumno, pero un alumno puede tener varias inscripciones a diferentes programas
    """
    alumno_id = fields.Many2one(
        'gestion_estudiantil.alumno', string='Alumno', required=True)

    """
    Cada inscripción está relacionada con un único programa, pero un programa puede tener varias inscripciones de diferentes alumnos
    """
    programa_id = fields.Many2one(
        'gestion_estudiantil.programa', string='Programa', required=True)

    # Método que verifica si un alumno ya se encuentra inscripto en un programa específico
    def alumno_inscripto(self, vals):
        if self.env['gestion_estudiantil.inscripcion'].search([
            ('alumno_id', '=', vals.get('alumno_id')),
            ('programa_id', '=', vals.get('programa_id'))
        ]):
            return True
        return False

    # Método que crea una inscripción
    @api.model
    def create(self, vals):
        if self.alumno_inscripto(vals):
            raise ValidationError('El alumno ya se encuentra inscripto en este programa.')
        return super(Inscripcion, self).create(vals)
