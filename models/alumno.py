from odoo import models, fields


class Alumno(models.Model):
    _name = "gestion_estudiantil.alumno"
    _description = 'Alumnos'

    nombre = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellido', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de nacimiento', required=True)
    legajo = fields.Integer(string='Nro. de legajo', required=True)
    email = fields.Char(string='Email', required=True)
    telefono = fields.Char(string='Teléfono', required=True)
    direccion = fields.Char(string='Dirección', required=True)
    pais = fields.Char(string='País', required=True)
