from django.contrib import admin
from django.urls import path
from . import views

from .views import *

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('birthday', views.BirthdayListView.as_view(), name='birthday'),
    path('add_birthday', views.BirthdayCreateView.as_view(), name='birthday_add'),
    path('update_birthday/<pk>/', views.BirthdayUpdateView.as_view(), name='update_birthday'),
    path('delete_birthday/<pk>/', views.BirthdayDelete.as_view(), name='delete_birthday'),
]