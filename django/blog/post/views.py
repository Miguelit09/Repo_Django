
from django.http import HttpResponse
from .models import Post, Author


def crear_autor(request, nombre, correo):
   author = Author(nombre=nombre, correo=correo)
   author.save()
   return HttpResponse(f"Registramos al autor ---  Nombre: {author.nombre}. ---   Correo:{author.correo}")

def index(request):  
  posts = Post.objects.all()
  for post in posts:
    print(f"Título: {post.titulo}\nCuerpo: {post.cuerpo}")
  # print(posts)
  return HttpResponse(posts)


# Create your views here.

def storage(request, titulo, cuerpo, id_author_id):
  post = Post(titulo=titulo, cuerpo=cuerpo, id_author_id=id_author_id)
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
    post.save()
    return HttpResponse(f"Guardamos los datos ---  Titulo: {post.titulo}. ---   Cuerpo:{post.cuerpo}")

def eliminar(request, consulta_id):
   post = Post.objects.get(id=consulta_id)
   post.delete()
   return HttpResponse("Post eliminado")

# def consultar_post_por_autor(request, id_author):
#    author = Author.objects.get(id=id_author)
#    posts = author.post.set.objects.all()
#    for post in posts:
#       print(f"Título: {post.titulo}\nCuerpo: {post.cuerpo}")