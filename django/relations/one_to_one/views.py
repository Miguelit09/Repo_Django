from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant

# Create your views here.

def index(request):
  places = Place.objects.all()
  return render(request, 'one_to_one.html',{
    'places': places
  })

def create(request, name, address,employees):
  new_place = Place.objects.create(name=name, address=address)
  new_restaurant = Restaurant.objects.create(place=new_place, employees=employees)
  # Crear lugar y restaurante
  # p1 = Place(name="Hamburguesas", address="Allá cerca en la otra esquina")
  # p1.save()
  # r1 = Restaurant(place= p1, employees="3")
  # r1.save()
  # Crear un restaurante con un lugar ya creado que no tiene restaurante.
  # p1 = Place.objects.get(id=1)
  # print(p1)
  # r1 = Restaurant(place=p1, employees=10)
  # r1.save() --> Save permite actualizar registros, no da error si se asigna un registro ya existente
  # Restaurant.objects.create(place=p1) --> Este no permite crear objetos con un id repetido
  # restaurant = Restaurant.objects.get(place_id=3)
  # print(restaurant.place.address)
  return HttpResponse("Se crearon los registros")

def read(request, id):
  query = Restaurant.objects.get(place_id=id)
  return render(request, 'one_to_one.html', {
    'query': query
  })

def update(request, id, field_name, new_value):
  place = Place.objects.get(id=id)
  restaurant = Restaurant.objects.get(place_id=id)
  if field_name == "name":
    place.name = new_value
    place.save()
  elif field_name == "address":
    place.address = new_value
    place.save()
  elif field_name == "employees":
    restaurant.employees = int(new_value)
    restaurant.save()
  
  return HttpResponse("Se actualizó el lugar.")

def delete(request, id):
  query = Place.objects.get(id=id)
  query.delete()

  return HttpResponse("Se eliminó el registro.")