# Generated by Django 4.0.6 on 2022-08-05 05:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='cellphone',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Номер телефона необходимо вводить в формате: «9-999-999-99-99».', regex='^\\d{1}-\\d{3}-\\d{3}-\\d{2}-\\d{2}$')]),
        ),
        migrations.AlterField(
            model_name='management',
            name='cellphone',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Номер телефона необходимо вводить в формате: «9-999-999-99-99».', regex='^\\d{1}-\\d{3}-\\d{3}-\\d{2}-\\d{2}$')], verbose_name='Сотовый телефон'),
        ),
        migrations.AlterField(
            model_name='management',
            name='fio',
            field=models.CharField(max_length=255, unique=True, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='phone',
            field=models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(message='Номер телефона необходимо вводить в формате: «99-99-99».', regex='^\\d{2}-\\d{2}-\\d{2}$')], verbose_name='Номер телефона'),
        ),
    ]
