from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Department)
class DepartmentTranslationOptions(TranslationOptions):
    fields = ('department',)


@register(Division)
class DivisionTranslationOptions(TranslationOptions):
    fields = ('division',)


@register(Employees)
class EmployeesTranslationOptions(TranslationOptions):
    fields = ('fio', 'position',)