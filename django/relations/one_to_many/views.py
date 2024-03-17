from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date
# Create your views here.

def index(request):
  reporters = Reporter.objects.all()
  return render(request, 'one_to_many.html',{
    'reporters': reporters
  })

def createReporter(request, first_name, last_name, email):
  Reporter.objects.create(first_name=first_name, last_name=last_name, email=email)
  return HttpResponse("Se registró el reportero")

def createArticle(request,headline,pub_date,reporter_id):
  reporter = Reporter.objects.get(id=reporter_id)
  Article.objects.create(headline=headline,pub_date=pub_date, reporter=reporter)
  return HttpResponse("Se registro el artículo")
  # r1 = Reporter.objects.create(first_name="Miguel", last_name="Pasachoa", email="miguel.p0908@gmail.com")
  # r2 = Reporter.objects.create(first_name="Leugim", last_name="Aohcasap", email="inversojajaxd@gmail.com")
  # r2 = Reporter.objects.get(id=2)

  # Article.objects.create(headline="adios3", pub_date=date(2005, 8, 10), reporter=r2)
  # Article.objects.create(headline="adios4", pub_date=date(2006, 1, 2), reporter=r2)
  
  # reporter = Reporter.objects.get(id=2)
  # articles = reporter.article_set.all()

  # return render(request, 'index.html', { --> Read
  #   'reporter': reporter,
  #   'articles': articles
  # })

def read(request, id):
  query = Reporter.objects.get(id=id)
  articles = query.article_set.all()
  return render(request, 'one_to_many.html', {
    'query': query,
    'articles': articles
  })

def update(request, table, id, field_name, new_value):
  if table == "reporter":
    reporter = Reporter.objects.get(id=id)
    if field_name == "first_name":
      reporter.first_name = new_value
    elif field_name == "last_name":
      reporter.last_name = new_value
    elif field_name == "email":
      reporter.email = new_value
    reporter.save()

  elif table == "article":
    article = Article.objects.get(id=id)
    if field_name == "headline":
      article.headline = new_value
    elif field_name == "pub_date":
      article.pub_date = new_value
    article.save()
  
  return HttpResponse("Se actualizó la información.")

def delete(request, table, id):
  if table == "reporter":
    query = Reporter.objects.get(id=id)
  elif table == "article":
    query = Article.objects.get(id=id)
  
  query.delete()

  return HttpResponse("Se eliminó el registro.")
