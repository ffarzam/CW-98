from django.db import models
from Songs.models import Song
from Accounts.models import User


# Create your models here.


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} liked on {self.song.title}"


class Comment(models.Model):
    content = models.TextField()
    is_confirmed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} commented on {self.song.title}"


class Playlist(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ManyToManyField(Song)

    def __str__(self):
        return self.title