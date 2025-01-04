# Generated by Django 4.2.17 on 2025-01-04 00:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_bookmodel_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookmodel',
            options={'permissions': (('development', 'Permiso como Desarrollador'), ('scrum_master', 'Permiso como Scrum Master'), ('product_owner', 'Permiso como Product Ower')), 'verbose_name': 'libro', 'verbose_name_plural': 'libros'},
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
