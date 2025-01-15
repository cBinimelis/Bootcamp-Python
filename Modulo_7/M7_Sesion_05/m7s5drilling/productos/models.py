from django.db import models


# Create your models here.
class Fabricante(models.Model):
    nombre = models.CharField(max_length=50)


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE, default=2)
