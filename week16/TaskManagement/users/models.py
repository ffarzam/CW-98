from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    img = models.ImageField(upload_to='image/', null=True, blank=True)

    def __str__(self):
        return self.username
