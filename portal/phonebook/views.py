import http
from urllib import request
import io
import xlsxwriter
import xlwt
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, View
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


class EmployeesCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Employees
    form_class = EmployeesForm
    success_message = "Сотрудник был успешно добавлен"
    success_url = reverse_lazy('phonebook')


def load_division(request):
    department_id = request.GET.get('department')
    divisions = Division.objects.filter(department_id=department_id).order_by('division')
    return render(request, 'phonebook/division_dropdown_list_options.html', {'divisions': divisions})


class EmployeesUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Employees
    initial = {'department': '', 'division': '', }
    form_class = EmployeesUpdateForm
    success_message = "Сотрудник был успешно изменен"
    success_url = reverse_lazy('phonebook')


class EmployeesDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Employees
    success_message = "Сотрудник был удален"
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


class DepartmentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Department
    form_class = DepartmentForm
    success_message = "Департамент был успешно добавлен"
    success_url = reverse_lazy('departments')


class DepartmentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Department
    form_class = DepartmentForm
    success_message = "Департамент был успешно изменен"
    success_url = reverse_lazy('departments')


class DepartmentDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Department
    success_message = "Департамент был удален"
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


class DivisionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Division
    form_class = DivisionForm
    success_message = "Отдел был успешно добавлен"
    success_url = reverse_lazy('divisions')


class DivisionUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Division
    form_class = DivisionForm
    success_message = "Отдел был успешно изменен"
    success_url = reverse_lazy('divisions')


class DivisionDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Division
    success_message = "Отдел был удален"
    success_url = reverse_lazy('divisions')


class DownloadPhonebook(View):
    def get(self, request):
        text = '«Қазмедиа орталығы» басқарушы компаниясы» ЖШС қызметкерлерінің телефон нөмірлері'
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet('Телефонная книга')
        merge_format = workbook.add_format({
            'bold': True,
            'border': 6,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': '#D7E4BC',
        })
        worksheet.merge_range('A1:G7', text, merge_format)
        worksheet.set_column('A:Z', 35)
        data = Employees.objects.all().values_list('fio', 'position', 'department__department', 'division__division',
                                                   'email', 'cellphone', 'phone__phone')
        table_range = 'A10:G' + str(len(data) + 10)
        options = {'data': data,
                   'style': 'Table Style Light 11',
                   'columns': [{'header': 'ФИО'},
                               {'header': 'Должность'},
                               {'header': 'Департамент'},
                               {'header': 'Отдел'},
                               {'header': 'Email'},
                               {'header': 'Сотовый телефон'},
                               {'header': 'Рабочий телефон'},
                               ]}
        worksheet.add_table(table_range, options)
        workbook.close()
        output.seek(0)
        filename = 'Phonebook.xlsx'
        response = HttpResponse(
            output,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=%s' % filename

        return response
