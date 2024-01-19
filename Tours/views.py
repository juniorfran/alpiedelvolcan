from django.shortcuts import get_object_or_404, redirect, render

from Configuraciones.models import Contacts, Urls_info, Urls_interes
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
    tipo_document = Reserva.DOCUMENTOS_VALIDOS
    # for tupla in tipo_document:
    #     tipo_document = tupla[0]
    
        #obtener todos los datos de contacto
    data_contact = Contacts.objects.latest()
    
    #obtener todas las url de informacion
    urls_info = Urls_info.objects.all()
    
    titulo_pagina = {
        'titulo_largo': "AL PIE DEL VOLCAN",
        'medio_titulo': "AL PIE DEL",
        'titulo_corto': "VOLCAN",
    }
    descripciones = {
        'descripcion_corta':'Aventura en el Volcan',
        'descripcion_larga':'Encuentra aventuras y descubre en este viaje al pie del volcan, donde podrás disfrutar de una experiencia única.',
        
    }
    
    #urls de interes
    urls_interes = Urls_interes.objects.all()

    if request.method == 'POST':
        # Obtén los datos del formulario directamente del request.POST
        nombre = request.POST.get('nombre')
        dui = request.POST.get('dui')
        correo_electronico = request.POST.get('correo_electronico')
        direccion = request.POST.get('direccion')
        # Obtén los datos del formulario directamente de request.POST
        cantidad_adultos = int(request.POST.get('cantidad_adultos'))
        #cantidad_ninos = int(request.POST.get('cantidad_ninos'))
        fecha_reserva = request.POST.get('fecha_reserva')
        
        #nuevo campos agregados
        telefono = request.POST.get("telefono")
        pais_residencia = request.POST.get("pais_residencia")
        tipo_documento = request.POST.get("tipo_documento")
        
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
            #cantidad_ninos=cantidad_ninos,
            fecha_reserva=fecha_reserva,
            precio_adulto=precio_adulto,
            precio_nino=precio_nino,
            telefono=telefono,
            pais_residencia=pais_residencia,
            tipo_documento=tipo_documento,
        )
        reserva.save()
        
        # Redirige a la página de éxito y pasa el reserva_id como parámetro
        return redirect('reserva_exitosa', reserva_id=reserva.id)
    # Renderiza el formulario para el método GET
    
    context = {
        'data_contact':data_contact,
        'urls_info':urls_info,
        'titulo':titulo_pagina,
        'descripcion':descripciones,
        'urls_interes':urls_interes,
        'tour': tour,
        'tipo_document':tipo_document,
    }
    
    return render(request, 'reservar_tour.html', context)

def reserva_exitosa(request, reserva_id):
    reserva = Reserva.objects.get(pk=reserva_id)
        #obtener todos los datos de contacto
    data_contact = Contacts.objects.latest()
    
    #obtener todas las url de informacion
    urls_info = Urls_info.objects.all()
    
    titulo_pagina = {
        'titulo_largo': "AL PIE DEL VOLCAN",
        'medio_titulo': "AL PIE DEL",
        'titulo_corto': "VOLCAN",
    }
    descripciones = {
        'descripcion_corta':'Aventura en el Volcan',
        'descripcion_larga':'Encuentra aventuras y descubre en este viaje al pie del volcan, donde podrás disfrutar de una experiencia única.',
        
    }
    
    #urls de interes
    urls_interes = Urls_interes.objects.all()
    
    context = {
        'data_contact':data_contact,
        'urls_info':urls_info,
        'titulo':titulo_pagina,
        'descripcion':descripciones,
        'urls_interes':urls_interes,
        'reserva': reserva,
    }

    return render(request, 'reserva_exitosa.html', context)


# import requests

# def obtener_token(client_id, client_secret):
#     url = "https://id.wompi.sv/connect/token"
#     payload = {
#         "grant_type": "client_credentials",
#         "audience": "wompi_api",
#         "client_id": client_id,
#         "client_secret": client_secret,
#     }
#     headers = {"Content-Type": "application/x-www-form-urlencoded"}

#     response = requests.post(url, data=payload, headers=headers)
    
#     if response.status_code == 200:
#         data = response.json()
#         access_token = data.get("access_token")
#         return access_token
#     else:
#         print(f"Error al obtener el token: {response.status_code}")
#         return None

# # Usar las credenciales proporcionadas
# client_id = "50163375-39c0-4dc7-8d8b-b1bc34f6e419"
# client_secret = "2c68b6a6-9b41-42c7-b418-8315913bd006"

# token = obtener_token(client_id, client_secret)

# if token:
#     # Ahora puedes usar el token en tus peticiones a la API de Wompi
#     url_api = "https://api.wompi.sv/EnlacePago"
#     headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

#     response = requests.get(url_api, headers=headers)

#     if response.status_code == 200:
#         data = response.json()
#         print(data)
#     else:
#         print(f"Error en la petición a la API: {response.status_code}")
# else:
#     print("No se pudo obtener el token de autenticación.")


