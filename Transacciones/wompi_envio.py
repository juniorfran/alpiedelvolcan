# wompi_envio.py
import requests
from django.shortcuts import get_object_or_404
from Tours.models import Reserva
from .wompi_connect import authenticate_wompi
from .wompi_consulta import make_wompi_get_request
from .models import EnlacePago  # Importa tu modelo EnlacePago desde tu aplicación de Django



def make_wompi_post_request(endpoint, access_token, data):
    url = f"https://api.wompi.sv/{endpoint}"
    headers = {
        "content-type": "application/json",
        "authorization": f"Bearer {access_token}"
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during POST request: {e}")
        return None
    

def create_payment_link(reserva_id, client_id, client_secret, comercio_id, monto, nombre_producto, descripcionProducto, imagenProducto, cantidad, **kwargs):
    # Autenticar con Wompi
    access_token = authenticate_wompi(client_id, client_secret)

    if not access_token:
        return None

    try:
        # Obtener la instancia de Reserva
        reserva_instance = get_object_or_404(Reserva, pk=reserva_id)

        # Construir la solicitud JSON
        request_data = {
            "identificadorEnlaceComercio": comercio_id,
            "monto": monto,
            "nombreProducto": nombre_producto,
            "descripcionProducto":descripcionProducto,
            "urlImagenProducto": imagenProducto,
            "cantidadPorDefecto": cantidad,
            # "metadata": {
            #     "identificadorEnlaceComercio": comercio_id,
            #     "descripcionProducto": descripcionProducto,
            #     "urlImagenProducto": imagenProducto,
            #     "cantidadPorDefecto": cantidad
            #     # Otros datos específicos de la pantalla de pago
            # },
                    
            **kwargs
        }

        # Realizar la solicitud POST a Wompi para crear el enlace de pago
        response = requests.post("https://api.wompi.sv/EnlacePago", json=request_data, headers=get_wompi_headers(access_token))
        response.raise_for_status()
        payment_link_data = response.json()

        # Almacenar la información del enlace de pago en la base de datos
        enlace_pago = EnlacePago.objects.create(
            reserva=reserva_instance,
            comercio_id=comercio_id,
            monto=monto,
            nombre_producto=nombre_producto,
            url_qr_code=payment_link_data["urlQrCodeEnlace"],
            url_enlace=payment_link_data["urlEnlace"],
            esta_productivo=payment_link_data["estaProductivo"],
            descripcionProducto=descripcionProducto,
            imagenProducto=imagenProducto,
            cantidad=cantidad
        )

        return enlace_pago
    except requests.exceptions.RequestException as e:
        print(f"Error creating payment link: {e}")
        return None



def get_wompi_headers(access_token):
    return {
        "content-type": "application/json",
        "authorization": f"Bearer {access_token}"
    }

