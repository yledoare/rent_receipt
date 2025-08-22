# -*- coding: utf-8 -*-
{
    'name': "rent_receipt_property_management",
    'summary': "Print rental receipt ",
    'description': """
Long description of module's purpose
    """,
    'author': "OS4B",
    'website': "https://www.os4b.com",

    'category': 'Rental',
    'version': '0.1',

    'depends': [
        'base',
        'contacts',
    ],

    'data': [
        # SECURITY
        'security/res_groups.xml',
        'security/ir_rule.xml',
        'security/ir.model.access.csv',
        # VIEWS
        'views/rent_receipt_property_views.xml',
        'views/res_partner_views.xml',
        'views/rent_receipt_location.xml',
        #REPORT
        'report/rent_receipt_location_report.xml',
        'report/rent_receipt_location_report_template.xml',
        # MENU
        'views/menu.xml',
    ],

}

