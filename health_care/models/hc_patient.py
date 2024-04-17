from odoo import api, fields, models

class HCPatient(models.Model):
    _inherit = 'res.partner'
        
    resident_type = fields.Char()

    def patient_import(Self):
        Self.env['hc.patient.import'].patient_import()

