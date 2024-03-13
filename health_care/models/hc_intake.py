from odoo import _, api, fields, models


class HCIntake(models.Model):
    _name = 'hc.intake'
    _description = 'Intake'
    
    state = fields.Selection(selection=[('Inicio', 'Inicio'), ('Aprobada', 'Aprobada'), ('Cancelada', 'Cancelada'), ('Terminada', 'Terminada')], default='Inicio')
    patient_id = fields.Many2one(comodel_name='hc.patient')
    start_date = fields.Date()
    end_date = fields.Date()
    visit_ids = fields.One2many(comodel_name='hc.visit', inverse_name='intake_id')
    insurance_aproved = fields.Boolean()
    contacts_ids = fields.Many2many(comodel_name='hc.contact')

    
    

