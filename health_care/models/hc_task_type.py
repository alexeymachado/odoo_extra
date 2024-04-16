from odoo import _, api, fields, models

class HCVisitType(models.Model):
    _name = 'hc.task.type'
    _description='Task Type'
    name = fields.Char()
    description = fields.Char()
