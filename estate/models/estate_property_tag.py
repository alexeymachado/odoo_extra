from odoo import fields, models

class EstatePropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'tag propiedades'
    name = fields.Char(required=True)
