# -*- coding: utf-8 -*-
{
    'name': 'Mail Fix ses',
    'version': '12.0.1.0.0',    
    'author': 'Odoo Nodriza Tech (ONT)',
    'website': 'https://nodrizatech.com/',
    'category': 'Tools',
    'license': 'AGPL-3',
    'depends': ['base', 'mail'],
    'data': [
        'data/ir_cron.xml',
        'data/ir_configparameter_data.xml',
    ],
    'installable': True,
    'auto_install': False,    
}