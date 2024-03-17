from django.shortcuts import render
from django.http import HttpResponse
from .models import Publication, ArticleTwo

# Create your views here.
def create(request):

  #Crear publicaciones
  # p1 = Publication.objects.create(title="Python")
  # p1.save()
  # p2 = Publication.objects.create(title="HTML")
  # p2.save()
  # p3 = Publication.objects.create(title="CSS")
  # p3.save()

  # #Crear article
  # a1 = ArticleTwo(headline="Programación Orientada a Objetos")
  # a1.save()
  # # Añadir artículo a publicacion1
  # a1.publications.add(p1)

  # a2 = ArticleTwo(headline="Python se conecta con HTML")
  # a2.save()

  # a3 = ArticleTwo(headline="HTML y CSS junticos")
  # a3.save()

  # a2.publications.add(p1, p2)
  # a3.publications.add(p2)
  # a3.publications.add(p3)
  publications = Publication.objects.all()

  return render(request, 'index.html', {
    'publications': publications,
  })