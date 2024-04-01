from odoo import api, fields, models

class HCMedicine(models.Model):
    _name = 'hc.medicine'
    _description = 'HC Medicine'

    name = fields.Char()
    family_id = fields.Many2one(comodel_name='hc.medicine.family')

    
