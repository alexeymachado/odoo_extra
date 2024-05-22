from odoo import _, api, fields, models


class HCIntake(models.Model):
    _name = 'hc.intake'
    _description = 'Intake'
    _inherit=['mail.thread', 'mail.activity.mixin', 'avatar.mixin']
  
    state = fields.Selection(selection=[('referral', 'Referral'), ('eligibility', 'Eligibility'), 
        ('intake', 'Intake'), ('admission', 'Admission'), ('finished', 'Finished')], default='referral')
    
    active = fields.Boolean('Active', default=True, tracking=True)

    user_id = fields.Many2one('res.users', string='Salesperson', default=lambda self: self.env.user,  tracking=True)
    not_admitted_reason_id = fields.Many2one(comodel_name='hc.not.admitted.reason')

    referral_id = fields.Many2one(comodel_name='res.partner')

    facility_id = fields.Many2one(comodel_name='hc.facility')
    facility_admit_date = fields.Date()
    facility_discharge_date = fields.Date()

    patient_id = fields.Many2one(comodel_name='res.partner', domain=[('is_patient','=',True)])
   
    name = fields.Char(related='patient_id.name', string="Name", readonly=False, traking=True)
    
    pat_street = fields.Char(related='patient_id.street', string="Street")
    pat_city = fields.Char(related='patient_id.city', string="City")
    pat_state = fields.Char(related='patient_id.state_str', string="State")
    pat_zip_code = fields.Char(related='patient_id.zip', string="Zip")

    insurance_agent_id = fields.Many2one(comodel_name='hc.insurance.agent', ondelete='cascade')
    insurance_plan_id = fields.Many2one(comodel_name='hc.insurance.plan', ondelete='cascade')
    insurance_number = fields.Char()
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
    
    start_date = fields.Date(default=fields.Date.today())
    estimated_len_of_stay = fields.Integer()
    estimated_end_date = fields.Date()
    
    mrn = fields.Char(string='MRN')
    hic = fields.Char(string='HIC')
    
    functional_limitation_ids = fields.Many2many(comodel_name='hc.functional.limitation')
    flags_ids = fields.Many2many(comodel_name='hc.flags')
    activities_permitted = fields.Many2many(comodel_name='hc.activities.permitted')
    weight_bearing = fields.Selection([('full', 'Full'),('partial', 'Partial'),('none','None')], default='none') 
    assistive_device = fields.Selection([('cane','Cane'),('walker','Walker'),('wheelchair','Wheel Chair')])
    diets = fields.Text()
    allergies = fields.Text()
   
    foley_catheter_insert = fields.Boolean()
    foley_catheter_insert_date = fields.Date()
    foley_catheter_size = fields.Char()

    laboratory_work = fields.Char()
    laboratory_frequency = fields.Char()
        
    diagnostic_ids= fields.One2many(comodel_name='hc.intake.diagnostic', inverse_name='intake_id')
    discipline = fields.Text()
    discipline_frec = fields.Text()
    discipline_ids = fields.One2many(comodel_name='hc.intake.discipline', inverse_name='intake_id')
    medicine_ids = fields.One2many(comodel_name='hc.intake.medicine', inverse_name='intake_id')
    task_ids = fields.One2many(comodel_name='hc.task', inverse_name='intake_id')
    procedure_ids = fields.Many2many(comodel_name='hc.procedure')
    supply_ids=fields.Many2many(comodel_name='hc.supply')

    health_care_reason = fields.Char()
    homebound_reason = fields.Char()
    estimated_len_of_stay = fields.Integer()

    coordinator_id = fields.Many2one(comodel_name='hr.employee')
    nurse_id = fields.Many2one (comodel_name='hr.employee')

    start_care_date = fields.Date()

    def set_wait_doc(self):
        self.write({'state':"wait_doc"})

    def set_no_admit(self):
        self.write({'state':"not_admitted"})  

    def set_admit(self):
        self.write({'state':"admitted"})

    def set_finish(self):
        self.write({'state':"finished"})          
