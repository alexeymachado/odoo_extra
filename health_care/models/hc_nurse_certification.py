from odoo import _, api, fields, models



class HCNurseCertification(models.Model):
    _name = 'hc.nurse.certification'
    _description = 'HC Nurse Certification'

    nurse_id = fields.Many2one(comodel_name='hc.nurse')
    certification_id = fields.Many2one(comodel_name='hc.certification')
    
    emit_date=fields.Date()
    expiration_date = fields.Date()
    observation = fields.Text()
    

