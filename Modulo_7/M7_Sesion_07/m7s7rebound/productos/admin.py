from django.contrib import admin
from .models import Producto, Fabricante


# Register your models here.
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "descripcion", "f_vencimiento", "fabricante"]


@admin.register(Fabricante)
class FabricanteAdmin(admin.ModelAdmin):
    list_display = ["nombre"]
