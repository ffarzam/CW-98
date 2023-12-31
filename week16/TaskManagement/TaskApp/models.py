from django.db import models
from users.models import CustomUser


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='image/', null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Tag(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    TODO = "todo"
    DOING = "doing"
    DONE = "done"
    status_choice = [
        (TODO, 'Todo'),
        (DOING, 'Doing'),
        (DONE, 'Done'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=status_choice)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    tag = models.ManyToManyField(Tag)
    file = models.FileField(upload_to='uploads/', null=True, blank=True)
    created = models.DateField(auto_now_add=True, editable=False)
    updated = models.DateField(auto_now=True, editable=False)
    is_active = models.BooleanField(default=True)

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def get_tags(self):
        task = Task.objects.get(id=self.id)
        tags = task.tag.all()
        return list(tags)

    def __str__(self):
        return f"{self.title}"