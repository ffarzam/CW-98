from django.contrib import admin
from .models import Category, Task, Tag

# Register your models here.

admin.site.register(Category)

admin.site.register(Tag)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "is_active", ]
    readonly_fields = ["is_active"]

