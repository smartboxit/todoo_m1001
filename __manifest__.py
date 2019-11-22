# -*- coding: utf-8 -*-
{
    'name': "zemployee_car_request",

    'summary': """
        Substance: The experience of any change requires not only the perception of the altered qualities that constitute the change but also the concept of an underlying substance which persists through this alteration. 
        (E.g., in order to know by experience that the classroom wall has changed in color from blue to yellow, 
        I must not only perceive the different colors—blue then, yellow now—but also suppose that the wall itself has endured from then until now.) 
        Thus, Kant supposed that the philosophical concept of substance (reflected in the scientific assumption of an external world of material objects) is an a priori condition for our experience.""",

    'description': """
        This apps Intended for use internal only
    """,

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
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}