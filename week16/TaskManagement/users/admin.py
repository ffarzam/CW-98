from django.contrib import admin
from .models import CustomUser
from django.contrib.sessions.models import Session
from django.urls import reverse
from django.utils.html import format_html, urlencode
from django.db.models import Count


# Register your models here.

# admin.site.register(CustomUser)


class SessionAdmin(admin.ModelAdmin):
    def session_data(self, obj):
        return obj.get_decoded()

    list_display = ['session_key', 'session_data', 'expire_date']


admin.site.register(Session, SessionAdmin)


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "task_count"]
    # ordering = ["username", "email",]

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



