# Generated by Django 5.1.3 on 2024-12-04 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smartphone', '0009_rename_author_chapter_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='book',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Chapter',
        ),
    ]