# -*- coding: utf-8 -*-
{
    'name': "Purchase Order Line Wizard",

    'summary': """
        Library Managment
     """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Andres D Amelio",
    'website': "http://www.andresdamelio.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Product',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['purchase'],

    # always loaded
    'data': [
        'wizard/purchase_order_line_view.xml',
    ],
    'installable' : True,
    'application': True
    # only loaded in demostration mode

}