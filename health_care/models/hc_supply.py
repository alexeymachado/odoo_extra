from odoo import _, api, fields, models


class HCSupply(models.Model):
    _name = 'hc.supply'
    _description = 'HC Supply'

    name = fields.Char()
    description = fields.Text()

    def create(self, vals_list):
        print('Estoy aqui')
        return super().create(vals_list)
