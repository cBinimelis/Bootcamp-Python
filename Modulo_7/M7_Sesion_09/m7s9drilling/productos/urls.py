"""
URL configuration for practica_orm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

app_name = "productos"

urlpatterns = [
    path("producto/list/", views.producto_list, name="producto_list"),
    path("producto/create/", views.producto_create, name="producto_create"),
    path("producto/<int:pk>/edit", views.producto_edit, name="producto_edit"),
    path("producto/<int:pk>/delete", views.producto_delete, name="producto_delete"),
    path("producto/<int:pk>", views.producto_view, name="producto_view"),
]
