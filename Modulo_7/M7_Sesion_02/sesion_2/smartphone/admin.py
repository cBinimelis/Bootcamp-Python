from django.contrib import messages
from gettext import ngettext
from django.contrib import admin
from .form import SmartphoneForm

from .models import Smartphone


@admin.register(Smartphone)
class SmartphoneAdmin(admin.ModelAdmin):
    list_display = [
        "model",
        "storage",
        "ram",
        "screen_size",
        "height",
        "price",
        "status",
    ]
    search_fields = ["model"]
    list_filter = ["height"]
    ordering = ["-price", "model"]
    form = SmartphoneForm

    fieldsets = (
        ("Basic", {"fields": ("model", "ram")}),
        ("Advanced", {"fields": ("height", "price", "status")}),
    )

    def marcar_agotado(self, request, queryset):
        actualizados = queryset.update(status="agotado")
        self.message_user(
            request,
            ngettext(
                "%d smartphone was updated", "%d smartphones were updated", actualizados
            )
            % actualizados,
            messages.SUCCESS,
        )

    def marcar_disponible(self, request, queryset):
        actualizados = queryset.update(status="disponible")
        self.message_user(
            request,
            ngettext(
                "%d smartphone was updated", "%d smartphones were updated", actualizados
            )
            % actualizados,
            messages.SUCCESS,
        )

    actions = [marcar_agotado, marcar_disponible]
