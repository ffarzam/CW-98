from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db import models
from .manager import CustomManager
from Songs.models import Song


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

    REQUIRED_FIELDS = []

    objects = CustomManager()

    def __str__(self):
        return self.username


class User(Base):
    Normal = "Normal"
    VIP = "VIP"
    CHOICES = (
        (Normal, 'Normal'),
        (VIP, 'VIP'),
    )
    user_type = models.CharField(max_length=6, choices=CHOICES, default="Normal")
    image = models.ImageField(upload_to='users/% Y/% m/% d/', null=True, blank=True)
    vip_until = models.DateField(null=True, blank=True)


class Artist(Base):
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='artists/% Y/% m/% d/', null=True, blank=True)
    song = models.ManyToManyField(Song)


class Band(models.Model):
    name = models.CharField(max_length=50)
    start_band = models.DateField(auto_now_add=True, editable=False)
    end_band = models.DateField(null=True, blank=True, editable=True)