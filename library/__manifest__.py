# -*- coding: utf-8 -*-
{
    'name': "Library Managment",

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
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/library_book_view.xml',
        'views/library_book_category_view.xml',
        # 'views/templates.xml',
    ],
    'installable' : True,
    # only loaded in demostration mode

}