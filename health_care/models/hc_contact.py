from odoo import api, fields, models


class HCContact(models.Model):
    _name = 'hc.contact'
    _description = 'HC Contact'

    name = fields.Char()
    first_name = fields.Char(string='First Name')  # Nombre
    last_name = fields.Char(string='Last Name')  # Apellidos
    gender = fields.Char(string='Gender')
    birth_day = fields.Date()
    primary_language = fields.Char()
    age = fields.Integer(compute='_compute_age')
    sex = fields.Selection(selection=(('M', 'Masculino'), ('F', 'Femenino')))
    race = fields.Selection(selection=(
        ('W', 'White'), ('B', 'Black'), ('M', 'Meztiza')))
    ssn = fields.Char(string='Social Security Number')
    phone = fields.Char()
    facsimile = fields.Char()
    address = fields.Char()
    city = fields.Char()
    state = fields.Char()
    zip_code = fields.Char()
    email = fields.Char()

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
