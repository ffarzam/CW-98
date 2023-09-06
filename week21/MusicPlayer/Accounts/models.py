from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.db.models import F
from django.utils.translation import gettext_lazy as _
from django.db import models
from .manager import CustomManager
from Songs.models import Song
from Interactions.models import Like, Playlist


class Base(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=25, verbose_name=_("Username"), unique=True)
    name = models.CharField(verbose_name=_("Name"), max_length=100)
    email = models.EmailField(verbose_name=_("Email"), unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name=_("Joined Date"), auto_now_add=True, editable=False)
    last_modify = models.DateTimeField(verbose_name=_("Last Modify"), auto_now=True, editable=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ["username"]

    objects = CustomManager()

    def __str__(self):
        return self.email

    def number_of_playlist(self):
        return len(Playlist.objects.select_related("user").filter(user=self))

    def get_artist(self):
        qs = Base.objects.filter(id=self.id)
        if qs.exists():
            base = qs.get()
            usn = base.username
            artist = Artist.objects.filter(username=usn)
            if artist.exists():
                artist = artist.get()
                return artist
            else:
                return None

    def get_user(self):
        qs = Base.objects.filter(id=self.id)
        if qs.exists():
            base = qs.get()
            usn = base.username
            user = User.objects.filter(username=usn)
            if user.exists():
                user = user.get()
                return user
            else:
                return None

    def number_of_songs(self):
        artist = self.get_artist()
        return len(artist.song.all())

        # return len(Playlist.objects.select_related("user").prefetch_related('song').filter(user=self).annotate(
        #     song_id=F("song__id")).filter(song_id__isnull=False).values("song_id").distinct())

    def number_of_likes(self):
        return len(Like.objects.select_related("user").filter(user=self))

    @property
    def is_permitted(self):
        qs = Base.objects.filter(id=self.id)

        if qs.exists():
            base = qs.get()
            usn = base.username
            user = User.objects.filter(username=usn)
            artist = Artist.objects.filter(username=usn)
            if user.exists():
                user = user.get()
                if user.user_type == "V":
                    return True
            elif artist.exists():
                return True
            else:
                return True


class User(Base):
    Free = "F"
    VIP = "V"
    CHOICES = (
        (Free, 'Free'),
        (VIP, 'VIP'),
    )
    user_type = models.CharField(max_length=6, choices=CHOICES, default=Free)
    image = models.ImageField(upload_to='users/% Y/% m/% d/', null=True, blank=True)
    vip_until = models.DateField(null=True, blank=True)


class Band(models.Model):
    name = models.CharField(max_length=50)
    start_band = models.DateField(auto_now_add=True, editable=False)
    end_band = models.DateField(null=True, blank=True)


class Artist(Base):
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='artists/% Y/% m/% d/', null=True, blank=True)
    band = models.ForeignKey(Band, on_delete=models.PROTECT, null=True, blank=True)
    song = models.ManyToManyField(Song, blank=True)
