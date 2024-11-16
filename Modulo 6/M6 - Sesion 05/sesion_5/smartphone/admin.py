from django.contrib import admin

from .models import Smartphone


@admin.register(Smartphone)
class SmartphoneAdmin(admin.ModelAdmin):
    list_display = ["model"]
