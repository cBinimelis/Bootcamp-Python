from django.urls import path
from . import views

app_name="product"

urlpatterns =[
    path('',views.list, name='list'),
    path('add/',views.add, name='add'),
    path('edit/',views.edit, name='edit'),
]