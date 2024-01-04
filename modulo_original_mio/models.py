from odoo import api, models, fields

#primero creamos las clases 
class Alumno(models.Model):
    #esto es el Id para referirse a esta clase
    _name='salesianos.alumno'
    name=fields.Char(required=True)
    email=fields.Char()
    phone=fields.Char()
    edad=fields.Integer()
    id = fields.Integer()
#la relacion entre alumno y profesor 1 .. N en este caso 1 alumno tiene un profe ponemos en Alumno Many2One(el one es del alumno)
   #comodel_name hace referencia a la Id de la otra clase referenciada(la de profesor) y el string el nombre de la relacion
    profesor = fields.Many2one(comodel_name='salesianos.profesor', string='profesor')


class Profesor(models.Model):
    _name='salesianos.profesor'
    name=fields.Char(required=True)
    email=fields.Char()
    phone=fields.Char()
    edad=fields.Integer()
    # inverse_name es el campo que se relaciona con el modelo alumno (profesor en este caso), ya que ahi esta el nombre de 'profesor'
    #  y comodel_name es el modelo con el que se relaciona (alumno en este caso)
    alumno=fields.One2many(comodel_name='salesianos.alumno', inverse_name='profesor')
                            #si hay errer por inverse_name chekar eseta linea--^    


    

