# Generated by Django 4.2.9 on 2024-01-23 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Tours', '0014_alter_reserva_codigo_reserva'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnlacePago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comercio_id', models.CharField(max_length=500)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nombre_producto', models.CharField(max_length=500)),
                ('url_qr_code', models.URLField()),
                ('url_enlace', models.URLField()),
                ('esta_productivo', models.BooleanField()),
                ('permitir_tarjeta_credito_debito', models.BooleanField()),
                ('permitir_pago_punto_agricola', models.BooleanField()),
                ('permitir_pago_cuotas_agricola', models.BooleanField()),
                ('permitir_pago_bitcoin', models.BooleanField()),
                ('cantidad_maxima_cuotas', models.CharField(max_length=20)),
                ('descripcion_producto', models.TextField()),
                ('url_imagen_producto', models.URLField()),
                ('url_redirect', models.URLField()),
                ('es_monto_editable', models.BooleanField()),
                ('es_cantidad_editable', models.BooleanField()),
                ('cantidad_por_defecto', models.IntegerField()),
                ('emails_notificacion', models.EmailField(max_length=254)),
                ('telefonos_notificacion', models.CharField(max_length=20)),
                ('notificar_transaccion_cliente', models.BooleanField()),
                ('fecha_inicio_vigencia', models.DateTimeField()),
                ('fecha_fin_vigencia', models.DateTimeField()),
                ('cantidad_maxima_pagos_exitosos', models.IntegerField()),
                ('cantidad_maxima_pagos_fallidos', models.IntegerField()),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tours.reserva')),
            ],
        ),
    ]
