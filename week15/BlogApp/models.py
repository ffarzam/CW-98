from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=500)

    def __str__(self) -> str:
        return f"{self.name}: {self.bio}"


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    publication_date = models.DateField()

    def __str__(self) -> str:
        return f"{self.title}: {self.author}, {self.publication_date}"


class Category(models.Model):
    name = models.CharField(max_length=100),
    description = models.TextField(),

    def __str__(self) -> str:
        return f"{self.name}: {self.description}"


class Comment(models.Model):
    post = models.CharField(max_length=100),
    author = models.CharField(max_length=50),
    content = models.TextField(),
    date = models.DateField()

    def __str__(self) -> str:
        return f"{self.post}:{self.author}({self.date})"
