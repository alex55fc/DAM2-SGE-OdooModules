# -*- coding: utf-8 -*-
{
    'name': "compras",
    'summary': """compras para el colegio""",
    'description': """
        Modulo para gestionar las ventas:
            - Ventas
            - Clientes
            - Productos
            - Vendedores
            - Facturas
    """,
    'author': "john doe",
    'website': "http://www.salesuanos.edu",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Examen',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views.xml',
    ],
}
