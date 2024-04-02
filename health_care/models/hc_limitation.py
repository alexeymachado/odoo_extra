from odoo import api, fields, models

class HCLimitation(models.Model):
    _name = 'hc.limitation'
    _description = 'Limitations'

    name = fields.Char()
    description = fields.Text()
    

    
    

    

