from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import mark_safe


class CustomUser(AbstractUser):
    img = models.ImageField(upload_to='image/', null=True, blank=True)

    def img_preview(self):
        if self.img:
            return mark_safe(f'<img src = "{self.img.url}" width = "150" height="150"/> ')
    def __str__(self):
        return self.username
