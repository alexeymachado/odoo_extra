from odoo import _, api, fields, models


class HCIntake(models.Model):
    _name = 'hc.intake'
    _description = 'Intake'

    
    state = fields.Selection(selection=[('new', 'New'), ('wait_doc', 'Wait Documentation'), (
        'no_admit', 'NO Admit'), ('admit', 'Admit'), ('finished', 'Finished')], default='new')

    start_date = fields.Date()
    end_date = fields.Date()
    no_admit_reason = fields.Char()

    referral_id = fields.Many2one(comodel_name='hc.contact')

    patient_id = fields.Many2one(comodel_name='hc.patient')

    facility_id = fields.Many2one(comodel_name='hc.facility')
    facility_admit_date = fields.Date()
    facility_discharge_date = fields.Date()

    insurance_agent_id = fields.Many2one(comodel_name='hc.insurance.agent', ondelete='cascade')
    insurance_plan_id = fields.Many2one(comodel_name='hc.insurance.plan', ondelete='cascade')
    insurance_number = fields.Char()
    insurance_aproved = fields.Boolean()

    physician_id = fields.Many2one(comodel_name='hc.physician')

    note_file_binary = fields.Binary()
    note_file_name = fields.Char()
    note_emited_date = fields.Date()
    note_received_date = fields.Date()
    note_observation = fields.Text()

    order_file_binary = fields.Binary()
    order_file_name = fields.Char()
    order_emited_date = fields.Date()
    order_received_date = fields.Date()
    order_observation = fields.Text()
    

    functional_limitation_ids = fields.Many2many(comodel_name='hc.functional.limitation')
    flags_ids = fields.Many2many(comodel_name='hc.flags')
    activities_permitted = fields.Many2many(comodel_name='hc.activities.permitted')
    weight_bearing = fields.Selection([('full', 'Full'),('partial', 'Partial'),('none','None')]) 
    assistive_device = fields.Selection([('cane','Cane'),('walker','Walker'),('wheelchair','Wheel Chair')])
    diets = fields.Text()
    allergies = fields.Text()
   
    foley_catheter_insert = fields.Boolean()
    foley_catheter_insert_date = fields.Date()
    foley_catheter_size = fields.Char()

    laboratory_work = fields.Char()
    laboratory_frequency = fields.Char()
    
    
    diagnostic_ids= fields.One2many(comodel_name='hc.intake.diagnostic', inverse_name='intake_id')
    discipline_ids = fields.One2many(comodel_name='hc.intake.discipline', inverse_name='intake_id')
    medicine_ids = fields.One2many(comodel_name='hc.intake.medicine', inverse_name='intake_id')
    visit_ids = fields.One2many(comodel_name='hc.visit', inverse_name='intake_id')


    health_care_reason = fields.Char()
    homebound_reason = fields.Char()
    estimated_len_of_stay = fields.Integer()

    coordinator_id = fields.Many2one(comodel_name='hc.contact')
    nurse_id = fields.Many2one (comodel_name='hc.nurse')

    start_care_date = fields.Date()

    


