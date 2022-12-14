from django.db import models
from django.core.validators import RegexValidator


class Phone(models.Model):
    phone = models.CharField(max_length=8, verbose_name='Номер телефона')

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'Номер телефона'
        verbose_name_plural = 'Номера телефонов'
        ordering = ['phone']


class Department(models.Model):
    department = models.CharField(max_length=255, unique=True, verbose_name='Департамент')

    def __str__(self):
        return self.department

    class Meta:
        verbose_name = 'Департамент'
        verbose_name_plural = 'Департаменты'
        ordering = ['department']


class Division(models.Model):
    department = models.ForeignKey('Department', on_delete=models.PROTECT, verbose_name='Департамент',
                                   related_name='division')
    division = models.CharField(max_length=255, unique=True, verbose_name='Отдел')

    def __str__(self):
        return self.division

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'
        ordering = ['division']


class Employees(models.Model):
    fio = models.CharField(max_length=255, unique=True, verbose_name='Сотрудник')
    position = models.CharField(max_length=255, verbose_name='Должность')
    department = models.ForeignKey('Department', on_delete=models.PROTECT, verbose_name='Департамент',
                                   related_name='employees',)
    division = models.ForeignKey('Division', on_delete=models.PROTECT, verbose_name='Отдел', related_name='employees',
                                 null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    cellphone_regex = RegexValidator(regex=r'^\d{1}-\d{3}-\d{3}-\d{2}-\d{2}$',
                                     message="Номер телефона необходимо вводить в формате: «9-999-999-99-99».")
    cellphone = models.CharField(validators=[cellphone_regex], max_length=15, verbose_name='Сотовый телефон',
                                 blank=True, null=True)
    phone = models.ForeignKey('Phone', default='', on_delete=models.SET_DEFAULT, verbose_name='телефон',
                              null=True, blank=True)
    photo = models.ImageField(upload_to='employees_photos', verbose_name='Фото сотрудников', blank=True)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['fio']


class Management(models.Model):
    CHOICES = [
        ('Руководство', 'Руководство'),
        ('Административный блок', 'Административный блок'),
        ('Администратор по информационной безопасности ', 'Администратор по информационной безопасности ')
    ]
    fio = models.CharField(max_length=255, unique=True, verbose_name='ФИО')
    position = models.CharField(max_length=255, verbose_name='Должность')
    choice = models.CharField(max_length=255, choices=CHOICES, verbose_name='Руководство')
    email = models.EmailField(blank=True, null=True)
    cellphone_regex = RegexValidator(regex=r'^\d{1}-\d{3}-\d{3}-\d{2}-\d{2}$',
                                     message="Номер телефона необходимо вводить в формате: «9-999-999-99-99».")
    cellphone = models.CharField(validators=[cellphone_regex], max_length=15, verbose_name='Сотовый телефон',
                                 blank=True, null=True)
    phone = models.ForeignKey('Phone', default='', on_delete=models.SET_DEFAULT, verbose_name='телефон',
                              null=True, blank=True)

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = 'Руководство'
        verbose_name_plural = 'Руководство'
        ordering = ['fio']

