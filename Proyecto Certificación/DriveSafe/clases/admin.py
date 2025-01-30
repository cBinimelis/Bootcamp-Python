from django.contrib import admin
from .models import Vehiculo, Clase, DetalleClase

# Register your models here.
admin.site.register(Vehiculo)
admin.site.register(Clase)
admin.site.register(DetalleClase)


admin.site.site_header = "Drive Safe"
admin.site.site_title = "Panel de control, proyecto autoescuela"
admin.site.site_header = "Administrador Django"


# Register your models here.
# @admin.register(BookModel)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ["title", "author", "score", "clasification"]
#     readonly_fields = ["created", "modified"]
#     list_filter = ("score", "modified")

#     def clasification(self, obj):
#         if obj.score < 1000:
#             score = "Low"
#         elif obj.score > 1000 and obj.score < 2500:
#             score = "Medium"
#         else:
#             score = "High"

#         return score
