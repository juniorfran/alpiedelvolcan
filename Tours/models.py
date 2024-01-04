from django.db import models

# Create your models here.

#modelos para tours
class TipoTour(models.Model):
    nombre = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre

class Tour(models.Model):
    titulo = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2) #Precio del tour en dolares americanos
    duracion = models.PositiveIntegerField()   #Duracion del tour en dias 
    iva = models.BooleanField(default=False)    #Si es True el precio es con IVA (19%) si no lo es sin IVA (0%).
    imagen = models.ImageField(upload_to='tours')
    tipo_tour = models.ForeignKey(TipoTour, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.titulo} - ${self.precio}"


class ImagenTour(models.Model):
    tour = models.ForeignKey(Tour, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='tours/%Y/%m/%d/')

    def __str__(self):
        return f"Imagen para {self.tour.titulo}"