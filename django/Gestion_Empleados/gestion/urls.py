from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index_gestion"),

    path('registrar_pais/', views.registrar_pais, name="registrar_pais"),
    path('save_pais/', views.save_pais, name="save_pais"),

    path('registrar_poblacion/', views.registrar_poblacion, name="registrar_poblacion"),
    path('save_poblacion/', views.save_poblacion, name="save_poblacion"),

    path('registrar_fabrica/', views.registrar_fabrica, name="registrar_fabrica"),
    path('save_fabrica/', views.save_fabrica, name="save_fabrica"),

    path('registrar_salario/', views.registrar_salario, name="registrar_salario"),
    path('save_salario/', views.save_salario, name="save_salario"),

    path('tabla_puesto/', views.tabla_puesto, name="tabla_puesto"),
    path('registrar_puesto/', views.registrar_puesto, name="registrar_puesto"),
    path('save_puesto/', views.save_puesto, name="save_puesto"),
    path('listar_puestos/', views.listar_puestos, name="listar_puestos"),
    path('formulario_editar_puesto/<int:id>/', views.formulario_editar_puesto, name="formulario_editar_puesto"),
    path('editar_puesto/', views.editar_puesto, name="editar_puesto"),
    path('eliminar_puesto/<int:id>', views.eliminar_puesto, name="eliminar_puesto"),

    path('tabla_empleado/', views.tabla_empleado, name="tabla_empleado"),
    path('registrar_empleado/', views.registrar_empleado, name="registrar_empleado"),
    path('save_empleado/', views.save_empleado, name="save_empleado"),
    path('listar_empleados/', views.listar_empleados, name="listar_empleados"),
    path('formulario_editar_empleado/<int:id>/', views.formulario_editar_empleado, name="formulario_editar_empleado"),
    path('editar_empleado/', views.editar_empleado, name="editar_empleado"),
    path('eliminar_empleado/<int:id>', views.eliminar_empleado, name="eliminar_empleado"),
]
