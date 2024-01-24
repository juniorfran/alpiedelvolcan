from django.shortcuts import render
import requests
from .wompi_connect import authenticate_wompi
from .wompi_consulta import make_wompi_get_request
from .wompi_envio import make_wompi_post_request, create_payment_link
from datetime import datetime, timedelta
# Create your views here.

# Tus credenciales de Wompi
Client_id = "86d5de4c-dd6a-42d2-8d5b-ff5aed09ae83"
Client_secret = "c3bb69e4-7d19-486b-b9d8-1b2b592714d5"

# Autenticarse y obtener el token
access_token = authenticate_wompi(Client_id, Client_secret)

if access_token:
    # Hacer una consulta utilizando el token
    consulta_result = make_wompi_get_request("EnlacePago", access_token)

    if consulta_result:
        print("Consulta exitosa:")
        #print(consulta_result)


def crear_enlace_pago(request):
    # Obtén los parámetros necesarios, por ejemplo, desde el formulario
    client_id = Client_id
    client_secret = Client_secret
    comercio_id = "12568"
    monto = 100.0  # Ajusta el monto según tus necesidades
    nombre_producto = "Tour al volcan de san miguel"

    # Llama a la función para crear el enlace de pago
    enlace_pago = create_payment_link(client_id, client_secret, comercio_id, monto, nombre_producto)

    # Realiza las acciones adicionales que necesites con el enlace de pago creado

    return render(request, "detalle_enlace_pago.html", {"enlace_pago": enlace_pago})



