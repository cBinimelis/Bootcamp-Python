# Generated by Django 5.1.3 on 2024-12-04 23:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartphone', '0010_remove_chapter_book_delete_book_delete_chapter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Builder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='smartphone',
            name='builder',
            field=models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, related_name='smartphone_builder', to='smartphone.builder'),
            preserve_default='True',
        ),
    ]
