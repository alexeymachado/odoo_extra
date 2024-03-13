from odoo import api, fields, models

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Ofertas de Compra a la Propiedad'
    price = fields.Float(string="precio", required=True)
    status = fields.Selection(default="Aceptada", selection=[("Aceptada", "Aceptada"), ("Rechazada","Rechazada")])
    partner_id = fields.Many2one(comodel_name="res.partner")
    property_id = fields.Many2one(comodel_name="estate.property")
    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_date_deadline", inverse="_inverse_date_deadline", readonly=False, store=True)

    @api.depends('validity')
    def _compute_date_deadline(self):
        for record in self:
            if record.validity:
                record.date_deadline = fields.Date.add(record.create_date,days=record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            if record.date_deadline:
                record.validity = (record.date_deadline - record.create_date.date()).days

                