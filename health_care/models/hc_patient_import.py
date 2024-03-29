from odoo import models, fields, _
import openpyxl
import base64
from io import BytesIO
from odoo.exceptions import UserError
from datetime import datetime



class HCPatientImport(models.TransientModel):

    _name = "hc.patient.import"
    file = fields.Binary(string="File", required=True)


    def patient_import(self):
        try:
            wb = openpyxl.load_workbook(BytesIO(base64.b64decode(self.file)), read_only=True)
            ws = wb.active
            for record in ws.iter_rows(min_row=2,values_only=True):

                # search if the customer exist else create
                # contact_id = self.env['hc.contac'].search([('first_name', '=', record[2]), ('last_name','=',record[1])])
                # if not contact_id:
                #     contact_id=self.env['hc.contact'].create({
                #         'first_name':record[2],
                #         'last_name':record[1]
                #         })

                
                
                search = self.env['hc.patient'].search([('mrn', '=', record[1])])

                if not search:
                    self.env['hc.patient'].create({
                        'mrn': record[0],
                        'hic': record[4],
                        'name': str(record[1] + ' ' + record[2]).title(),
                        'first_name': str(record[2]).title(),
                        'last_name': str(record[1]).title(),
                        'gender': record[3],
                        'birth_day': datetime.strptime(record[6], "%m/%d/%Y").date(),
                        'phone':record[8],
                        'address': record[10],
                        'city':record[11],
                        'state':record[12],
                        'zip_code':record[13],
                        'email': record[14],
                    })
        except: 
            raise UserError(_('Please insert a valid file'))

