from django.shortcuts import get_object_or_404, render
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

def consultas(request):
  # consultar todos los posts 
  posts = Post.objects.all()

  # consultar con un filtro
  filtro = Post.objects.filter(titulo='uno')

  # obtener un único registro
  post = Post.objects.get(id= 12)

  # obtener los 20 primeros elementos

  limite = Post.objects.all()[:20]

  # obtener los 5 primeros resultados partiendo del item 15

  limite = Post.objects.all()[3:8]

  #obtener los registros ordenados por el titulo

  orden = Post.objects.all().order_by('cuerpo')[:20] #Indicando el nombre del campo, se ordenan ASC, indicando el nombre del campo con un guion antes (-cuerpo), los ordenan DESC 

  # obtener los elementos que su id sea menor o igual que 20

  menor = Post.objects.filter(id__lte=20)

  return render(request, 'index.html', {
    'posts': posts,
    'filtro': filtro,
    'post': post,
    'limite': limite,
    'orden': orden,
    'menor': menor,
  })