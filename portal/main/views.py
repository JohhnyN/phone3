import datetime

import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, View, TemplateView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.template import loader


from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin


class Index(TemplateView):

    template_name = 'main/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Index, self).get_context_data(*args, **kwargs)
        today = datetime.datetime.today()
        birthday = Birthday.objects.filter(date__month=today.month, date__day=today.day)
        context['birthday'] = birthday
        return context


class BirthdayListView(LoginRequiredMixin, ListView):
    model = Birthday
    context_object_name = 'birthday'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get('q')
        if query:
            return qs.filter(Q(fio__icontains=query) |
                             Q(date__icontains=query))
        return Birthday.objects.filter()


class BirthdayCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Birthday
    form_class = BirthdayForm
    success_message = "День рождения был успешно добавлен"
    success_url = reverse_lazy('birthday')


class BirthdayUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Birthday
    form_class = BirthdayForm
    success_message = "День рождения был успешно изменен"
    success_url = reverse_lazy('birthday')


class BirthdayDelete(LoginRequiredMixin, SuccessMessageMixin,  DeleteView):
    model = Birthday
    success_message = "День рождения удален"
    success_url = reverse_lazy('birthday')


def send_card(request):
    today = datetime.datetime.today()
    birthday = Birthday.objects.filter(date__month=today.month, date__day=today.day)

    for b in birthday:
        fio = b.fio
        position = b.position
        photo = b.photo.url

        if birthday:
            print(photo)
            html_message = loader.render_to_string(
                r'D:\phone\portal\main\templates\main\email_card.html',
                {
                    'photo': photo,
                    'fio': fio,
                    'position': position,
                }
            )
            send_mail(
                'Тема',
                'Открытка',
                'zh@kmo.kz',
                ['zh.nurushev@kmo.kz'],
                fail_silently=False,
                html_message=html_message,
            )
    return redirect('birthday')