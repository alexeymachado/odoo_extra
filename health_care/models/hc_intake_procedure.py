from odoo import api, fields, models

class HCIntakeProcedure(models.Model):
    _name = 'hc.intake.procedure'
    _description = 'Intake Procedure'
    
    
    intake_id = fields.Many2one(comodel_name='hc.intake')
    procedure_id = fields.Many2one(comodel_name='hc.procedure')

    def create(self, vals_list):
        intake_procedure = super().create(vals_list)
        
        for supply in self.procedure_id.supply_ids:
            if not self.env['hc.intake_supply'].search([('intake_id','=',self.intake_id),('supply_id', '=', supply.id)]):
                intake_supply = self.env['hc.intake_supply'].create({
                    'intake_id': self.intake_id,
                    'supply_id': supply.id
                })
        
        return intake_procedure            



    
