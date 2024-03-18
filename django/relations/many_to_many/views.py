from django.shortcuts import render
from django.http import HttpResponse
from .models import Publication, ArticleTwo

def index(request):
  publications = Publication.objects.all()
  return render(request, 'many_to_many.html', {
    'publications': publications,
  })


# Create your views here.
def create(request, table, information):

  if table == "publication":
    Publication.objects.create(title=information)
  elif table == "articletwo":
    ArticleTwo.objects.create(headline=information)
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
  return HttpResponse(f"Se creó registro en la tabla {table}")

def createRelationship(request, article_id, publication_id):
  article = ArticleTwo.objects.get(id=article_id)
  publication = Publication.objects.get(id=publication_id)

  article.publications.add(publication)

  return HttpResponse(f"El artículo '{article.headline}' se añadió a la publicación '{publication.title}'")

def read(request, table, id):
  if table == "publication":
    query = Publication.objects.get(id=id)
  elif table == "articletwo":
    query = ArticleTwo.objects.get(id=id)

    # publications = query.publication.all()
    # print(publications)
  return render(request, 'many_to_many.html', {
    'table': table,
    'query': query
  })