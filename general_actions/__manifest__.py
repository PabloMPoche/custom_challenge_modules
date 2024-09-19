# -*- coding: utf-8 -*-
{
    'name': 'General Actions',
    'version': '1.0',
    'summary': 'Add custom usefull actions for odoo modules.',
    'description': 'Add custom usefull actions for odoo modules.',
    'category': 'Sales/CRM',
    'author': 'Pablo Yoel Mercedes Poché',
    'license': 'LGPL-3',
    'depends': [
        'contacts',
    ],
    'data': [
        'data/res_partner.xml',
        'data/service_cron.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
