from odoo import api, fields, models

class HCFacility(models.Model):
    _name = 'hc.facility'
    _description = 'HC Facility'

    name = fields.Char()
    facility_type_id = fields.Many2one(comodel_name='hc.facility.type')
    phone = fields.Char()

class HCFacilityType(models.Model):
    _name = 'hc.facility.type'
    _description = 'HC Facility Type'

    name = fields.Char()

           
