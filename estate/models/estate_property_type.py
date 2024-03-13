from odoo import fields, models

class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Tipos de Propiedad'
    name = fields.Char(required=True) 
    property_ids = fields.One2many(comodel_name='estate.property', inverse_name='type_id')   
