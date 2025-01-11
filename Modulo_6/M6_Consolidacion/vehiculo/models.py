from django.db import models

# Create your models here.
MARCAS = [
    ("Fiat", "Fiat"),
    ("Chevrolet", "Chevrolet"),
    ("Ford", "Ford"),
    ("Toyota", "Toyota"),
]
CATEGORIAS = [
    ("Particular", "Particular"),
    ("Transporte", "Transporte"),
    ("Carga", "Carga"),
]


class VehiculoModel(models.Model):
    marca = models.CharField(max_length=20, choices=MARCAS, default="ford")
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(
        max_length=20, choices=CATEGORIAS, default="particular"
    )
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Vehiculo"
        verbose_name_plural = "Vehiculos"
        permissions = (
            ("visualizar_catalogo", "Puede visualizar catalogo de vehiculos"),
        )

    def __str__(self):
        if self.precio >= 0 and self.precio <= 10000:
            valor = "Bajo"
        elif self.precio > 10000 and self.precio <= 30000:
            valor = "Medio"
        elif self.precio > 30000:
            valor = "Alto"

        return f"{self.modelo}-{self.marca}-{valor}"
