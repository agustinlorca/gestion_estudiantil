from odoo import models, fields


class Programa(models.Model):
    _name = "gestion_estudiantil.programa"
    _description = "Programas"

    nombre = fields.Char(string="Nombre", required=True)
    descripcion = fields.Text(string="Descripción", required=True)
