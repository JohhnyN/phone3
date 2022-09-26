import os
from django import forms

from django.forms import DateInput

from .models import *


class BirthdayForm(forms.ModelForm):
    class Meta:
        model = Birthday
        fields = '__all__'


