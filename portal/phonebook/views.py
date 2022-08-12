from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import ProtectedError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DeleteView
from .models import *
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


class DepartmentDelete(DeleteView):
    model = Department
    success_url = reverse_lazy('departments')
    error_url = reverse_lazy('departments')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        error_url = self.get_error_url()
        try:
            self.object.delete()
            return HttpResponseRedirect(success_url)
        except models.deletion.ProtectedError:
            return HttpResponseRedirect(error_url)


class DivisionListView(ListView):
    model = Division
    context_object_name = 'divisions'


class DivisionCreateView(CreateView):
    model = Division
    form_class = DivisionForm
    success_url = reverse_lazy('phonebook')