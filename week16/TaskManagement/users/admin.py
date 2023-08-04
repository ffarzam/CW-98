from django.contrib import admin
from .models import CustomUser
from django.contrib.sessions.models import Session

# Register your models here.

admin.site.register(CustomUser)


class SessionAdmin(admin.ModelAdmin):
    def session_data(self, obj):
        return obj.get_decoded()

    list_display = ['session_key', 'session_data', 'expire_date']


admin.site.register(Session, SessionAdmin)

