from odoo import api, fields, models

class HCNotAdmittedReason(models.Model):
    _name = 'hc.not.admitted.reason'
    _description = 'HC Not Admitted Reason'

    name = fields.Char()
    description = fields.Char()


           
