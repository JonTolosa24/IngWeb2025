from django.db import models


class Red(models.Model):
    ip = models.CharField(max_length=15)
    nombre = models.CharField(max_length=100)
    fecha_creacion= models.DateTimeField(default="Fecha creacion")
    def __str__(self):
        return f"{self.ip}- {self.nombre}- {self.fecha_creacion}"

class Equipo(models.Model):
    mac = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=30)
    red = models.ForeignKey(Red, on_delete=models.CASCADE, related_name="equipos")

    def __str__(self):
        return f"{self.nombre} ({self.mac})"
    
class Empresa(models.Model):
    nombre = models.CharField(max_length=50)
    cif = models.CharField(max_length=12)
    def __str__(self):
        return f"{self.nombre}- {self.cif}"    

class Trabajador(models.Model):
    id = models.AutoField(primary_key=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="trabajadores")
    nombre = models.CharField(max_length=40)
    fecha_nacim = models.DateField(default ='00:00:00:00:00:00') 
    antiguedad = models.IntegerField(default=0)   
    def __str__(self):
        return f"{self.empresa}- {self.nombre}- {self.fecha_nacim}- {self.antiguedad}"
    