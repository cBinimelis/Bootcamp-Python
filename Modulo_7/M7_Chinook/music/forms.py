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
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "artist": forms.Select(attrs={"class": "form-select"}),
        }


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }


class MediaTypeForm(forms.ModelForm):
    class Meta:
        model = MediaType
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ["name", "tracks"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "tracks": forms.Select(attrs={"class": "form-select"}),
        }


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = [
            "name",
            "composer",
            "miliseconds",
            "size_bytes",
            "unit_price",
            "album",
            "genre",
            "media_type",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "composer": forms.TextInput(attrs={"class": "form-control"}),
            "miliseconds": forms.NumberInput(attrs={"class": "form-control"}),
            "size_bytes": forms.NumberInput(attrs={"class": "form-control"}),
            "unit_price": forms.NumberInput(attrs={"class": "form-control"}),
            "album": forms.Select(attrs={"class": "form-select"}),
            "genre": forms.Select(attrs={"class": "form-select"}),
            "media_type": forms.Select(attrs={"class": "form-select"}),
        }
