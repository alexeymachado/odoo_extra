from odoo import api, fields, models

class HCInsurancePlan(models.Model):
    _name = 'hc.insurance.plan'
    _description = 'Insurance Plan'

    name = fields.Char()