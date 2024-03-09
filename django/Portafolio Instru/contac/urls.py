from . import views
from django.urls import path
urlpatterns = [
    path("contac/", views.contac, name="contac")
]

