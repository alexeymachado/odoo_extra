from odoo import api, fields, models

class HCPatientContact(models.Model):
    _name = 'hc.patient.contact'
    _description = 'Patient Contact Model'

    patient_id = fields.Many2one(comodel_name='hc.patient', required=True, ondelete='cascade')
    contact_id = fields.Many2one(comodel_name='hc.contact', required=True, ondelete='cascade')
    contact_relation_id = fields.Many2one(comodel_name='hc.contact.relation', required=True, ondelete='cascade') 
    

    
    



    
    
    



