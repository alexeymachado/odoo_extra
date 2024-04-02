from odoo import _, api, fields, models



class HCNurseCategory(models.Model):
    _name = 'hc.nurse.category'
    _description = 'model.technical.name'
    name = fields.Char()
    observation = fields.Text()
    

