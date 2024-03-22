from django.db import models

# Create your models here.

class Pais:
    nombre_pais = models.CharField(max_length=60)

class Poblacion:
    nombre_poblacion = models.CharField(max_length=60)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT)