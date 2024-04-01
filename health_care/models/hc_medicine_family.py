from odoo import api, fields, models

class HCMedicineFamily(models.Model):
    _name = 'hc.medicine.family'
    _description = 'HC Medicine Family'

    name = fields.Char()
    


    