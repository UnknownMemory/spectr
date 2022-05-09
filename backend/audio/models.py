from django.db import models

from user.models import User


class Album(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="album_artist")
    name = models.TextField(null=False)
    cover = models.URLField()
    released = models.DateTimeField()


class Genre(models.Model):
    name = models.TextField()


class Track(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="track_artist")
    trackname = models.TextField(null=False)
    cover = models.URLField()
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, related_name="album", null=True)
    genre = models.ForeignKey(
        Genre, on_delete=models.SET_NULL, related_name="track_genre", null=True
    )
    play = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    private = models.BooleanField(default=False)


class Playlist(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    name = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)


class Playlist_Track(models.Model):
    playlist_id = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name="playlist_id")
    track_id = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name="track_id")
    pos = models.IntegerField()
