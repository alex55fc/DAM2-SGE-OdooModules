from odoo import api, models, fields

# imaginad que esta en otro modulo
class Base(models.Model):
    _name = 'salesianos.base'
    name = fields.Char(required=True, string='Nombre')
    color = fields.Selection(selection=[('rojo','Color rojo'), ('verde','Color verde'), ('azul',"Color Azul")], 
                             required=True, string='Color RGB')

class CMYK(models.Model):
    # do not generate a new table in the database
    # extiendo la tabla
    _inherit = 'salesianos.base'
    color_cmyk = fields.Selection(selection=[
                ('cyan','Color cyan'), 
                ('magenta','Color magenta'), ('yellow',"Color yellow")], 
                             required=True, string='Color CMYK')
    

class ColorBlind(models.Model):
    # generates a new table in the database
    #replico la tabla
    _inherit = 'salesianos.base'
    _name = 'salesianos.colorblind'
    
    color_blind = fields.Selection(selection=[ ('brown','Color brown'),
                                              ('blue','Color blue'), 
                                              ('pink',"Color pink")],
                             required=True, string='Color Blind')


class Cliente(models.Model):
    _name = 'salesianos.cliente'
    name = fields.Char(required=True)
    email = fields.Char()
    phone = fields.Char()
    vendedor = fields.Many2one(comodel_name='salesianos.vendedor', string='vendedor') # relacion con el modelo vendedor comodel es el modelo con el que se relaciona, string es el nombre que se le da a la relacion
    edad = fields.Integer()
    # restricción de campos en el modelo @api.constraints añade un decorador (for record in self) cuando se crea un objeto, los datos se guardan en self -> record, en realidad no es un bucle, solo se ejecuta una vez; el registro que se está guardando en ese momento. El record es el objeto que se está guardando de la clase cliente, poniendo el .edad se accede al campo edad y si se quiere acceder a más campos hay que ponerlos en la lista, @api.constraints('edad', 'nombre', ...)
    @api.constrains('edad', 'name') 
    def _check_edad(self):
        for record in self:
            if record.edad < 18:
                raise models.ValidationError('El cliente ' + record.name + ' debe ser mayor de edad')
            elif record.edad > 100:
                raise models.ValidationError('El cliente ' + record.name + ' no puede tener mas de 100 años')
            else:
                pass
    altura = fields.Float()
    peso = fields.Float()
    imc = fields.Float(compute='_compute_imc', store=True) # el campo imc es calculado y se almacena en la base de datos
    @api.depends('peso', 'altura') # dependencias del campo imc
    def _compute_imc(self):
        for record in self:
            if record.altura > 0 and record.peso > 0:
                record.imc = record.peso / record.altura ** 2
            else:
                record.imc = 0
    proveedor = fields.Many2many(comodel_name='salesianos.proveedor', string='proveedor')

class Proveedor(models.Model):
    _name = 'salesianos.proveedor'
    name = fields.Char(required=True)
    cif = fields.Char(required=True)
    titular = fields.Char()
    tipo = fields.Selection(selection=[
                                        ('interno', 'Prov Interno'), 
                                       ('externo', 'Prov Externo')
                                    ], 
                            required=True)
    #cliente = fields.Many2many(comodel_name='salesianos.cliente', string='cliente')

class Vendedor(models.Model):
    _name = 'salesianos.vendedor'
    name = fields.Char(required=True)
    company = fields.Char()
    fecha_incorporacion = fields.Date()
    fecha_despido = fields.Date()
    cliente = fields.One2many(comodel_name='salesianos.cliente', inverse_name='vendedor') # relacion con el modelo cliente, inverse_name es el campo que se relaciona con el modelo cliente (vendedor en este caso) y comodel_name es el modelo con el que se relaciona (cliente en este caso)


