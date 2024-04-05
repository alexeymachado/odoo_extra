from odoo import api, fields, models

class HCFunctionalLimitation(models.Model):
    _name = 'hc.functional.limitation'
    _description = 'Functional Limitations'

    name = fields.Char()
    description = fields.Text()
    

    
    

    

