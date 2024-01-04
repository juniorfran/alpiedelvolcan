from django.shortcuts import render
from .models import Tour

def index(request):
    # Obtener todos los tours desde la base de datos
    tours = Tour.objects.all()

    # Puedes agregar más lógica aquí según tus necesidades

    # Renderizar la plantilla 'index.html' con la lista de tours
    return render(request, 'index.alpiedelvolcan.html', {'tours': tours})
