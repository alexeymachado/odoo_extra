from odoo import api, fields, models

class HCPhysician(models.Model):

    _inherit='res.partner'

    is_physician = fields.Boolean()
   
    upin = fields.Char(help='Unique Physician Identification Number (UPIN)', size=6)
    npi = fields.Char(help='National Provider Identifier (NPI)', size=10)
    license_file = fields.Binary()
    state_license = fields.Char()
    state_license_expiration_date = fields.Date()
    state_license_str = fields.Char()

    facsimile = fields.Char()

