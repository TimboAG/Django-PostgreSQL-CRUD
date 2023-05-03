from django.shortcuts import render, HttpResponse, redirect
from .models import tareas

# Create your views here.

def lista_tareas(request):
    return render(request, "tarea.html")

def crear_tarea(request):
    miTarea = tareas(titulo=request.POST['titulo'], descripcion=request.POST['descripcion'])
    miTarea.save()
    return redirect ("/")