# Generated by Django 4.2.9 on 2024-01-09 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tours', '0004_reserva'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='qrcodes'),
        ),
        migrations.AddField(
            model_name='reserva',
            name='qr_code_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='fecha_reserva',
            field=models.DateField(),
        ),
    ]
