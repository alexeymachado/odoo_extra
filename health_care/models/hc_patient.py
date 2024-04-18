from odoo import api, fields, models

class HCPatient(models.Model):
    _inherit = ['res.partner']
        
    resident_type = fields.Char()
    is_patient=fields.Boolean()

    gender = fields.Selection(selection=[('M', 'Masculine'), ('F', 'Femenine')])
    gender_str = fields.Char()
    state_str= fields.Char()
    race = fields.Selection(selection=[('W', 'White'), ('B', 'Black'), ('M', 'Meztiza')])

    birthday = fields.Date()
    age = fields.Integer(compute='_compute_age')
    primary_language = fields.Char()

    ssn = fields.Char(string='Social Security Number')
    
    emergency_contact_ids=fields.One2many(comodel_name='hc.patient.contact',inverse_name='patient_id')

    @api.depends('birthday')
    def _compute_age(self):
        for record in self:
            if record.birthday:
                record.age = fields.Date.today().year-record.birthday.year
                if fields.Date.today() > record.birthday:
                    record.age -= 1
            else:
                record.age = 0
  

