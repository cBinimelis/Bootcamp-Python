# Generated by Django 5.1.3 on 2024-11-27 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smartphone', '0008_smartphone_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapter',
            old_name='author',
            new_name='title',
        ),
    ]