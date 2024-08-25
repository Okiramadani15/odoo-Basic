{
    'name': 'My Purchase Module',
    'version': '14.0.1.0.0',
    'summary': 'My purchase',
    'description': """Purchase""",
    'category': 'Extra Tools',
    'author': 'okiramadani',
    'website': 'https://github.com/Okiramadani15',
    'license': 'AGPL-3',
    'depends': ['base', 'mail'],
    'data': [
        'views/purchase_action.xml',
        'views/purchase_menu_item.xml',
        'views/purchase_view.xml',
        'security/ir.model.access.csv'
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
