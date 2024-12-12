from django.urls import path
from . import views

urlpatterns = [
    # Equipment
    path("", views.equipment_list, name="equipment_list"),
    path("create/", views.equipment_create, name="equipment_create"),
    path("<int:pk>/edit", views.equipment_edit, name="equipment_edit"),
    path("<int:pk>/delete", views.equipment_delete, name="equipment_delete"),
    path("<int:pk>", views.equipment_view, name="equipment_view"),
    
    #Model
    path("model/", views.model_list, name="model_list"),
    path("model/create/", views.model_create, name="model_create"),
    path("model/<int:pk>/edit", views.model_edit, name="model_edit"),
    path("model/<int:pk>/delete", views.model_delete, name="model_delete"),
    path('model/<int:pk>', views.model_view,name='model_view'),
    
    # Brand
    path("brand/", views.brand_list, name="brand_list"),
    path("brand/create/", views.brand_create, name="brand_create"),
    path("brand/<int:pk>/edit", views.brand_edit, name="brand_edit"),
    path("brand/<int:pk>/delete", views.brand_delete, name="brand_delete"),
    path('brand/<int:pk>', views.brand_view,name='brand_view')
]
