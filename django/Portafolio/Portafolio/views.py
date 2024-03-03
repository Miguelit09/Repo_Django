from django.shortcuts import render

def inicio(request):
  return render(request, 'index.html', {})

def portafolio(request):
  return render(request, 'portafolio.html', {})

def contacto_form(request):
  return render(request, 'contacto_form.html', {})