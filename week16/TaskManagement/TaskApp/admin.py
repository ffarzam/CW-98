from django.contrib import admin
from .models import Category, Task, Tag
import csv
from django.http import HttpResponse, JsonResponse
import json

# Register your models here.

admin.site.register(Category)

admin.site.register(Tag)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "is_active", "created", "updated"]
    readonly_fields = ["is_active"]
    actions = ["export_as_csv", "export_as_json"]

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export to CSV"

    def export_as_json(self, request, queryset):
        meta = self.model._meta
        data = list(queryset.values())
        response = JsonResponse(data, safe=False)
        response['Content-Disposition'] = 'attachment; filename={}.json'.format(meta)

        return response

    export_as_json.short_description = 'Export to Json'
