# -*- coding: utf-8 -*-
{
    'name': "zemployee_car_request",

    'summary': "Aplikasi pemesanan mobil untuk keluar kantor via HRD dan GA",
        

    'description': "This apps Intended for use internal only",
        
    

    'author': "My Best Company Ever",
    'website': "http://www.linknet.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','fleet'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}