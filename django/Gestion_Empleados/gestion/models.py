from django.db import models

# Create your models here.

class Pais(models.Model):
    nombre_pais = models.CharField(max_length=60)

class Poblacion(models.Model):
    nombre_poblacion = models.CharField(max_length=60)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)  

class Fabrica(models.Model):
    nombre_fabrica = models.CharField(max_length=50)
    direccion_fabrica = models.CharField(max_length=40)
    codigo_postal = models.CharField(max_length=10)
    poblacion = models.ForeignKey(Poblacion, on_delete=models.PROTECT)

class Salario(models.Model):
    valor_bruto_año = models.IntegerField()
    extra_junio = models.BooleanField(default=False)
    extra_diciembre = models.BooleanField(default=False)

class Puesto(models.Model):
    descripcion = models.CharField(max_length=200)
    nombre_puesto = models.CharField(max_length=50)
    salario = models.ForeignKey(Salario, on_delete=models.PROTECT)

class Empleado(models.Model):
    nombre_empleado = models.CharField(max_length=50)
    documento = models.CharField(max_length=20)
    email = models.CharField(max_length=75)
    direccion_empleado = models.CharField(max_length=40)
    puesto = models.ForeignKey(Puesto, on_delete=models.PROTECT)
    fabrica = models.ForeignKey(Fabrica, on_delete=models.PROTECT)
