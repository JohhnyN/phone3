from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportModelAdmin
from .models import *


@admin.register(Birthday)
class EmployeesAdmin(ImportExportModelAdmin, TranslationAdmin):
    list_display = ('fio', 'position', 'date', 'get_html_photo',)
    search_fields = ('fio',)

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = 'Фото'


@admin.register(News)
class NewsAdmin(ImportExportModelAdmin, TranslationAdmin):
    list_display = ('title', 'slug', 'text', 'create_date', 'update_date', 'user', 'division')
    prepopulated_fields = {'slug': ('title',)}


