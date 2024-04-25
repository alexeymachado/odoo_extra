from odoo import api, fields, models


class HCContact(models.Model):

    _inherit = 'res.partner'

    # Esta clase añade información de caracter personal a partner, esto es lo que hace employee con su clase employee_private.
    # Pero los objetos patient y physician no son empleados.

    first_name = fields.Char()
    last_name = fields.Char()
    full_name = fields.Char(compute="_compute_full_name")
    
    def _compute_full_name(self):
        return "{self.first_name}, {self.last_name}"

    # def button_details(self):
    #     view = {
    #         'name': 'Edit Contact',
    #         'domain': [],
    #         'view_type': 'form',
    #         'view_mode': 'form',
    #         'res_model': 'res.partner',
    #         'view_id': False,
    #         'type': 'ir.actions.act_window',
    #         # 'target': 'new',
    #         'readonly': True,
    #         'res_id': self.id,
    #     }
    #     return view

