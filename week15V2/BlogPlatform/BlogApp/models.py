from django.db import models
from Authors.models import Author


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.name}: {self.description}"


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    publication_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title}: {self.author}, {self.publication_date}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    comment_date = models.DateField()

    def __str__(self) -> str:
        return f"{self.post}:{self.author}, {self.comment_date}"
