# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 22:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('climbalot', '0003_auto_20160817_2248'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='c_routes',
            options={'verbose_name_plural': 'C-Routes'},
        ),
        migrations.AlterModelOptions(
            name='v_routes',
            options={'verbose_name_plural': 'V-Routes'},
        ),
    ]