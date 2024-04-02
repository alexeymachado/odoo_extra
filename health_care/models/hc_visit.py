from odoo import _, api, fields, models


class HCVisit(models.Model):
    _name = 'hc.visit'
    _description = 'Visit'
    intake_id = fields.Many2one(comodel_name='hc.intake')

    date = fields.Date()
    type_id = fields.Many2one(comodel_name='hc.visit.type')
    nurse_id = fields.Many2one(comodel_name='hc.nurse')
    resume = fields.Text()