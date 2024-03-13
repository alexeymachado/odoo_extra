from odoo import _, api, fields, models

class HCVisit(models.Model):
    _name = 'hc.visit'
    _description = 'Visit'
    date = fields.Date()
    type_id = fields.Many2one(comodel_name='hc.visit.type')
    intake_id = fields.Many2one(comodel_name ='hc.intake')
    nurse_id = fields.Many2one(comodel_name ='hc.nurse')
    resume = fields.Text()



