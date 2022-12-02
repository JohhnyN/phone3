from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'user', 'division')


@register(MainTest)
class MainTestTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(ParentTest)
class ParentTestTranslationOptions(TranslationOptions):
    fields = ('test', 'title',)