from django.db import models


# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class MediaType(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Playlist(models.Model):
    name = models.CharField(max_length=50)
    tracks = models.ManyToManyField("Track")
    def __str__(self):
        return self.name


class Track(models.Model):
    name = models.CharField(max_length=50)
    composer = models.CharField(max_length=100)
    miliseconds = models.IntegerField()
    size_bytes = models.IntegerField()
    unit_price = models.IntegerField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    media_type = models.ForeignKey(MediaType, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
