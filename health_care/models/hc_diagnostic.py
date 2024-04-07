from odoo import _, api, fields, models

class HCDiagnostic(models.Model):
    _name = 'hc.diagnostic'
    _description = 'HCDiagnostic'
    name = fields.Char()
    code = fields.Char()
    procedure_ids= fields.Many2many(comodel_name='hc.procedure')
