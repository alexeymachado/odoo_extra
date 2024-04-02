from odoo import api, fields, models

class HCIntakeDiscipline(models.Model):
    _name = 'hc.intake.discipline'
    _description = 'Intake Discipline'
    
    intake_id = fields.Many2one(comodel_name='hc.intake')
    discipline_id = fields.Many2one(comodel_name='hc.discipline')
    frecuencia = fields.Char()
    observacion = fields.Char()

    
