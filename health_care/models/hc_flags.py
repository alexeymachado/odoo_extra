from odoo import _, api, fields, models


class HCFlags(models.Model):
    _name = 'hc.flags'
    _description = 'HC Flags'

    name = fields.Char()
    description = fields.Char()
