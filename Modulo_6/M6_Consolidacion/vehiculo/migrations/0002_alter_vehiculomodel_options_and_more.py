# Generated by Django 4.0.5 on 2025-01-10 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vehiculomodel',
            options={'permissions': (('visualizar_catalogo', 'Puede visualizar catalogo de vehiculos'),), 'verbose_name': 'Vehiculo', 'verbose_name_plural': 'Vehiculos'},
        ),
        migrations.AlterField(
            model_name='vehiculomodel',
            name='categoria',
            field=models.CharField(choices=[('Particular', 'Particular'), ('Transporte', 'Transporte'), ('Carga', 'Carga')], default='particular', max_length=20),
        ),
        migrations.AlterField(
            model_name='vehiculomodel',
            name='marca',
            field=models.CharField(choices=[('Fiat', 'Fiat'), ('Chevrolet', 'Chevrolet'), ('Ford', 'Ford'), ('Toyota', 'Toyota')], default='ford', max_length=20),
        ),
    ]