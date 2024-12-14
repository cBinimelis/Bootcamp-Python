from django.urls import path
from . import views

app_name = "music"

urlpatterns = [
    path("", views.home, name="home"),
    path("artist/", views.artist_list, name="artist_list"),
    path("artist/create/", views.artist_create, name="artist_create"),
    path("artist/<int:pk>/edit", views.artist_edit, name="artist_edit"),
    path("artist/<int:pk>/delete", views.artist_delete, name="artist_delete"),
    path("artist/<int:pk>", views.artist_view, name="artist_view"),
]
