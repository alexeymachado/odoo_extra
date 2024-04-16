from odoo import models, fields, _
import openpyxl
import base64
from io import BytesIO
from odoo.exceptions import UserError
from datetime import datetime



class HCTaskImport(models.TransientModel):

    _name = "hc.task.import"
    _description = 'Task Import'

    file = fields.Binary(string="File", required=True)


    def task_import(self):
        try:
            wb = openpyxl.load_workbook(BytesIO(base64.b64decode(self.file)), read_only=True)
            ws = wb.active

            #Busca el Id del facility_type Farmacia y si no esta lo crea 
            facility_type_id = self.env['hc.facility.type'].search([('name','=','farmacy')]).id
            if not facility_type_id:
                facility_type_id = self.env['hc.facility.type'].create({'name':'farmacy'}).id


            
            for record in ws.iter_rows(min_row=2,values_only=True):

                # Procesando Patient
                
                patient = self.env['hc.patient'].search([('mrn', '=', record[0])])

                if not patient:
                    patiend = self.env['hc.patient'].create({
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

                # Procesando tipo relacion de contactos

                relation_name = str(record[16]).title()

                relation = self.env['hc.contact.relation'].search([('name', '=', relation_name)])
                if not relation:
                    relation = self.env['hc.contact.relation'].create({'name':relation_name})

                # Procesando Contactos del Paciente

                contact_name = str(record[15]).title()
                contact = self.env['hc.patient.contact'].search([('name', '=', contact_name)])
                if not contact:
                    contact=self.env['hc.patient.contact'].create({
                        'patient_id':patiend.id,
                        'contact_relation_id':relation.id,
                        'name':contact_name,
                        'phone': record[17],
                        'address': record[18],
                        'city': record[19],
                        'state': record[20],
                        'zip_code': record[21],
                        })

                # Procesando farmacia (facility)

                farmacy_name = str(record[22]).title()
                farmacy_phone = record[23]    
                
                facility = self.env['hc.facility'].search([('name', '=', farmacy_name),('facility_type_id','=',facility_type_id)])
                if not facility:
                    facility = self.env['hc.facility'].create({'name':farmacy_name, 'facility_type_id':facility_type_id})

                if facility.phone:
                    if facility.phone.find(farmacy_phone)==-1:
                        facility.phone+=", " + farmacy_phone    
                else:
                    facility.phone=farmacy_phone

                                
                # Procesando physician

                physician_name = str(record[34]).title()
                physician = self.env['hc.physician'].search([('name','=',physician_name)])
                if not physician:
                    physician=self.env['hc.physician'].create({
                        'name':physician_name,
                        'npi': record[35],
                        'phone': record[36],
                        'facsimile': record[37]
                    })

                # Procesando Branch

                branch_name = str(record[39]).title()
                branch = self.env['hc.branch'].search([('name','=',branch_name)])
                if not branch:
                    branch=self.env['hc.branch'].create({
                        'name':branch_name,
                        'npi': record[35],
                    }) 

                # Procesando Intake

                intake = self.env['hc.intake'].create({
                    'start_date': datetime.strptime(record[25], "%m/%d/%Y").date(), 
                    'end_date': datetime.strptime(record[26], "%m/%d/%Y").date(), 
                    'start_care_date': datetime.strptime(record[24], "%m/%d/%Y").date(), 
                    'note_diagnostic_primary': str(record[28]).title(),
                    'note_diagnostic_secondary': str(record[29]).title(),
                    'disciplines': str(record[30]).title(),
                    'disciplines_frecuencies': str(record[31]).title(),
                    'patient_id': patient.id,
                    'physician_id': physician.id
                })    
        except: 
            # raise UserError(_('Please insert a valid file'))
            raise

