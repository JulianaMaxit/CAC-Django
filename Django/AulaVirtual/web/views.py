from django.shortcuts import render
from django.http import HttpResponse

def index(request): #llamo a la vista
    return render(request, 'index.html')

def saludar(request, nombre):
    
    print(request.method)

    return HttpResponse(f"<h1>Hola {nombre}.</h1>")

def alumnos_por_año(request, year): #ejemplo_vista_expresion_regular
    alumnos = ["Carlos", "María", "Juan"] #"""levanta los usuarios de la BBDD y los muestra por pantalla"""
    return HttpResponse(f"Listado de alumnos: {year} \n {alumnos}")
