from odoo import api, fields, models
from odoo.exceptions import UserError, AccessError

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"
    active = fields.Boolean(default=True)
    estado = fields.Selection(selection=[ ('new', 'New'), ('offer received', 'Offer received'), ('offer accepted', 'Offer Accepted'), ('sold','Sold'), ('canceled', 'Canceled')], default='new', copy=False)

    name = fields.Char()
    description = fields.Text()
    postcode=fields.Char()
    date_availability=fields.Date(string="Available From", copy=False, default=fields.Date.add(fields.Date.today(),months=3))
    expected_price=fields.Float()
    selling_price=fields.Float(copy=False, readonly=True)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(string="Living Area (Ssqm)")
    facades = fields.Integer()
    garage=fields.Boolean()
    garden=fields.Boolean()
    garden_area=fields.Integer()
    garden_orientation=fields.Selection(selection=[('north','North'), ('south','South'), ('east', 'East'), ('west', 'West')])
    total_area = fields.Integer(compute="_compute_total_area", string="Area Total")
    prueba = fields.Char()
    type_id = fields.Many2one(comodel_name="estate.property.type", string="Tipo")
    comprador_id = fields.Many2one(comodel_name="res.partner", copy=False)
    vendedor_id = fields.Many2one(comodel_name="res.users", default=lambda self: self.env.user)
    tag_ids = fields.Many2many(comodel_name="estate.property.tag")
    offer_ids= fields.One2many(comodel_name="estate.property.offer",inverse_name="property_id")
    best_price = fields.Float(compute="_compute_best_price", string="Mejor Precio")

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area+record.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            if record.offer_ids:
                record.best_price = max(record.offer_ids.mapped('price')) 
            else:
                record.best_price=0          

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area=100
            self.garden_orientation='north'  
        else:
            self.garden_area=0
            self.garden_orientation=''

    def action_cancel(self):
        if self.estado!='sold':
            self.estado='canceled'
        else:
            raise UserError("No se puede cancelar una propiedad vendida")  
        
    def action_sold(self):
        if self.estado!='canceled':
            self.estado='sold'
        else:
            raise UserError("No se puede vender una propiedad cancelada")  
 

                      
