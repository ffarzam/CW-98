from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/', default="def.jpg")

    def __str__(self) -> str:
        return f"{self.name}: {self.bio}"
