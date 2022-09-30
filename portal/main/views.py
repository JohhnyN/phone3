import datetime


from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, TemplateView
from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from html2image import Html2Image
from .forms import *
from django.db.models import Q
from django.contrib.messages.views import SuccessMessageMixin
from django.conf import settings


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

    if birthday:
        print('Отправка письма')
        for b in birthday:

            # Путь к Открытке
            card = settings.STATICFILES_DIRS
            card = ''.join(card) + '/img/Открытка.png'

            # Данные ДР
            fio = b.fio
            position = b.position

            # Путь к фото ДР
            url = settings.MEDIA_ROOT
            new_url = url.rsplit("\\", 1)[0]
            photo = new_url + b.photo.url

            # Контекст для рендеринга
            context = {
                'card': card,
                'fio': fio,
                'position': position,
                'photo': photo,
            }
            html = render_to_string('main/source_email.html', context)

            # Получение карточки
            folder = url + '/Card'
            hti = Html2Image(output_path=folder)
            fio_card = fio.rsplit(" ", 2)[0]
            filename = fio_card + '.jpg'
            hti.screenshot(html_str=html, save_as=filename, size=(724, 420))
            print('есть карточка')

            # Отправка письма
            image_path = folder + '/' + filename
            context = {'filename': image_path}
            html = render_to_string('main/email_card.html', context)
            subject = 'C Днем Рождения ' + fio
            print(subject)
            mail = EmailMessage(
                subject=subject,
                body=html,
                from_email='portal@kmo.kz',
                to=['zh.nurushev@kmo.kz'],
            )
            mail.content_subtype = "html"
            mail.send()
            print('письмо ушло')

    return redirect('birthday')

