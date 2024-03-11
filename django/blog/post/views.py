from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Post, Author


def crear_autor(request, nombre, correo):
  author = Author(nombre=nombre, correo=correo)
  author.save()
  return HttpResponse(f"Registramos al autor ---  Nombre: {author.nombre}. ---   Correo:{author.correo}")

def index(request): 
  respuesta = "" 
  posts = Post.objects.all()
  for post in posts:
    respuesta += (f"ID: {post.id} - Título: {post.titulo} - Cuerpo: {post.cuerpo} ---")
  return HttpResponse(respuesta)


# Create your views here.

def storage(request, titulo, cuerpo, author_id):
  post = Post(titulo=titulo, cuerpo=cuerpo, author_id=author_id)
  post.save()
  return HttpResponse(f"Guardamos los datos ---  Titulo: {post.titulo}. ---   Cuerpo:{post.cuerpo} ---")

def consultar(request, consulta_id):
    post = Post.objects.get(id=consulta_id)
    print(f"\nTítulo: {post.titulo}\nCuerpo: {post.cuerpo}\nFecha: {post.fecha}\nID = {post.id}")
    return HttpResponse(f"Consultando --- Título: {post.titulo} --- Cuerpo: {post.cuerpo} --- Fecha: {post.fecha} --- ID = {post.id}")

def actualizar(request, consulta_id, campo, valor):
    post = Post.objects.get(id=consulta_id)
    if campo == "titulo":
      post.titulo = valor
    elif campo == "cuerpo":
      post.cuerpo = valor
    elif campo == "author_id":
      post.author_id = valor
    post.save()
    return HttpResponse(f"Guardamos los datos ---  Titulo: {post.titulo}. ---   Cuerpo:{post.cuerpo}")

def eliminar(request, consulta_id):
  post = Post.objects.get(id=consulta_id)
  post.delete()
  return HttpResponse("Post eliminado")

def consultar_post_por_autor(request, author_id):
  respuesta = ""
  author = get_object_or_404(Author, id=author_id)
  posts_author = author.posts.all()
  for post in posts_author:
    respuesta += (f"\nTítulo: {post.titulo}\nCuerpo: {post.cuerpo}")
  return HttpResponse(respuesta)