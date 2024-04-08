from odoo import api, fields, models


class HCIntakeProcedure(models.Model):
    _name = 'hc.intake.procedure'
    _description = 'Intake Procedure'

    intake_id = fields.Many2one(comodel_name='hc.intake')
    procedure_id = fields.Many2one(comodel_name='hc.procedure')
