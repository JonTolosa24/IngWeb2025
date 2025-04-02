from django.db import models

class Red(models.Model):
 ip = models.CharField(max_length=15)
 nombre = models.CharField(max_length=200)
 fecha_creacion = models.DateTimeField('Fecha de creacion')
 
 def __str__(self):
  return self.nombre
 
class Equipo(models.Model):
 red = models.ForeignKey(Red, on_delete=models.CASCADE)
 tipo = models.CharField(max_length=30, default='PC')
 identificador = models.IntegerField(default=0)
 
 def __str__(self):
     return self.tipo
 