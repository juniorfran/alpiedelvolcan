from django.contrib import admin
from .models import TipoTour, Tour, ImagenTour

@admin.register(TipoTour)
class TipoTourAdmin(admin.ModelAdmin):
    list_display = ('nombre', )

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'precio', 'duracion', 'iva', 'tipo_tour')
    search_fields = ('titulo', 'tipo_tour__nombre')
    list_filter = ('iva', 'tipo_tour')

@admin.register(ImagenTour)
class ImagenTourAdmin(admin.ModelAdmin):
    list_display = ('tour', 'imagen')
    search_fields = ('tour__titulo', )

# Puedes personalizar más opciones según tus necesidades
