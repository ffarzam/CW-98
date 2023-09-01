from django.db import models
from Accounts.models import Band


# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=50)
    audio_file = models.FileField(upload_to="AudioFile/% Y/% m/% d/")
    cover_photo = models.ImageField(upload_to="Image% Y/% m/% d/")
    upload_date = models.DateField(auto_now_add=True, editable=False)
    genre = models.ManyToManyField(Genre)
    band = models.ForeignKey(Band, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.title
