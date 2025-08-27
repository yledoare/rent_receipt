# -*- coding: utf-8 -*-
{
    'name': "Rental receipt",
    'summary': "Print rental receipt ",
    'description': """
Long description of module's purpose
    """,
    'author': "OS4B",
    'website': "https://www.os4b.bzh",

    'category': 'Rental',
    'version': '0.7',

    'depends': [
        'base',
        'contacts',
    ],

    'data': [
        # SECURITY
        'security/ir.model.access.csv',
        # VIEWS
        'views/rent_receipt_property_views.xml',
        'views/rent_receipt_location.xml',
        #REPORT
        'report/rent_receipt_location_report.xml',
        'report/rent_receipt_location_report_template.xml',
        # MENU
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',

}

