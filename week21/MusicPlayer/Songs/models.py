from django.db import models


# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=50)
    audio_file = models.FileField(upload_to="AudioFile/%Y/%m/%d/")
    cover_photo = models.ImageField(upload_to="Image/%Y/%m/%d/")
    upload_date = models.DateField(auto_now_add=True, editable=False)
    genres = models.ManyToManyField(Genre)
    band = models.ForeignKey("Accounts.Band", on_delete=models.PROTECT, null=True, blank=True)

    @property
    def song_artists(self):
        # songs = Song.objects.prefetch_related("artist_set").annotate(name=F("artist__name")).filter(id=self.id)
        artists = self.artist_set.all()
        return list(artists)

    @property
    def song_genres(self):
        songs = self.genres.all()
        return list(songs)

    @property
    def number_of_likes(self):
        # qs = Like.objects.select_related("song").filter(song=self.id).aggregate(count=Count("song"))
        likes = self.like_set.all()
        return len(likes)

    def __str__(self):
        return self.title
