from django.urls import path, include
from . import views

app_name = "laboratorio"

urlpatterns = [
    # Labos -------------------------------------------------------------------
    path("laboratorio/", views.laboratorio_list, name="laboratorio_list"),
    path("laboratorio/create/", views.laboratorio_create, name="laboratorio_create"),
    path("laboratorio/<int:pk>/edit", views.laboratorio_edit, name="laboratorio_edit"),
    path(
        "laboratorio/<int:pk>/delete",
        views.laboratorio_delete,
        name="laboratorio_delete",
    ),
]
