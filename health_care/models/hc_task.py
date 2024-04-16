from odoo import _, api, fields, models


class HCVisit(models.Model):
    _name = 'hc.task'
    _description = 'Task'
    intake_id = fields.Many2one(comodel_name='hc.intake')

    name = fields.Char()
    type_id = fields.Many2one(comodel_name='hc.task.type')
    
    date = fields.Date()
    time_in = fields.Datetime()
    time_out = fields.Datetime()
    time_doc = fields.Datetime(string='Documentation Time')
    time_travel = fields.Datetime(string='Travel Time')
    comment = fields.Text()

    employee_id = fields.Many2one(comodel_name='hr.employee')
    