from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Artist, Album, Genre, Track
from .forms import ArtistForm, AlbumForm, GenreForm, TrackForm


# Create your views here.
def home(request):
    return render(request, "music/home.html")


# ARTIST ----------------------------------------------------------------
def artist_list(request):
    artists = Artist.objects.all()
    context = {"artists": artists}
    return render(request, "music/artist/artist_list.html", context)


def artist_create(request):
    if request.method == "POST":
        form = ArtistForm(request.POST)
        form.save()
        return redirect("music:artist_list")
    else:
        form = ArtistForm()
    context = {"form": form}
    return render(request, "music/artist/artist_form.html", context)


def artist_edit(request, pk):
    artist = Artist.objects.get(id=pk)
    if request.method == "POST":
        form = ArtistForm(request.POST, instance=artist)
        form.save()
        return redirect("music:artist_list")
    else:
        form = ArtistForm(instance=artist)
    context = {"form": form}
    return render(request, "music/artist/artist_form.html", context)


def artist_delete(request, pk):
    artist = Artist.objects.get(id=pk)
    if request.method == "POST":
        artist.delete()
        return redirect("music:artist_list")
    else:
        context = {"artist": artist}
        return render(request, "music/artist/artist_confirm_delete.html", context)


def artist_view(request, pk):
    artist = Artist.objects.get(id=pk)
    context = {"artist": artist}
    return render(request, "music/artist/artist_view.html", context)


# ALBUM ----------------------------------------------------------------
def album_list(request):
    albums = Album.objects.all()
    context = {"albums": albums}
    return render(request, "music/album/album_list.html", context)


def album_create(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        form.save()
        return redirect("music:album_list")
    else:
        form = AlbumForm()
    context = {"form": form}
    return render(request, "music/album/album_form.html", context)


def album_edit(request, pk):
    album = Album.objects.get(id=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        form.save()
        return redirect("music:album_list")
    else:
        form = AlbumForm(instance=album)
    context = {"form": form}
    return render(request, "music/album/album_form.html", context)


def album_delete(request, pk):
    album = Album.objects.get(id=pk)
    if request.method == "POST":
        album.delete()
        return redirect("music:album_list")
    else:
        context = {"album": album}
        return render(request, "music/album/album_confirm_delete.html", context)


def album_view(request, pk):
    album = Album.objects.get(id=pk)
    context = {"album": album}
    return render(request, "music/album/album_view.html", context)


# GENRE ----------------------------------------------------------------


def genre_list(request):
    genres = Genre.objects.all()
    context = {"genres": genres}
    return render(request, "music/genre/genre_list.html", context)


def genre_create(request):
    if request.method == "POST":
        form = GenreForm(request.POST)
        form.save()
        return redirect("music:genre_list")
    else:
        form = GenreForm()
    context = {"form": form}
    return render(request, "music/genre/genre_form.html", context)


def genre_edit(request, pk):
    genre = Genre.objects.get(id=pk)
    if request.method == "POST":
        form = GenreForm(request.POST, instance=genre)
        form.save()
        return redirect("music:genre_list")
    else:
        form = GenreForm(instance=genre)
    context = {"form": form}
    return render(request, "music/genre/genre_form.html", context)


def genre_delete(request, pk):
    genre = Genre.objects.get(id=pk)
    if request.method == "POST":
        genre.delete()
        return redirect("music:genre_list")
    else:
        context = {"genre": genre}
        return render(request, "music/genre/genre_confirm_delete.html", context)


def genre_view(request, pk):
    genre = Genre.objects.get(id=pk)
    context = {"genre": genre}
    return render(request, "music/genre/genre_view.html", context)


# TRACK ----------------------------------------------------------------


def track_list(request):
    tracks = Track.objects.all()
    context = {"tracks": tracks}
    return render(request, "music/track/track_list.html", context)


def track_create(request):
    if request.method == "POST":
        form = TrackForm(request.POST)
        form.save()
        return redirect("music:track_list")
    else:
        form = TrackForm()
    context = {"form": form}
    return render(request, "music/track/track_form.html", context)


def track_edit(request, pk):
    track = Track.objects.get(id=pk)
    if request.method == "POST":
        form = TrackForm(request.POST, instance=track)
        form.save()
        return redirect("music:track_list")
    else:
        form = TrackForm(instance=track)
    context = {"form": form}
    return render(request, "music/track/track_form.html", context)


def track_delete(request, pk):
    track = Track.objects.get(id=pk)
    if request.method == "POST":
        track.delete()
        return redirect("music:track_list")
    else:
        context = {"track": track}
        return render(request, "music/track/track_confirm_delete.html", context)


def track_view(request, pk):
    track = Track.objects.get(id=pk)
    context = {"track": track}
    return render(request, "music/track/track_view.html", context)
