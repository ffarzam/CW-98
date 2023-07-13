from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=500)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    publication_date = models.DateField()

