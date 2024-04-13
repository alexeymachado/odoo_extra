from odoo import api, fields, models


class HCContact(models.Model):
    _name = 'hc.contact'
    _description = 'HC Contact'

    name = fields.Char()
    first_name = fields.Char(string='First Name')  # Nombre
    last_name = fields.Char(string='Last Name')  # Apellidos
    
    sex = fields.Selection(selection=(('M', 'Masculino'), ('F', 'Femenino')))
    gender = fields.Char(string='Gender')
    race = fields.Selection(selection=(('W', 'White'), ('B', 'Black'), ('M', 'Meztiza')))

    birth_day = fields.Date()
    age = fields.Integer(compute='_compute_age')
    primary_language = fields.Char()
    
    ssn = fields.Char(string='Social Security Number')

    
    address = fields.Char()
    city = fields.Char()
    state = fields.Char()
    zip_code = fields.Char()
    email = fields.Char()
    phone = fields.Char()
    facsimile = fields.Char()

    @api.depends('birth_day')
    def _compute_age(self):
        for record in self:
            if record.birth_day:
                record.age = fields.Date.today().year-record.birth_day.year
                if fields.Date.today() > record.birth_day:
                    record.age -= 1
            else:
                record.age = 0

    def button_details(self):
        view = {
            'name': 'Edit Contact',
            'domain': [],
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'hc.contact',
            'view_id': False,
            'type': 'ir.actions.act_window',
            # 'target': 'new',
            'readonly': True,
            'res_id': self.id,
        }
        return view
