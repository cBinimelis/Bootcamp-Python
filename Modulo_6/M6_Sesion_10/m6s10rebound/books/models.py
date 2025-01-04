from django.db import models
from django.conf import settings


# Create your models here.
class BookModel(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    score = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "libro"
        verbose_name_plural = "libros"
        permissions = (
            ("development", "Permiso como Desarrollador"),
            ("scrum_master", "Permiso como Scrum Master"),
            ("product_owner", "Permiso como Product Ower"),
        )

    def __str__(self):
        return self.title
