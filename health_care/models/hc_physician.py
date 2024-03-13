from odoo import api, fields, models

class HCPhysician(models.Model):
    _name = 'hc.physician'
    _description = 'Physician Model'

    _inherits={'hc.contact':'contact_id'}
    contact_id = fields.Many2one(comodel_name='hc.contact', required=True, ondelete='cascade')

    upin = fields.Char(help='Unique Physician Identification Number (UPIN)', size=6)
    npi = fields.Char(help='National Provider Identifier (NPI)', size=10)
    state_license = fields.Char()
    state_license_expiration_date = fields.Date()
    state_license_str = fields.Char()
    contact_txt = fields.Char()


    
    