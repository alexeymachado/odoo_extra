from odoo import _, api, fields, models

class HCVisitType(models.Model):
    _name = 'hc.visit.type'
    _description='Visit Type'
    name = fields.Char()
    description = fields.Char()
