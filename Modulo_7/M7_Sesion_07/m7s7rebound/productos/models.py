from django.db import models


# Create your models here.
class Fabricante(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    f_vencimiento = models.DateField(null=True)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nombre
