from django.urls import path
from orders import views

app_name = "orders"

urlpatterns = [
    path("", views.order_list, name="order_list"),
    path("api/order_list", views.api_order_list, name="api_order_list"),
    path("api/<int:pk>/detail", views.api_order_detail, name="api_order_detail"),
    path("api/<int:pk>/create-detail", views.create_detail, name="create_detail"),
    path("check-create/", views.check_create, name="check_create"),
]
