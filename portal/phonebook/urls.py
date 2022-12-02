from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.EmployeesListView.as_view(), name='phonebook'),
    path('employees_add/', views.EmployeesCreateView.as_view(), name='employees_add'),
    path('ajax/load-division/', views.load_division, name='ajax_load_division'),
    path('employees_update/<pk>/', views.EmployeesUpdateView.as_view(), name='employees_update'),
    path('employees_delete/<pk>/', views.EmployeesDelete.as_view(), name="employees_delete"),
    path('departments', views.DepartmentListView.as_view(), name='departments'),
    path('department_add', views.DepartmentCreateView.as_view(), name='department_add'),
    path('department_update/<pk>/', views.DepartmentUpdateView.as_view(), name='department_update'),
    path('department_delete/<pk>/', views.DepartmentDelete.as_view(), name="department_delete"),
    path('divisions', views.DivisionListView.as_view(), name='divisions'),
    path('division_add', views.DivisionCreateView.as_view(), name='division_add'),
    path('division_update/<pk>/', views.DivisionUpdateView.as_view(), name='division_update'),
    path('division_delete/<pk>/', views.DivisionDeleteView.as_view(), name='division_delete'),
    re_path(r'^export/xls/$', views.DownloadPhonebook.as_view(), name='download_phonebook'),
]

