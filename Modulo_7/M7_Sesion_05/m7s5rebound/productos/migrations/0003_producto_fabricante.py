# Generated by Django 5.1.4 on 2025-01-15 00:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_fabricante'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='fabricante',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='productos.fabricante'),
        ),
    ]
