from django import forms
from django.forms import DateInput

from .models import *


class BirthdayForm(forms.ModelForm):
    class Meta:
        model = Birthday
        fields = '__all__'
        widgets = {
            'fio': forms.TextInput(attrs={'class': 'form-control'}),
            'position': forms.TextInput(attrs={'class': 'form-control'}),
            'date': DateInput(format=('%Y-%m-%d'), attrs={'class': 'date', 'id': "datepicker", 'placeholder': 'Select a date', 'type': 'date'}),

        }