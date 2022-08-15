from django.core.exceptions import PermissionDenied
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from .forms import *


class PermissionMixin(object):

    def get_object(self, *args, **kwargs):
        obj = super(PermissionMixin, self).get_object(*args, **kwargs)
        if not obj.created_by == self.request.user:
            raise PermissionDenied()
        else:
            return obj


class EmployeesListView(ListView):
    model = Employees
    context_object_name = 'employees'


class EmployeesCreateView(CreateView):
    model = Employees
    form_class = EmployeesForm
    success_url = reverse_lazy('phonebook')


def load_division(request):
    department_id = request.GET.get('department')
    divisions = Division.objects.filter(department_id=department_id).order_by('division')
    return render(request, 'phonebook/division_dropdown_list_options.html', {'divisions': divisions})


class DepartmentListView(ListView):
    model = Department
    context_object_name = 'departments'


class DepartmentCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    success_url = reverse_lazy('departments')


class DepartmentUpdateView(UpdateView):
    model = Department
    form_class = DepartmentForm
    success_url = reverse_lazy('departments')


class DepartmentDelete(DeleteView):
    model = Department
    success_url = reverse_lazy('departments')


class DivisionListView(ListView):
    model = Division
    context_object_name = 'divisions'


class DivisionCreateView(CreateView):
    model = Division
    form_class = DivisionForm
    success_url = reverse_lazy('divisions')


class DivisionDeleteView(DeleteView):
    model = Division
    success_url = reverse_lazy('divisions')


class DivisionUpdateView(UpdateView):
    model = Division
    form_class = DivisionForm
    success_url = reverse_lazy('divisions')

