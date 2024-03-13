# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class Eeee(models.TransientModel):
    _name = 'eeee'
    _description = _('Eeee')

    name = fields.Char(_('Name'))

    def add(self):
        _logger.info('Hello Wizard')
