from odoo import api, fields, models

class HCPatient(models.Model):
    _name = 'hc.patient'
    _description = 'Patient Model'

    # _inherits={'res.partner':'partner_id'}
    # partner_id = fields.Many2one('res.partner', required=True, ondelete='restrict', auto_join=True, index=True,
    #     string='Related Partner', help='Partner-related data of the user')



    _inherits={'hc.contact':'contact_id'}
    contact_id = fields.Many2one(comodel_name='hc.contact', required=True, ondelete='cascade')

    mrn = fields.Char(string='Medical Record Number')
    hic = fields.Char(string='HIC')
    medicaid = fields.Char()

    resident_type = fields.Char()

    emergency_contact_id = fields.Many2one(comodel_name='hc.contact')
    emergency_contact_relationship = fields.Char()

    



    
    
    



