from django.urls import path, include
from . import views

app_name = "management"

urlpatterns = [
    path("", views.home, name="home"),
]