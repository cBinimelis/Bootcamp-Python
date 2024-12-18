from django.urls import path
from orders import views

app_name = "orders"

urlpatterns = [
    path("", views.order_list, name="order_list"),
    path("check-create/", views.check_create, name="check_create"),
]
