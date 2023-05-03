from django.shortcuts import render, HttpResponse, redirect
from .models import tareas

# Create your views here.


def lista_tareas(request):
    return render(request, "tarea.html")


def crear_tarea(request):
    miTarea = tareas(
        titulo=request.POST['titulo'], descripcion=request.POST['descripcion'])
    miTarea.save()
    return redirect("/")


def ver_tareas(request):
    misTareas = tareas.objects.all()
    return render(request, "lista_tareas.html", {"misTareas": misTareas})


def eliminar_tareas(request, id):
    misTareas = tareas.objects.get(id=id)
    misTareas.delete()
    return redirect("/ver")
