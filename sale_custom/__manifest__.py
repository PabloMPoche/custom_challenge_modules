# -*- coding: utf-8 -*-
{
    'name': 'Sale Custom',
    'version': '1.0',
    'summary': 'Add custom usefull actions for sale management.',
    'description': 'Add custom usefull actions for sale management.',
    'category': 'Sales/CRM',
    'author': 'Pablo Yoel Mercedes Poché',
    'license': 'LGPL-3',
    'depends': [
        'sale_management',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/sale_type.xml',
        'views/sale_order_views.xml',
        'views/sale_type_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
