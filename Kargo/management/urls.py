from django.urls import path, include
from . import views

app_name = "management"

urlpatterns = [
    path("", views.home, name="home"),
    # Pistas-------------------------------------------------------------------
    path("pista/", views.pista_list, name="pista_list"),
    path("pista/create/", views.pista_create, name="pista_create"),
    path("pista/<int:pk>/edit", views.pista_edit, name="pista_edit"),
    path("pista/<int:pk>/delete", views.pista_delete, name="pista_delete"),
    path("pista/<int:pk>", views.pista_view, name="pista_view"),
    # Pistas-------------------------------------------------------------------
    path("reserva/", views.reserva_list, name="reserva_list"),
    path("reserva/create/", views.reserva_create, name="reserva_create"),
    path("reserva/<int:pk>/edit", views.reserva_edit, name="reserva_edit"),
    path("reserva/<int:pk>/delete", views.reserva_delete, name="reserva_delete"),
    path("reserva/<int:pk>", views.reserva_view, name="reserva_view"),
]
