from odoo import api, fields, models

class HCNurse(models.Model):
    _name = 'hc.nurse'
    _description = 'Nurse Model'

    _inherits={'hc.contact':'contact_id'}

    contact_id = fields.Many2one(comodel_name='hc.contact', required=True, ondelete='cascade')



   

    



    
    
    



