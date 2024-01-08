from django.shortcuts import get_object_or_404, render
from .models import Tour

def tours_index(request):
    # Obtener todos los tours desde la base de datos
    tours = Tour.objects.all()

    # Puedes agregar más lógica aquí según tus necesidades

    # Renderizar la plantilla 'index.html' con la lista de tours
    return render(request, 'show_tours.html', {'tours': tours})

def tour_detail(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    return render(request, 'detail_tours.html', {'tour': tour})
