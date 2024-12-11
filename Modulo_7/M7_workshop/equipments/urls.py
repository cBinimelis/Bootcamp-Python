from django.urls import path
from . import views

urlpatterns = [
    # Equipment
    path("", views.equipment_list, name="equipment_list"),
    path("create/", views.equipment_create, name="equipment_create"),
    path("<int:pk>/edit", views.equipment_edit, name="equipment_edit"),
    path("<int:pk>/delete", views.equipment_delete, name="equipment_delete"),
    path("<int:pk>", views.equipment_view, name="equipment_view"),
    # Brand
    path("brand/", views.brand_list, name="brand_list"),
    path("brand/create/", views.brand_create, name="brand_create"),
    path("brand/<int:pk>/edit", views.brand_edit, name="brand_edit"),
    path("brand/<int:pk>/delete", views.brand_delete, name="brand_delete"),
]
