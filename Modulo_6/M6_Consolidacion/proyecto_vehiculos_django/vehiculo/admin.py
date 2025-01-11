from django.contrib import admin

from .models import VehiculoModel


# Register your models here.
@admin.register(VehiculoModel)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ["marca", "modelo", "categoria", "condicion"]

    def condicion(self, obj):
        if obj.precio >= 0 and obj.precio <= 10000:
            valor = "Bajo"
        elif obj.precio > 10000 and obj.precio <= 30000:
            valor = "Medio"
        elif obj.precio > 30000:
            valor = "Alto"

        return valor
