from django.urls import path
from . import views

app_name = "music"

urlpatterns = [
    path("", views.home, name="home"),
    
    #ARTIST URLS
    path("artist/", views.artist_list, name="artist_list"),
    path("artist/create/", views.artist_create, name="artist_create"),
    path("artist/<int:pk>/edit", views.artist_edit, name="artist_edit"),
    path("artist/<int:pk>/delete", views.artist_delete, name="artist_delete"),
    path("artist/<int:pk>", views.artist_view, name="artist_view"),
    
    #ALBUM URLS
    path("album/", views.album_list, name="album_list"),
    path("album/create/", views.album_create, name="album_create"),
    path("album/<int:pk>/edit", views.album_edit, name="album_edit"),
    path("album/<int:pk>/delete", views.album_delete, name="album_delete"),
    path("album/<int:pk>", views.album_view, name="album_view"),
]
