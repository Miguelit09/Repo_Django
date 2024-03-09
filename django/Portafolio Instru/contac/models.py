from django.db import models

# Create your models here.

class Contac(models.Model):
  nombre = models.CharField(max_length=75)
  telefono = models.CharField(max_length=10)
  email = models.CharField(max_length=100)
  mensaje = models.TextField()