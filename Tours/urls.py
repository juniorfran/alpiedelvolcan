from django.urls import path
from . import views

urlpatterns = [
    
    #urls del index
    path('', views.tours_index, name='index'),
    # Agrega más URL según sea necesario
]