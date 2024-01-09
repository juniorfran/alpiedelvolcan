from django.shortcuts import get_object_or_404, redirect, render
from .models import ImagenTour, Resena, Tour, Reserva
from .forms import ResenaForm, ReservaForm
from django.utils import timezone

def tours_index(request):
    # Obtener todos los tours desde la base de datos
    tours = Tour.objects.all()

    # Puedes agregar más lógica aquí según tus necesidades

    # Renderizar la plantilla 'index.html' con la lista de tours
    return render(request, 'show_tours.html', {'tours': tours})

# def tour_detail(request, tour_id):
#     tour = get_object_or_404(Tour, id=tour_id)
#     return render(request, 'detail_tours.html', {'tour': tour})


def tour_detail(request, tour_id):
    tour = Tour.objects.get(pk=tour_id)
    resenas = Resena.objects.filter(tour=tour)
    imagenes = [tour.imagen] + list(tour.imagenes.all())

    if request.method == 'POST':
        estrellas = int(request.POST.get('rating'))
        comentario = request.POST.get('comentario')

        # Validación de campos, ajusta según tus necesidades
        if estrellas < 1 or estrellas > 5:
            # Manejar error, por ejemplo, redirigir a la misma página con un mensaje de error
            return redirect('tour_detail', tour_id=tour_id)

        resena = Resena.objects.create(tour=tour, estrellas=estrellas, comentario=comentario)
        return redirect('tour_detail', tour_id=tour_id)

    return render(request, 'detail_tours.html', {'tour': tour, 'imagenes': imagenes, 'resenas': resenas})


def reservar_tour(request, tour_id):
    tour = get_object_or_404(Tour, pk=tour_id)

    if request.method == 'POST':
        # Obtén los datos del formulario directamente del request.POST
        nombre = request.POST.get('nombre')
        dui = request.POST.get('dui')
        correo_electronico = request.POST.get('correo_electronico')
        direccion = request.POST.get('direccion')
        # Obtén los datos del formulario directamente de request.POST
        cantidad_adultos = int(request.POST.get('cantidad_adultos'))
        cantidad_ninos = int(request.POST.get('cantidad_ninos'))
        fecha_reserva = request.POST.get('fecha_reserva')
        
        # Obtener los precios de adulto y nino del tour
        precio_adulto = tour.precio_adulto
        precio_nino = tour.precio_nino

        reserva = Reserva(
            tour=tour,
            nombre=nombre,
            dui=dui,
            correo_electronico=correo_electronico,
            direccion=direccion,
            cantidad_adultos=cantidad_adultos,
            cantidad_ninos=cantidad_ninos,
            fecha_reserva=fecha_reserva,
            precio_adulto=precio_adulto,
            precio_nino=precio_nino,
        )
        reserva.save()
        
        # Redirige a la página de éxito y pasa el reserva_id como parámetro
        return redirect('reserva_exitosa', reserva_id=reserva.id)
    # Renderiza el formulario para el método GET
    return render(request, 'reservar_tour.html', {'tour': tour})

def reserva_exitosa(request, reserva_id):
    reserva = Reserva.objects.get(pk=reserva_id)

    return render(request, 'reserva_exitosa.html', {'reserva': reserva})