# Generated by Django 4.0.6 on 2022-08-05 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0012_alter_management_cellphone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='management',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]