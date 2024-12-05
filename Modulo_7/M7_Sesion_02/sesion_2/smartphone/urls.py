from django.urls import path
from smartphone import views

app_name = "smartphone"

urlpatterns = [
    path("", views.home, name="home"),
    path("create", views.create, name="create"),
    path("create-multiple", views.create_multiple, name="create_multiple"),
    path("update", views.update, name="update"),
    path("update-multiple", views.update_multiple, name="update_multiple"),
]
