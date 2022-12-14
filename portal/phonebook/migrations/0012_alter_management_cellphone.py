# Generated by Django 4.0.6 on 2022-08-05 08:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0011_alter_management_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='management',
            name='cellphone',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message='Номер телефона необходимо вводить в формате: «9-999-999-99-99».', regex='^\\d{1}-\\d{3}-\\d{3}-\\d{2}-\\d{2}$')], verbose_name='Сотовый телефон'),
        ),
    ]
