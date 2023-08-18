from django.contrib import admin
from .models import CustomUser
from django.contrib.sessions.models import Session
from django.urls import reverse
from django.utils.html import format_html, urlencode
from django.db.models import Count


# Register your models here.

# admin.site.register(CustomUser)
class IsGreatUserFilter(admin.SimpleListFilter):
    title = 'is_great_user'
    parameter_name = 'is_great_user'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'Yes':
            return queryset.filter(task_count__gt=10)
        elif value == 'No':
            return queryset.exclude(task_count__gt=10)
        return queryset


class SessionAdmin(admin.ModelAdmin):
    def session_data(self, obj):
        return obj.get_decoded()

    list_display = ['session_key', 'session_data', 'expire_date']


admin.site.register(Session, SessionAdmin)


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "task_count", "is_great_user", 'img_preview']
    ordering = ["username", "email"]
    list_filter = ["username", "email", IsGreatUserFilter,]

    @admin.display(ordering='task_count')
    def task_count(self, user):
        url = (reverse('admin:TaskApp_task_changelist')
               + '?'
               + urlencode({
                    'user__id': str(user.id)
                }))

        return format_html('<a href="{}">{}</a>', url, user.task_count)

    task_count.short_description = 'Number Of Tasks'

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            task_count=Count('task__user')
        )

    def is_great_user(self, obj):
        if obj.task_count > 10:
            return True
        else:
            return False


