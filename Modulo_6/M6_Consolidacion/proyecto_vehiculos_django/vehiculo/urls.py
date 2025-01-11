from django.urls import path, include
from . import views

app_name = "vehiculo"

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add, name="add"),
    path("list/", views.list, name="list"),
]
