from django.contrib import admin
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportModelAdmin
from .models import *


@admin.register(Birthday)
class EmployeesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('fio', 'position', 'date', 'get_html_photo',)
    search_fields = ('fio',)

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = 'Фото'


