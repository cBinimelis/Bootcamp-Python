from django.contrib import admin
from .models import Reserva, Cliente, Pista

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Pista)
admin.site.register(Reserva)
