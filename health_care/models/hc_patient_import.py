from odoo import models, fields, _
import openpyxl
import base64
from io import BytesIO
from odoo.exceptions import UserError
from datetime import datetime



class HCPatientImport(models.TransientModel):

    _name = "hc.patient.import"
    _description = 'Patient Import'

    file = fields.Binary(string="File", required=True)


    def patient_import(self):
        try:
            wb = openpyxl.load_workbook(BytesIO(base64.b64decode(self.file)), read_only=True)
            ws = wb.active

            #Busca el Id del facility_type Farmacia y si no esta lo crea 
            facility_type_id = self.env['hc.facility.type'].search([('name','=','farmacy')]).id
            if not facility_type_id:
                facility_type_id = self.env['hc.facility.type'].create({'name':'farmacy'}).id

          
            for record in ws.iter_rows(min_row=2,values_only=True):

                # Procesando Patient
                
                first_name = str(record[2]).title()
                last_name = str(record[1]).title()
                name = f"{last_name} {first_name}"

                patient = self.env['res.partner'].search([('name', '=', name)])
                
                if not patient:
                    patient = self.env['res.partner'].create({
                        'is_patient':True,
                        'last_name': last_name,
                        'first_name': first_name,
                        'name': name,
                        'gender_str': record[3],
                        'birthday': datetime.strptime(record[6], "%m/%d/%Y").date(),
                        'phone':record[8],
                        'street': record[10],
                        'city':record[11],
                        'state_str':record[12],
                        'zip':record[13],
                        'email': record[14],
                    })

                # Procesando tipo relacion de contactos

                relation_name = str(record[16]).title()

                relation = self.env['hc.contact.relation'].search([('name', '=', relation_name)])
                if not relation:
                    relation = self.env['hc.contact.relation'].create({'name':relation_name})

                # Creando Contacto Emergencia del Paciente    
                
                contact_name = str(record[15]).title() # Hay que buscar un campo llave más adecuado
                contact_phone =  record[17]

                contact = self.env['res.partner'].search([('name', '=', contact_name), ('phone','=', contact_phone)])
                                
                if not contact:
                    contact=self.env['res.partner'].create({
                        'name':contact_name,
                        'phone': contact_phone,
                        'street': record[18],
                        'city': record[19],
                        'state_str': record[20],
                        'zip': record[21]
                    })   

                # Creando la relacion del paciente con el contacto
                
                self.env['hc.patient.contact'].create({
                        'patient_id':patient.id,
                        'contact_id':contact.id,
                        'relation_id':relation.id
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
                physician = self.env['res.partner'].search([('name','=',physician_name)])
                if not physician:
                    physician=self.env['res.partner'].create({
                        'is_physician':True,
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

                start_date=datetime.strptime(record[25], "%m/%d/%Y").date()
                end_date = datetime.strptime(record[26], "%m/%d/%Y").date()
                start_care_date = datetime.strptime(record[24], "%m/%d/%Y").date()
           
                if (end_date > datetime.today().date()):
                    state= 'admitted'
                else:
                    state='finished' 



                intake = self.env['hc.intake'].create({
                    'mrn': record[0],
                    'hic': record[4],
                    'start_date': start_date, 
                    'end_date': end_date, 
                    'state': state,
                    'start_care_date': start_care_date, 
                    
                    #Se deben procesar las disciplina
                    'discipline': str(record[30]).title(),
                    'discipline_frec': str(record[31]).title(),

                    'patient_id': patient.id,
                    'physician_id': physician.id
                })    

                # Procesando Diagnostico Primario

                diagnostic_name = str(record[28]).title()
                diagnostic = self.env['hc.diagnostic'].search([('name','=',diagnostic_name)])
                if not diagnostic:
                    diagnostic = self.env['hc.diagnostic'].create({'name':diagnostic_name})

                self.env['hc.intake.diagnostic'].create({'intake_id':intake.id,'diagnostic_id': diagnostic.id,'observation': 'Primario'})    
                
                # Procesando Diagnostico Secundario

                diagnostic_name = str(record[29]).title()
                diagnostic = self.env['hc.diagnostic'].search([('name','=',diagnostic_name)])
                if not diagnostic:
                    diagnostic = self.env['hc.diagnostic'].create({'name':diagnostic_name})

                self.env['hc.intake.diagnostic'].create({'intake_id':intake.id,'diagnostic_id': diagnostic.id, 'observation': 'secundario',})   






        except: 
            # raise UserError(_('Please insert a valid file'))
            raise

