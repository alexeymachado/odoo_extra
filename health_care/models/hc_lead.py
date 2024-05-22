# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class Lead(models.Model):
 
    _inherit = 'crm.lead'
    
    reference_by = fields.Char()
    facility_id = fields.Many2one(comodel_name='hc.facility')
    facility_admit_date = fields.Date()
    facility_discharge_date = fields.Date()

    insurance_agency_id = fields.Many2one(comodel_name='hc.insurance.agent', ondelete='cascade')
    insurance_number = fields.Char()
    insurance_plan_id = fields.Many2one(comodel_name='hc.insurance.plan', ondelete='cascade')
    insurance_aproved = fields.Boolean()

    physician_id = fields.Many2one(comodel_name='res.partner', domain=[('is_physician','=',True)])

    note_received_date = fields.Date(default=fields.Date.today())
    note_file_binary = fields.Binary()
    note_file_name = fields.Char()
    note_emitted_date = fields.Date()
    note_observation = fields.Text()

    order_received_date = fields.Date(default=fields.Date.today())
    order_file_binary = fields.Binary()
    order_file_name = fields.Char()
    order_emitted_date = fields.Date()
    order_observation = fields.Text()
