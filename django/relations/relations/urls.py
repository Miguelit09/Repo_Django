
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('one_to_one/', include('one_to_one.urls'), name="one_to_one"),
    path('one_to_many/', include('one_to_many.urls'), name="one_to_many"),
    path('many_to_many/', include('many_to_many.urls'), name="many_to_many")
]
