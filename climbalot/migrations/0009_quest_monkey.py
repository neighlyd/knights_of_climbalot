# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 00:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('climbalot', '0008_auto_20160818_0033'),
    ]

    operations = [
        migrations.AddField(
            model_name='quest',
            name='monkey',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='climbalot.Monkey'),
            preserve_default=False,
        ),
    ]