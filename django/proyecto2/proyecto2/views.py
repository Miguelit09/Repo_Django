from django.shortcuts import render

def saludar(request, name, last_name, age):
  context = {
    'name': name,
    'last_name': last_name,
    'age': age
  }
  return render(request, 'saludo.html', context)