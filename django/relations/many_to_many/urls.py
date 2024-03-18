from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index_many_to_many"),
    path('create/<str:table>/<str:information>/', views.create, name="create_many_to_many"),
    path('createRelationship/<int:article_id>/<int:publication_id>/', views.createRelationship, name="create_relationship_many_to_many"),
    path('read/<str:table>/<int:id>/', views.read, name="read_many_to_many"),
]