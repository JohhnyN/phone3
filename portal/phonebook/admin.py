from django.contrib import admin
from django.utils.safestring import mark_safe
from modeltranslation.admin import TranslationAdmin
from .models import *
from import_export.admin import ImportExportModelAdmin


@admin.register(Phone)
class PhoneAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('phone',)


@admin.register(Department)
class DepartmentAdmin(ImportExportModelAdmin, TranslationAdmin):
    list_display = ('id', 'department_ru', 'department_kk',)
    list_display_links = ('department_ru', 'department_kk',)


@admin.register(Division)
class DivisionAdmin(ImportExportModelAdmin, TranslationAdmin):
    list_display = ('id', 'division_ru', 'division_kk', 'department',)
    list_filter = ('department',)
    list_display_links = ('division_ru', 'division_kk',)


@admin.register(Employees)
class EmployeesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('fio_ru', 'fio_kk', 'position_ru', 'position_kk', 'create_date', 'update_date', 'get_photo')
    list_filter = ('division', 'department',)
    list_display_links = ('fio_ru', 'fio_kk',)
    search_fields = ('fio',)
    fields = ('fio_ru', 'fio_kk', 'position_ru', 'position_kk', 'department', 'division', 'email', 'cellphone', 'phone', 'photo', 'get_photo', 'create_date', 'update_date')
    readonly_fields = ('get_photo', 'create_date', 'update_date')

    def get_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width="50">')

    get_photo.short_description = 'Фото'


@admin.register(Management)
class ManagementAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('fio', 'position', 'choice', 'email', 'cellphone', 'phone')


admin.site.site_title = 'PORTAL'
admin.site.site_header = 'PORTAL'
