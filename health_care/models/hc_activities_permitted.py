from odoo import _, api, fields, models



class HCActivitiesPermitted(models.Model):
    _name = 'hc.activities.permitted'
    _description = 'HCActivitiesPermitted'

    name = fields.Char()
    description = fields.Char()
    
