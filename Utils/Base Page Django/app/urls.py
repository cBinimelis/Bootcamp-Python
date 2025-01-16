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
]
