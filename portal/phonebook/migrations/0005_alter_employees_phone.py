# Generated by Django 4.0.6 on 2022-08-05 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0004_alter_employees_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='phone',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='phonebook.phone', verbose_name='телефон'),
        ),
    ]