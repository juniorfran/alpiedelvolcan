from django.shortcuts import render
from Tours.models import Tour
from Configuraciones.models import Barra_Principal, CarruselInicio, Services_Bar, Team_bar, Contacts, Urls_info, Urls_interes

#vista para mostrar la pagina principal
def index(request):
    #obtener los tour por orden de popularidad
    tours = Tour.objects.all()
    
    #obtener la barra principal
    barra_principal = Barra_Principal.objects.latest()
    
    #obtener todos los carrusel de incio
    carrusel_incio = CarruselInicio.objects.all()
    
    #Obtener todos los services bar
    services = Services_Bar.objects.filter(services_visible=True)  # Filtra los servicios visibles
    
    #obetner todos los teams
    teams_bar = Team_bar.objects.all().order_by("id")
    
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
    
    
    context={
        'tours':tours,
        'barra_principal':barra_principal,
        'carrusel_incio':carrusel_incio,
        'services':services,
        'teams_bar':teams_bar[:4],  #mostrando solo
        #los primeros 4 equipos en la barra de info
        'data_contact':data_contact,
        'urls_info':urls_info,
        'titulo':titulo_pagina,
        'descripcion':descripciones,
        'urls_interes':urls_interes,
        }
    
    
    return render(request, 'base.html', context)


