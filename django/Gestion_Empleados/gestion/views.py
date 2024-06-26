from django.shortcuts import render
from django.http import HttpResponse
from .models import Pais, Poblacion, Fabrica, Salario, Puesto, Empleado
# Create your views here.

def index(request):
    return render(request, 'index.html', {})


# PAIS 
def registrar_pais(request):
    return render(request, 'registrar_pais.html', {})

def save_pais(request):
    nombre_pais = request.POST['nombre_pais']
    new_pais = Pais.objects.create(nombre_pais=nombre_pais)
    return HttpResponse(f"Se registró el país {new_pais.nombre_pais}.")

# POBLACIÓN
def registrar_poblacion(request):
    paises = Pais.objects.all()
    return render(request, 'registrar_poblacion.html', {
        'paises': paises
    })

def save_poblacion(request):
    nombre_poblacion = request.POST['nombre_poblacion']
    pais_id = request.POST['pais_id']
    pais = Pais.objects.get(id=pais_id)
    new_poblacion = Poblacion.objects.create(nombre_poblacion=nombre_poblacion, pais=pais)
    return HttpResponse(f"Se registró la población {new_poblacion.nombre_poblacion} localizada en {pais.nombre_pais}")


# FABRICA
def registrar_fabrica(request):
    poblaciones = Poblacion.objects.all()
    return render(request, 'registrar_fabrica.html', {
        'poblaciones': poblaciones
    })

def save_fabrica(request):
    nombre_fabrica = request.POST['nombre_fabrica']
    direccion_fabrica = request.POST['direccion_fabrica']
    codigo_postal = request.POST['codigo_postal']
    poblacion_id = request.POST['poblacion_id']
    poblacion = Poblacion.objects.get(id=poblacion_id)
    new_fabrica = Fabrica.objects.create(nombre_fabrica=nombre_fabrica, direccion_fabrica=direccion_fabrica, codigo_postal=codigo_postal, poblacion = poblacion)
    return HttpResponse(f"Se registró la fabrica {new_fabrica.nombre_fabrica} localizada en la población {poblacion.nombre_poblacion}")

# SALARIO
def registrar_salario(request):
    return render(request, 'registrar_salario.html', {})

def save_salario(request):
    valor_bruto_año = request.POST['valor_bruto_año']
    if 'extra_junio' in request.POST:
        extra_junio = True
    else:
        extra_junio = False
    if 'extra_diciembre' in request.POST:
        extra_diciembre = True
    else:
        extra_diciembre = False
    new_salario = Salario.objects.create(valor_bruto_año=valor_bruto_año, extra_junio=extra_junio, extra_diciembre=extra_diciembre)
    return HttpResponse(f"Se registró el salario")

# PUESTO

def tabla_puesto(request):
    return render(request, 'tabla_puesto.html', {})

def registrar_puesto(request):
    salarios = Salario.objects.all()
    return render(request, 'registrar_puesto.html', {
        'salarios': salarios
    })

def save_puesto(request):
    nombre_puesto = request.POST['nombre_puesto']
    descripcion = request.POST['descripcion']
    salario_id = request.POST['salario_id']
    salario = Salario.objects.get(id=salario_id)
    new_puesto = Puesto.objects.create(nombre_puesto=nombre_puesto, descripcion=descripcion, salario=salario)
    return HttpResponse(f"Se registró el puesto {new_puesto.nombre_puesto}.")

def listar_puestos(request):
    puestos = Puesto.objects.all()
    return render(request, 'lista_puestos.html', {
        'puestos': puestos
    })

def formulario_editar_puesto(request, id):
    puesto = Puesto.objects.get(id=id)
    salarios = Salario.objects.all()
    return render(request, 'editar_puesto.html', {
        'puesto': puesto,
        'salarios': salarios,
    })


def editar_puesto(request):
    puesto = Puesto.objects.get(id=request.POST['id'])
    puesto.nombre_puesto = request.POST['nombre_puesto']
    puesto.descripcion = request.POST['descripcion']
    puesto.salario = Salario.objects.get(id=request.POST['salario_id'])

    puesto.save()
    return HttpResponse(f"Puesto con ID {puesto.id} actualizado.")

def eliminar_puesto(request, id):
    puesto = Puesto.objects.get(id=id)
    puesto.delete()
    return HttpResponse(f"Puesto con ID {id} eliminado.")




# EMPLEADO
def tabla_empleado(request):
    return render(request, 'tabla_empleado.html', {})

def registrar_empleado(request):
    fabricas = Fabrica.objects.all()
    puestos = Puesto.objects.all()
    return render(request, 'registrar_empleado.html', {
        'fabricas': fabricas,
        'puestos': puestos
    })

def save_empleado(request):
    nombre_empleado = request.POST['nombre_empleado']
    documento = request.POST['documento']
    email = request.POST['email']
    direccion_empleado = request.POST['direccion_empleado']
    fabrica_id = request.POST['fabrica_id']
    fabrica = Fabrica.objects.get(id=fabrica_id)
    puesto_id = request.POST['puesto_id']
    puesto = Puesto.objects.get(id=puesto_id)
    new_empleado = Empleado.objects.create(nombre_empleado=nombre_empleado, documento=documento, email=email ,direccion_empleado=direccion_empleado, fabrica=fabrica, puesto=puesto)
    return HttpResponse(f"Se registró el empleado {new_empleado.nombre_empleado} con el puesto de {puesto.nombre_puesto} en la fabrica {fabrica.nombre_fabrica}")

def listar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'lista_empleados.html', {
        'empleados': empleados
    })

def formulario_editar_empleado(request, id):
    empleado = Empleado.objects.get(id=id)
    fabricas = Fabrica.objects.all()
    puestos = Puesto.objects.all()
    return render(request, 'editar_empleado.html', {
        'empleado': empleado,
        'fabricas': fabricas,
        'puestos': puestos,
    })


def editar_empleado(request):
    empleado = Empleado.objects.get(id=request.POST['id'])
    empleado.nombre_empleado = request.POST['nombre_empleado']
    empleado.documento = request.POST['documento']
    empleado.email = request.POST['email']
    empleado.direccion_empleado = request.POST['direccion_empleado']
    empleado.fabrica = Fabrica.objects.get(id=request.POST['fabrica_id'])
    empleado.puesto = Puesto.objects.get(id=request.POST['puesto_id'])

    empleado.save()
    return HttpResponse(f"Empleado con ID {empleado.id} actualizado.")

def eliminar_empleado(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    return HttpResponse(f"Empleado con ID {id} eliminado.")
