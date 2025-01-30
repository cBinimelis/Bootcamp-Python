from django.db import models
from django.contrib.auth.models import User


TIPO_LICENCIA = [
    ("A", "Clase A"),
    ("B", "Clase B"),
    ("C", "Clase C"),
]

TIPO_CLASE = [
    ("T", "Clase Teorica"),
    ("P", "Clase Practica"),
]

ESTADO_CLASE = [
    ("P", "Pendiente"),
    ("E", "En curso"),
    ("A", "Aprobada"),
    ("R", "Reprobada"),
]

TRANSMISION = [
    ("M", "Manual"),
    ("A", "Automática"),
]

ESTADO_VEHICULO = [
    ("D", "Disponible"),
    ("M", "En Mantención"),
]


class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=70)
    telefono = models.CharField(max_length=15)
    tipo_licencia = models.CharField(max_length=1, choices=TIPO_LICENCIA)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Instructor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=70)
    telefono = models.CharField(max_length=15)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=1, choices=TIPO_CLASE)
    descripcion = models.CharField(max_length=1000)

    def __str__(self):
        return self.nombre


class Vehiculo(models.Model):
    modelo = models.CharField(max_length=50)
    patente = models.CharField(max_length=10)
    transmision = models.CharField(max_length=1, choices=TRANSMISION, default="M")
    estado = models.CharField(max_length=1, choices=ESTADO_VEHICULO, default="D")

    def __str__(self):
        return self.patente


class DetalleClase(models.Model):
    clase = models.OneToOneField(Clase, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, null=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, null=True)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, null=True)
    fecha = models.DateField(null=True)
    hora = models.TimeField(max_length=5, null=True)
    estado = models.CharField(max_length=1, choices=ESTADO_CLASE, default="P")
    resultado = models.CharField(max_length=2000, blank=True)

    def __str__(self):
        return f"{self.clase}, {self.alumno}"
