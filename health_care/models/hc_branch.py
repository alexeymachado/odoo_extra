from odoo import api, fields, models


class HCBranch(models.Model):
    _name = 'hc.branch'
    _description = 'HC Branch'
    name = fields.Char()
    npi = fields.Char()
    description = fields.Char()
