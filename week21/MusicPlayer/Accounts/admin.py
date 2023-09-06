from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import BaseCreationForm, BaseChangeForm
from . import models


class BaseAdmin(UserAdmin):
    add_form = BaseCreationForm
    form = BaseChangeForm
    model = models.Base
    list_display = ("email", "username", "name", "is_staff", "is_active", "is_superuser",)
    list_filter = ("email", "username", "name", "is_staff", "is_active", "is_superuser",)
    fieldsets = (
        (None, {"fields": ("username", "name", "email", "password",)}),
        ("Permissions",
         {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "name", "email", "password1", "password2",
                "is_active", "is_staff", "is_superuser", "groups", "user_permissions"
            )}
         ),
    )
    # search_fields = ("phone", 'first_name__istartswith', 'last_name__istartswith')
    # ordering = ("phone", 'first_name', 'last_name')


admin.site.register(models.Base, BaseAdmin)

admin.site.register(models.User)
admin.site.register(models.Artist)
admin.site.register(models.Band)
