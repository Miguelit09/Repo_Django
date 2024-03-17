from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('create_reporter/<str:first_name>/<str:last_name>/<str:email>', views.createReporter, name="create_reporter_one_to_many"),
    path('create_article/<str:headline>/<str:pub_date>/<int:reporter_id>', views.createArticle, name="create_article_one_to_many"),
    path('read/<int:id>/', views.read, name="read_one_to_many"),
    path('update/<str:table>/<int:id>/<str:field_name>/<str:new_value>/', views.update, name="update_one_to_many"),
    path('delete/<str:table>/<int:id>/', views.delete, name="delete_one_to_many"),
]