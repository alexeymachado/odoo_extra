from odoo import _, api, fields, models

class HCCertification(models.Model):
    _name = 'hc.certification'
    _description = 'HC Certification'

    name = fields.Char()
    description= fields.Text()

    

