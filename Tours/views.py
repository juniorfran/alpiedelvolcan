from django.shortcuts import get_object_or_404, redirect, render
from .models import Resena, Tour
from .forms import ResenaForm

def tours_index(request):
    # Obtener todos los tours desde la base de datos
    tours = Tour.objects.all()

    # Puedes agregar más lógica aquí según tus necesidades

    # Renderizar la plantilla 'index.html' con la lista de tours
    return render(request, 'show_tours.html', {'tours': tours})

def tour_detail(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    return render(request, 'detail_tours.html', {'tour': tour})



def tour_detail(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    resenas = Resena.objects.filter(tour=tour)

    if request.method == 'POST':
        form = ResenaForm(request.POST)
        if form.is_valid():
            resena = form.save(commit=False)
            resena.tour = tour
            resena.save()
            return redirect('tour_detail', tour_id=tour.id)
    else:
        form = ResenaForm()

    return render(request, 'detail_tours.html', {'tour': tour, 'resenas': resenas, 'form': form})