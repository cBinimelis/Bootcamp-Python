# Generated by Django 4.2.17 on 2025-01-02 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_bookmodel_delete_book'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookmodel',
            options={'permissions': (('development', 'Permiso como Desarrollador'), ('scrum_master', 'Permiso como Scrum Master'), ('product_owner', 'Permiso como Product Ower'))},
        ),
    ]
