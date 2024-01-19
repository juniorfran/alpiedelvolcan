# Generated by Django 4.2.9 on 2024-01-16 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tours', '0010_alter_reserva_iva'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='pais_residencia',
            field=models.CharField(default='El Salvador', max_length=50),
        ),
        migrations.AddField(
            model_name='reserva',
            name='telefono',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reserva',
            name='tipo_documento',
            field=models.CharField(choices=[('DUI', 'Documento Unico de Identidad'), ('CE', 'Cédula de extrangería'), ('LIC', 'Licencia Nacional'), ('PA', 'Pasaporte'), ('Otro', 'Otro')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]