from odoo import api, fields, models

class HCDiscipline(models.Model):
    _name = 'hc.discipline'
    _description = 'Discipline'
    name = fields.Char()
    description = fields.Char()





   
