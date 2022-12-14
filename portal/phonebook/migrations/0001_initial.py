# Generated by Django 4.0.6 on 2022-08-05 04:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=255, unique=True, verbose_name='Департамент')),
            ],
            options={
                'verbose_name': 'Департамент',
                'verbose_name_plural': 'Департаменты',
                'ordering': ['department'],
            },
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.CharField(max_length=255, unique=True, verbose_name='Отдел')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='division', to='phonebook.department', verbose_name='Департамент')),
            ],
            options={
                'verbose_name': 'Отдел',
                'verbose_name_plural': 'Отделы',
                'ordering': ['division'],
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(message='Номер телефона необходимо вводить в формате: «99-99-99».', regex='^\\d{2}-\\d{2}-\\d{2}$')])),
            ],
            options={
                'verbose_name': 'Номер телефона',
                'verbose_name_plural': 'Номера телефонов',
                'ordering': ['phone'],
            },
        ),
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=255, unique=True, verbose_name='Руководство')),
                ('position', models.CharField(max_length=255, verbose_name='Должность')),
                ('choice', models.CharField(choices=[('Руководство', 'Руководство'), ('Административный блок', 'Административный блок'), ('Администратор по информационной безопасности ', 'Администратор по информационной безопасности ')], max_length=255, verbose_name='Руководство')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('cellphone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Номер телефона необходимо вводить в формате: «9-999-999-99-99».', regex='^\\d{1}-\\d{3}-\\d{3}-\\d{2}-d{2}$')])),
                ('phone', models.ForeignKey(default='-', on_delete=django.db.models.deletion.SET_DEFAULT, to='phonebook.phone', verbose_name='телефон')),
            ],
            options={
                'verbose_name': 'Руководство',
                'verbose_name_plural': 'Руководство',
                'ordering': ['fio'],
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=255, unique=True, verbose_name='Сотрудник')),
                ('position', models.CharField(max_length=255, verbose_name='Должность')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('cellphone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Номер телефона необходимо вводить в формате: «9-999-999-99-99».', regex='^\\d{1}-\\d{3}-\\d{3}-\\d{2}-d{2}$')])),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='employees', to='phonebook.division', verbose_name='Отдел')),
                ('phone', models.ForeignKey(default='-', on_delete=django.db.models.deletion.SET_DEFAULT, to='phonebook.phone', verbose_name='телефон')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
                'ordering': ['fio'],
            },
        ),
    ]
