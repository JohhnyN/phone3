from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportModelAdmin
from .models import *


@admin.register(Birthday)
class EmployeesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('fio', 'fio_kk', 'position', 'position_kk', 'date', 'get_html_photo',)
    list_display_links = ('fio', 'fio_kk',)
    search_fields = ('fio',)

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = 'Фото'


@admin.register(News)
class NewsAdmin(ImportExportModelAdmin, TranslationAdmin):
    list_display = ('title', 'slug', 'text', 'create_date', 'update_date', 'user', 'division')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(MainTest)
class MainTestAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'title_ru', 'title_kk')


@admin.register(ParentTest)
class ParentTestAdmin(TranslationAdmin):
    list_display = ('id', 'test_ru', 'test_kk', 'title', 'title_ru', 'title_kk')