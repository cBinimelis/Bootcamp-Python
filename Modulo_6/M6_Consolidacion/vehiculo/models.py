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
        return self.modelo + " - " + self.marca

    def condicion(self, obj):
        if obj.precio >= 0 and obj.precio <= 10000:
            valor = "Bajo"
        elif obj.precio > 10000 and obj.precio <= 30000:
            valor = "Medio"
        elif obj.precio > 30000:
            valor = "Alto"

        return valor
