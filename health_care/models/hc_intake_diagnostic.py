from odoo import _, api, fields, models



class HCIntakeDiagnostic(models.Model):
    _name = 'hc.intake.diagnostic'
    _description = 'HC Intake Diagnostic'

    intake_id = fields.Many2one(comodel_name='hc.intake')
    diagnostic_id = fields.Many2one(comodel_name='hc.diagnostic')
    observation = fields.Text()
