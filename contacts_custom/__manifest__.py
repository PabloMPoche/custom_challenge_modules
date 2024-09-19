# -*- coding: utf-8 -*-
{
    'name': 'Contacts Custom',
    'version': '1.0',
    'summary': 'Add customization for contacts module.',
    'description': 'Add customization for contacts module.',
    'category': 'Sales/CRM',
    'author': 'Pablo Yoel Mercedes Poché',
    'license': 'LGPL-3',
    'depends': [
        'contacts',
    ],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
