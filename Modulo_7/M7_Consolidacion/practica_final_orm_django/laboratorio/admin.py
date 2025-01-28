from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto


admin.site.site_header = "LABOFARMA"
admin.site.site_title = "Panel de control"
admin.site.site_title = "Administrador Django"


# Register your models here.
@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre"]


@admin.register(DirectorGeneral)
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "laboratorio"]


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "nombre",
        "laboratorio",
        "a_fabricacion",
        "p_costo",
        "p_venta",
    ]
    list_filter = ["nombre", "laboratorio"]
