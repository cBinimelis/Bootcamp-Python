from django.db import models
from django.conf import settings

# Create your models here.


class BookModel(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    score = models.IntegerField()

    class Meta:
        permissions = (
            ("development", "Permiso como Desarrollador"),
            ("scrum_master", "Permiso como Scrum Master"),
            ("product_owner", "Permiso como Product Ower"),
        )
