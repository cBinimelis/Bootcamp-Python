# Generated by Django 4.1.1 on 2025-01-27 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='directorgeneral',
            name='especialidad',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='ciudad',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='pais',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
