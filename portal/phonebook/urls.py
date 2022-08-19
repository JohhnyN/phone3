from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.EmployeesListView.as_view(), name='phonebook'),
    path('add/', views.EmployeesCreateView.as_view(), name='employees_add'),
    path('ajax/load-division/', views.load_division, name='ajax_load_division'),
    path('update_employees/<pk>/', views.EmployeesUpdateView.as_view(), name='update_employees'),
    path('delete_employees/<pk>/', views.EmployeesDelete.as_view(), name="delete_employees"),
    path('departments', views.DepartmentListView.as_view(), name='departments'),
    path('add_Department', views.DepartmentCreateView.as_view(), name='department_add'),
    path('update_department/<pk>/', views.DepartmentUpdateView.as_view(), name='update_department'),
    path('delete_department/<pk>/', views.DepartmentDelete.as_view(), name="delete_department"),
    path('divisions', views.DivisionListView.as_view(), name='divisions'),
    path('add_Division', views.DivisionCreateView.as_view(), name='division_add'),
    path('delete_division/<pk>/', views.DivisionDeleteView.as_view(), name='delete_division'),
    path('update_division/<pk>/', views.DivisionUpdateView.as_view(), name='update_division'),
]

