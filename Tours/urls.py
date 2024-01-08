from django.urls import path
from . import views

urlpatterns = [
    
    #urls del index
    path('', views.tours_index, name='tours'),
    path('tour/<int:tour_id>/', views.tour_detail, name='tour_detail'),
    # Agrega más URL según sea necesario
]