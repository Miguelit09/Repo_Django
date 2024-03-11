
from . import views

from django.urls import path
urlpatterns = [
    path("", views.index, name="lista_posts"),
    path("crear_autor/<str:nombre>/<str:correo>", views.crear_autor, name="crear_autor"),
    path("storage/<str:titulo>/<str:cuerpo>/<int:author_id>", views.storage, name="storage"),
    path("consultar/<int:consulta_id>", views.consultar, name="consultar"),
    path("actualizar/<int:consulta_id>/<str:campo>/<str:valor>", views.actualizar, name="actualizar"),
    path("eliminar/<int:consulta_id>", views.eliminar, name="eliminar"),
    path("consultar_post_por_autor/<int:author_id>", views.consultar_post_por_autor, name="consultar_post_por_autor")
]