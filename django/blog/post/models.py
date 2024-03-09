from django.db import models
from datetime import date

# Create your models here.
class Author(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField(max_length=100)

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    cuerpo = models.TextField()
    fecha = models.DateField(default= date.today)
    id_author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)

