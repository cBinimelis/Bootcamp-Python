from django.urls import path
from . import views

urlpatterns = [
    path("brand/", views.brand_list, name="brand_list"),
    path("brand/create/", views.brand_create, name="brand_create"),
    path("brand/<int:pk>/edit", views.brand_edit, name="brand_edit"),
]
