from odoo import api, models, fields

#Clases
class compradores(models.Model):
    _name = 'compradores'
    name = fields.Char(required=True)
    email = fields.Char()
    phone = fields.Char()
    id = fields.Integer()

    # restricción de campos en el modelo @api.constraints añade un decorador (for record in self) cuando se crea un objeto, los datos se guardan en self -> record, en realidad no es un bucle, 
    # solo se ejecuta una vez; el registro que se está guardando en ese momento. El record es el objeto que se está guardando de la clase cliente, poniendo el .edad se accede al campo edad y si se quiere acceder a más campos hay que ponerlos en la lista, @api.constraints('edad', 'nombre', ...)
    edad = fields.Integer()
#para que esta aqui el 'name'
    @api.constrains('edad', 'name') 
    def _check_edad(self):
        for record in self:
            if record.edad < 18:
                raise models.ValidationError('El cliente ' + record.name + ' debe ser mayor de edad')
            elif record.edad > 100:
                raise models.ValidationError('El cliente ' + record.name + ' no puede tener mas de 100 años')
            else:
                pass
    #para hacer el calendar
    fecha_incorporacion = fields.Date()
    fecha_despido = fields.Date()
    #relacion 1 .. n  con vendedor, 1 comprador compra a un 1 vendedor
    vendedores = fields.Many2one(comodel_name='vendedores', string='vendedores') # relacion con el modelo vendedor comodel es el modelo con el que se relaciona, string es el nombre que se le da a la relacion

class vendedores(models.Model):
    _name = 'vendedores'
    name = fields.Char(required=True)
    email = fields.Char()
    phone = fields.Char()

    altura = fields.Float()
    peso = fields.Float()
    # el campo imc es calculado y se almacena en la base de datos
    #al usar api.depends hace que en este caso el imc se actualice solo el resultado al tener los dos datos('peso', 'altura')
    imc = fields.Float(compute='_compute_imc', store=True)
    @api.depends('peso', 'altura') # dependencias del campo imc
    def _compute_imc(self):
        for record in self:
            if record.altura > 0 and record.peso > 0:
                record.imc = record.peso / record.altura ** 2
            else:
                record.imc = 0
    #relacion 1 .. n  con vendedor, 1 vendedor vende a muchos compradores
    compradores = fields.One2many(comodel_name='compradores', inverse_name='vendedores') # relacion con el modelo cliente, inverse_name es el campo que se relaciona con el modelo cliente (vendedor en este caso) y comodel_name es el modelo con el que se relaciona (cliente en este caso)

    #relacion M:M con proveedores
    #solo lo pongo en una clase de las dos relacionadas,en este caso la pongo en compradores
    proveedores = fields.Many2many(comodel_name='proveedores', string='proveedores')

class proveedores(models.Model):
    _name = 'proveedores'
    name = fields.Char(required=True)
    email = fields.Char()
    phone = fields.Char()
    id = fields.Integer()
    tipo = fields.Selection(selection=[
                                        ('interno', 'Prov Interno'), 
                                       ('externo', 'Prov Externo')
                                    ], 
                            required=True)
""" 
class transacciones(models.Model):
    _name = 'transacciones'
    name = fields.Char(required=True)
    precioInicial = fields.Float()
    precioFinal = fields.Float()
    fecha_venta = fields.Date()
"""

    

