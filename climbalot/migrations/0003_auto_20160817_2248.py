# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 22:48
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climbalot', '0002_auto_20160817_2245'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='y_routes',
            options={'verbose_name_plural': 'Y-Routes'},
        ),
        migrations.AlterField(
            model_name='monkey',
            name='experience',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]