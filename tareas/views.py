from django.shortcuts import render, HttpResponse

# Create your views here.

def lista_tareas(request):
    return render(request, "tarea.html")