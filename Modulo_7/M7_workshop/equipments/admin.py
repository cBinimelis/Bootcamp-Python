from django.contrib import admin
from .models import Brand, Model, Equipment


# Register your models here.
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ["id", "serial", "brand", "model"]
