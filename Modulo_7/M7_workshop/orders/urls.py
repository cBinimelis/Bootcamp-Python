from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path("", views.home, name="home"),
    path("api/home", views.api_home, name="api_home"),
    path("api/<int:pk>/detail", views.api_order_detail, name="api_order_detail"),
    path("api/<int:pk>/create-detail", views.create_detail, name="create_detail"),
    path("check-create", views.check_create, name="check_create"),
]
