from django.urls import path
from . import views

urlpatterns = [
    path("inputbook/", views.inputbook, name="inputbook"),
    path("register/", views.register, name="register"),
]
