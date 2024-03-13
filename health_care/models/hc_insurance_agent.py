from odoo import api, fields, models

class HCInsuranceAgent(models.Model):
    _name = 'hc.insurance.agent'
    _description = 'Insurance Agent'

    name = fields.Char()