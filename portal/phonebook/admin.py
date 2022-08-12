from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(Phone)
class PhoneAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('phone',)


@admin.register(Department)
class DepartmentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('department',)


@admin.register(Division)
class DivisionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('division', 'department',)
    list_filter = ('department',)


@admin.register(Employees)
class EmployeesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('fio', 'position', 'division', 'email', 'cellphone', 'phone',)
    list_filter = ('division', 'department',)


@admin.register(Management)
class ManagementAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('fio', 'position', 'choice', 'email', 'cellphone', 'phone')