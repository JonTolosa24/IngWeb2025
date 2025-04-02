from django.shortcuts import render
from django.http import HttpResponse

def index(request):
 return HttpResponse("¡Bienvenido a la aplicación!")

def nombre(request, nombre_empresa):
 return HttpResponse("Consultando la empresa %s." % nombre_empresa)

def detalle(request, id_empresa):
 response = "Información de la empresa con ID = %s."
 return HttpResponse(response % id_empresa)