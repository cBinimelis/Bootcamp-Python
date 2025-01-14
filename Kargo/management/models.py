from django.db import models
from django.contrib.auth.models import User

ESTADOS = [
    ("reservada", "Reservada"),
    ("ocupada", "Ocupada"),
    ("liberada", "Liberada"),
    ("terminada", "Terminada"),
]
HORAS = (
    ("08:00", "08:00"),
    ("09:00", "09:00"),
    ("10:00", "10:00"),
    ("11:00", "11:00"),
    ("12:00", "12:00"),
    ("13:00", "13:00"),
    ("14:00", "14:00"),
    ("15:00", "15:00"),
    ("16:00", "16:00"),
    ("17:00", "17:00"),
    ("18:00", "18:00"),
    ("19:00", "19:00"),
    ("20:00", "20:00"),
)
TIPOS = [
    ("niños", "Niños"),
    ("jovenes", "Jovenes"),
    ("adultos", "Adultos"),
]


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=70)
    telefono = models.CharField(max_length=15)
    edad = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre


class Pista(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=TIPOS)
    cantidad_vehiculos = models.IntegerField()

    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    pista = models.ForeignKey(Pista, on_delete=models.CASCADE, null=True)
    fecha = models.DateField()
    hora = models.TimeField(max_length=5, choices=HORAS)
    estado = models.CharField(max_length=50, choices=ESTADOS, default="reservada")
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, null=True)
