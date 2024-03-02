from django.shortcuts import render

def inicio(request):
  return render(request, 'index.html', {})

def nosotros(request):
  return render(request, 'nosotros.html', {})

def servicios(request):
  return render(request, 'servicios.html', {})

def blog(request):
  return render(request, 'blog.html', {})

def contactanos(request):
  return render(request, 'contactanos.html', {})

