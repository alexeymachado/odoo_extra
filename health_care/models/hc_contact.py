from odoo import api, fields, models

class HCContact(models.Model):
    _name = 'hc.contact'
    _description = 'HC Contact'

    name = fields.Char()
    first_name= fields.Char(string='First Name') # Nombre
    last_name = fields.Char(string='Last Name') # Apellidos
    gender = fields.Char(string='Gender')
    birth_day=fields.Date()
    primary_language= fields.Char()
    age = fields.Integer(compute='_compute_age')
    ssn = fields.Char(string='Social Security Number')
    phone = fields.Char()
    address=fields.Char()
    city = fields.Char()
    state = fields.Char()
    zip_code=fields.Char()
    email_address = fields.Char()

    @api.depends('birth_day')
    def _compute_age(self):
        for record in self:
            if record.birth_day:
                record.age = fields.Date.today().year-record.birth_day.year
                if fields.Date.today()>record.birth_day:
                    record.age-=1
            else:
                record.age=0    


   

    



    
    
    



