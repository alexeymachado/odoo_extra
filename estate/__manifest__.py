# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Estate',
    'version' : '0.1',
    'summary': 'Estate',
    'sequence': 10,
    'description': "Aplicación de Estate",
    'category': 'extra',
    'website': 'https://www.odoo.com/app/invoicing',
    'depends': ['base'],
    'data': [
        'security\ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_menuitem.xml'
    ],
    'installable': False,
    'application': False,
    'assets': {
    },
    'license': 'LGPL-3',
}
