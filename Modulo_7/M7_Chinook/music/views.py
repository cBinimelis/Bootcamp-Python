from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Artist
from .forms import ArtistForm


# Create your views here.
def home(request):
    return render(request, "music/home.html")


def artist_list(request):
    artists = Artist.objects.all()
    context = {"artists": artists}
    return render(request, "music/artist/artist_list.html", context)


def artist_create(request):
    if request.method == "POST":
        form = ArtistForm(request.POST)
        form.save()
        return redirect("artist_list")
    else:
        form = ArtistForm()
    context = {"form": form}
    return render(request, "music/artist/artist_form.html", context)


def artist_edit(request, pk):
    artist = Artist.objects.get(id=pk)
    if request.method == "POST":
        form = ArtistForm(request.POST, instance=artist)
        form.save()
        return redirect("artist_list")
    else:
        form = ArtistForm(instance=artist)
    context = {"form": form}
    return render(request, "music/artist/artist_form.html", context)


def artist_delete(request, pk):
    artist = Artist.objects.get(id=pk)
    if request.method == "POST":
        artist.delete()
        return redirect("artist_list")
    else:
        context = {"artist": artist}
        return render(request, "music/artist/artist_confirm_delete.html", context)


def artist_view(request, pk):
    artist = Artist.objects.get(id=pk)
    context = {"artist": artist}
    return render(request, "music/artist/artist_view.html", context)
