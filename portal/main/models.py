from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User, Group


class Birthday(models.Model):
    fio = models.CharField(max_length=255, unique=True, verbose_name='Сотрудник')
    fio_kk = models.CharField(max_length=255, unique=True, verbose_name='Қызметкер')
    position = models.CharField(max_length=255, verbose_name='Должность')
    position_kk = models.CharField(max_length=255, verbose_name='Қызмет атауы')
    date = models.DateField(verbose_name='День рождения')
    photo = models.ImageField(upload_to='birthday_photos', verbose_name='Фото')

    class Meta:
        verbose_name = 'День рождения'
        verbose_name_plural = 'Дни рождения'
        ordering = ['fio']

    def __str__(self):
        return self.fio


class News(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name=_('Новость'))
    slug = models.SlugField(unique=True)
    text = models.TextField(verbose_name=_('Текст'))
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Автор'))
    division = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name=_('Отдел'))

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['id']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})


class MainTest(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name=_('Родительский'))

    def __str__(self):
        return self.title


class ParentTest(models.Model):
    title = models.ForeignKey(MainTest, on_delete=models.CASCADE, verbose_name=_('Главный'))
    test = models.CharField(max_length=255, verbose_name=_('Дочерний'))


