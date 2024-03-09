from django.shortcuts import render

def inicio(requets):
  return render(requets, 'index.html', {})

def portafolio(requets):
  return render(requets, 'portafolio.html', {})

def contacto(requets):
  return render(requets, 'contacto.html', {})
