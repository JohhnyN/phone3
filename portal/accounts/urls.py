# from django.contrib.auth import views
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *


urlpatterns = [
    path('login/', login, name='login'),
    # path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
