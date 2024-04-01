from odoo import api, fields, models

class HCPatientInsurance(models.Model):
    _name = 'hc.patient.insurance'
    _description = 'Patient Insurance Model'


    patient_id = fields.Many2one(comodel_name='hc.patient', required=True, ondelete='cascade')
    insurance_agent_id = fields.Many2one(comodel_name='hc.insurance.agent', required=True, ondelete='cascade')
    insurance_plan_id = fields.Many2one(comodel_name='hc.insurance.plan', required=True, ondelete='cascade')
    