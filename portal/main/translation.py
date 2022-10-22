from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Birthday)
class BirthdayTranslationOptions(TranslationOptions):
    fields = ('fio', 'position',)


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'user', 'division')