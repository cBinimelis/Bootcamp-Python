from django.contrib import admin
from .models import Reserva, Cliente, Pista

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Pista)
admin.site.register(Reserva)


admin.site.site_header = "Book Store"
admin.site.site_title = "Panel de control, proyecto BookStore"
admin.site.site_title = "Administrador Django"


# Register your models here.
@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "score", "clasification"]
    readonly_fields = ["created", "modified"]
    list_filter = ("score", "modified")

    def clasification(self, obj):
        if obj.score < 1000:
            score = "Low"
        elif obj.score > 1000 and obj.score < 2500:
            score = "Medium"
        else:
            score = "High"

        return score
