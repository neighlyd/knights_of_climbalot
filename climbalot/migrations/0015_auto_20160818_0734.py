# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 07:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climbalot', '0014_auto_20160818_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='start_date',
            field=models.DateField(),
        ),
    ]