
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create/<str:name>/<str:address>/<int:employees>/', views.create, name="create_one_to_one"),
    path('read/<int:id>/', views.read, name="read_one_to_one"),
    path('update/<int:id>/<str:field_name>/<str:new_value>/', views.update, name="update_one_to_one"),
    path('delete/<int:id>/', views.delete, name="delete_one_to_one"),
]
