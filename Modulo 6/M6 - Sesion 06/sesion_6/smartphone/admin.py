from django.contrib import admin

from .models import Smartphone


@admin.register(Smartphone)
class SmartphoneAdmin(admin.ModelAdmin):
    list_display = ["model",'storage','ram','screen_size', 'height','price']
    search_fields=['model']
    list_filter=['height']
    ordering=['-price','model']
    
    fieldsets=(
        ('Basic',{
            'fields':('model','ram')
        }),
        ('Cost',{
            'fields':('height','price')
        })
    )