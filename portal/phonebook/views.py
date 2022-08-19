import http
from urllib import request

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from .forms import *


class EmployeesListView(ListView):
    model = Employees
    context_object_name = 'employees'


class EmployeesCreateView(LoginRequiredMixin, CreateView):
    model = Employees
    form_class = EmployeesForm
    success_url = reverse_lazy('phonebook')


def load_division(request):
    department_id = request.GET.get('department')
    divisions = Division.objects.filter(department_id=department_id).order_by('division')
    return render(request, 'phonebook/division_dropdown_list_options.html', {'divisions': divisions})


class EmployeesUpdateView(LoginRequiredMixin, UpdateView):
    model = Employees
    initial = {'department': '', 'division': '', }
    form_class = EmployeesUpdateForm
    success_url = reverse_lazy('phonebook')


class EmployeesDelete(LoginRequiredMixin, DeleteView):
    model = Employees
    success_url = reverse_lazy('phonebook')


class DepartmentListView(ListView):
    model = Department
    context_object_name = 'departments'


class DepartmentCreateView(LoginRequiredMixin, CreateView):
    model = Department
    form_class = DepartmentForm
    success_url = reverse_lazy('departments')


class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Department
    form_class = DepartmentForm
    success_url = reverse_lazy('departments')


class DepartmentDelete(LoginRequiredMixin, DeleteView):
    model = Department
    success_url = reverse_lazy('departments')


class DivisionListView(ListView):
    model = Division
    context_object_name = 'divisions'


class DivisionCreateView(LoginRequiredMixin, CreateView):
    model = Division
    form_class = DivisionForm
    success_url = reverse_lazy('divisions')


class DivisionUpdateView(LoginRequiredMixin, UpdateView):
    model = Division
    form_class = DivisionUpdateForm
    success_url = reverse_lazy('divisions')


class DivisionDeleteView(LoginRequiredMixin, DeleteView):
    model = Division
    success_url = reverse_lazy('divisions')

