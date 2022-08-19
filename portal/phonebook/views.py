import http
from urllib import request

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from .forms import *


class EmployeesListView(ListView):
    model = Employees
    context_object_name = 'employees'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get('q')
        if query:
            return qs.filter(Q(fio__icontains=query) |
                             Q(position__icontains=query) |
                             Q(department__department__icontains=query) |
                             Q(division__division__icontains=query) |
                             Q(phone__phone__icontains=query))
        return Employees.objects.filter()


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


class DepartmentListView(LoginRequiredMixin, ListView):
    model = Department
    context_object_name = 'departments'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get('q')
        if query:
            return qs.filter(Q(department__icontains=query))
        return Department.objects.filter()


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


class DivisionListView(LoginRequiredMixin, ListView):
    model = Division
    context_object_name = 'divisions'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get('q')
        if query:
            return qs.filter(Q(division__icontains=query) |
                             Q(department__department__icontains=query))
        return Division.objects.filter()


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

