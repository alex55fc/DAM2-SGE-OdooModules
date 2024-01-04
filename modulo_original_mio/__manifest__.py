# -*- coding: utf-8 -*-
{
    'name': "modulo_mio_prueba",
    'summary': """modulo de Alumnos y Profes""",
    'description': """
        Modulo para gestionar La relacion entre alumnos y profesores:
            relacion one2many
    """,
    'author': "Alexander Paul Fuela Cauja",
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
