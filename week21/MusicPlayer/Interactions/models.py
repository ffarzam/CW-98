from django.db import models


# Create your models here.


class Like(models.Model):
    user = models.ForeignKey("Accounts.Base", on_delete=models.CASCADE)
    song = models.ForeignKey("Songs.Song", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} liked on {self.song.title}"


class Comment(models.Model):
    content = models.TextField()
    is_confirmed = models.BooleanField(default=False)
    user = models.ForeignKey("Accounts.Base", on_delete=models.CASCADE)
    song = models.ForeignKey("Songs.Song", on_delete=models.CASCADE)
    send_date = models.DateField(auto_now_add=True, editable=False)

    def __str__(self):
        return f"{self.user.username} commented on {self.song.title}"


class Playlist(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    user = models.ForeignKey("Accounts.Base", on_delete=models.CASCADE)
    song = models.ManyToManyField("Songs.Song", blank=True)

    def __str__(self):
        return self.title
