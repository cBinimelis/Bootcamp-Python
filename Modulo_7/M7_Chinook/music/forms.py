from django import forms
from .models import Artist, Album, Genre, MediaType, Playlist, Track


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["title", "artist"]


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ["name"]


class MediaTypeForm(forms.ModelForm):
    class Meta:
        model = MediaType
        fields = ["name"]


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ["name", "tracks"]
