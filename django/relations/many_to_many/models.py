from django.db import models

# Create your models here.

class Publication(models.Model):
  title = models.CharField(max_length=30)

class ArticleTwo(models.Model):
  headline = models.CharField(max_length=100)
  publications = models.ManyToManyField(Publication)

