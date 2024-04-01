from odoo import api, fields, models


class HCPatientContact(models.Model):
    _name = 'hc.patient.contact'
    _description = 'Patient Contact Model'

    _inherits = {'hc.contact': 'contact_id'}

    contact_id = fields.Many2one(comodel_name='hc.contact', required=True, ondelete='cascade')
    patient_id = fields.Many2one(comodel_name='hc.patient', required=True, ondelete='cascade')

    contact_relation_id = fields.Many2one(string='relation', comodel_name='hc.contact.relation', required=True, ondelete='cascade')
