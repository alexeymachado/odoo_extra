from odoo import _, api, fields, models


class HCIntake(models.Model):
    _name = 'hc.intake'
    _description = 'Intake'

    patient_id = fields.Many2one(comodel_name='hc.patient')

    state = fields.Selection(selection=[('Inicio', 'Inicio'), ('Progreso', 'Progreso'), (
        'Cancelada', 'Cancelada'), ('Aprobada', 'Aprobada'), ('Terminada', 'Terminada')], default='Inicio')

    start_date = fields.Date()
    end_date = fields.Date()

    hospital_id = fields.Many2one(comodel_name='hc.facility')
    admit_date = fields.Date()
    discharge_date = fields.Date()

    start_care_date = fields.Date()

    insurance_aproved = fields.Boolean()

    referal_source = fields.Char()
    admin_date = fields.Date()
    discharge_date = fields.Date()

    diets = fields.Text()
    allergies = fields.Text()

    note_file = fields.Binary()
    note_emited_date = fields.Date()
    note_received_date = fields.Date()
    note_diagnostic_primary = fields.Char()
    note_diagnostic_secondary = fields.Char()
    note_physician_id = fields.Many2one(comodel_name='hc.physician')
    note_observation = fields.Text()

    order_file = fields.Binary()
    order_emited_date = fields.Date()
    order_recibed_date = fields.Date()
    order_physician_id = fields.Many2one(comodel_name='hc.physician')
    order_observacion = fields.Text()

    disciplines = fields.Char()
    disciplines_frecuencies = fields.Text()

    medicine_ids = fields.Many2many(
        comodel_name='hc.medicine', relation='hc_intake_medicine', column1='intake_id', column2='medicine_id')
    contact_ids = fields.Many2many(
        comodel_name='hc.contact', relation='hc_intake_contact', column1='intake_id', column2='contact_id')
    discipline_ids = fields.Many2many(
        comodel_name='hc.discipline', relation='hc_intake_discipline', column1='intake_id', column2='discipline_id')

    visit_ids = fields.One2many(
        comodel_name='hc.visit', inverse_name='intake_id')

    physician_id = fields.Many2one(comodel_name='hc.physician')
    case_manager_id = fields.Many2one(comodel_name='hc.contact')
