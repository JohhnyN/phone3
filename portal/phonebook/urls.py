from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.EmployeesListView.as_view(), name='phonebook'),
    path('add/', views.EmployeesCreateView.as_view(), name='employees_add'),
    path('ajax/load-division/', views.load_division, name='ajax_load_division'),
    path('addDepartment', views.DepartmentCreateView.as_view(), name='department_add'),
    path('addDivision', views.DivisionCreateView.as_view(), name='division_add'),
    path('departments', views.DepartmentListView.as_view(), name='departments'),
    path('divisions', views.DivisionListView.as_view(), name='divisions'),
    path('delete_department/<pk>/', views.DepartmentDelete.as_view(), name="delete_department"),
]
