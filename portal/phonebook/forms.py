from django import forms
from .models import *


class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['division'].queryset = Division.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['division'].queryset = Division.objects.filter(department_id=department_id).order_by('division')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['division'].queryset = self.instance.department.division_set.order_by('division')


class EmployeesUpdateForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class DivisionForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = '__all__'
