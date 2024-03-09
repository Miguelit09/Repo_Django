from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def contac(request):
  return HttpResponse("Mensaje cualquiera")