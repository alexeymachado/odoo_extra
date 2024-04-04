from odoo import _, api, fields, models


class HCSupply(models.Model):
    _name = 'hc.supply'
    _description = 'HC Supply'

    name = fields.Char()
    description = fields.Text()
