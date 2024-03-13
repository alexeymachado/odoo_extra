# -*- coding: utf-8 -*-
{
    'name': 'Health_Care',
    'version': '17.0.1.0',
    'description': """ Health_Care Description """,
    'summary': """ Health_care Summary """,
    'author': '',
    'website': '',
    'category': '',
    'depends': ['base', 'web'],
    'data': [ 
        'security/ir.model.access.csv',
        
        'views/hc_contact_views.xml',
        
        'views/hc_patient_views.xml',
        'views/hc_physician_views.xml',
        'views/hc_nurse_views.xml',
        'views/hc_visit_views.xml',
        'views/hc_visit_type_views.xml',

        'views/hc_intake_views.xml',
        
        'views/hc_menuitem.xml',
    ],
    'assets': {

    },
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
