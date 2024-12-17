from django.urls import path
from . import views

app_name = "music"

urlpatterns = [
    path("", views.home, name="home"),
    # ARTIST URLS
    path("artist/", views.artist_list, name="artist_list"),
    path("artist/create/", views.artist_create, name="artist_create"),
    path("artist/<int:pk>/edit", views.artist_edit, name="artist_edit"),
    path("artist/<int:pk>/delete", views.artist_delete, name="artist_delete"),
    path("artist/<int:pk>", views.artist_view, name="artist_view"),
    # ALBUM URLS
    path("album/", views.album_list, name="album_list"),
    path("album/create/", views.album_create, name="album_create"),
    path("album/<int:pk>/edit", views.album_edit, name="album_edit"),
    path("album/<int:pk>/delete", views.album_delete, name="album_delete"),
    path("album/<int:pk>", views.album_view, name="album_view"),
    # GENRE URLS
    path("genre/", views.genre_list, name="genre_list"),
    path("genre/create/", views.genre_create, name="genre_create"),
    path("genre/<int:pk>/edit", views.genre_edit, name="genre_edit"),
    path("genre/<int:pk>/delete", views.genre_delete, name="genre_delete"),
    path("genre/<int:pk>", views.genre_view, name="genre_view"),
    # TRACK URLS
    path("track/", views.track_list, name="track_list"),
    path("track/create/", views.track_create, name="track_create"),
    path("track/<int:pk>/edit", views.track_edit, name="track_edit"),
    path("track/<int:pk>/delete", views.track_delete, name="track_delete"),
    path("track/<int:pk>", views.track_view, name="track_view"),
]
