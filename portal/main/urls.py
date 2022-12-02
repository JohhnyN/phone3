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
    path('send', send, name='send'),
    path('<slug:slug>', article_detail, name='article_detail'),
    path('maintest/', views.MaintestListView.as_view(), name='maintest'),
    path('maintest_add/', views.MaintestCreateView.as_view(), name='maintest_add'),
    path('maintest_update/<pk>/', views.MaintestUpdateView.as_view(), name='maintest_update'),
    path('maintest_delete/<pk>/', views.MaintestDeleteview.as_view(), name='maintest_delete'),
    path('parenttest/', views.ParenttestListView.as_view(), name='parenttest'),
    path('parenttest_add/', views.ParenttestCreateView.as_view(), name='parenttest_add'),
    path('parenttest_update/<pk>/', views.ParenttestUpdateView.as_view(), name='parenttest_update'),
    path('parenttest_delete/<pk>/', views.ParenttestDeleteview.as_view(), name='parenttest_delete'),
]