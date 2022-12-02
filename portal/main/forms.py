import os
from django import forms
from modeltranslation.forms import TranslationModelForm
from django.utils.translation import gettext as _

from django.forms import DateInput

from .models import *


class BirthdayForm(TranslationModelForm):
    class Meta:
        model = Birthday
        fields = ('fio', 'fio_kk', 'date', 'position', 'position_kk', 'photo')


class MaintestForm(forms.ModelForm):
    class Meta:
        model = MainTest
        fields = '__all__'


class ParenttestForm(forms.ModelForm):
    class Meta:
        model = ParentTest
        fields = ('test', 'test_ru', 'test_kk', 'title_ru', 'title_kk')
