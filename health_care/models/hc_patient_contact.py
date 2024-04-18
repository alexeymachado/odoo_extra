# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class HCPatientContact(models.Model):
    _name = 'hc.patient.contact'
    _description = _('Hc Patient Contact')

    patient_id = fields.Many2one(comodel_name='res.partner', domain=[('is_patient','=','true')])
    contact_id = fields.Many2one(comodel_name='res.partner')
    relation_id = fields.Many2one(comodel_name='hc.contact.relation')
    observation = fields.Text()

