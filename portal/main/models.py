from django.db import models


class Birthday(models.Model):
    fio = models.CharField(max_length=255, unique=True, verbose_name='Сотрудник')
    position = models.CharField(max_length=255, verbose_name='Должность')
    date = models.DateField(verbose_name='День рождения')
    photo = models.ImageField(upload_to='birthday_photos', verbose_name='Фото')

    class Meta:
        verbose_name = 'День рождения'
        verbose_name_plural = 'Дни рождения'
        ordering = ['fio']


# class News(models.Model):
#     title = models.CharField(max_length=255, unique=True, verbose_name='Новость')
#


