# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 02:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climbalot', '0011_remove_monkey_crest'),
    ]

    operations = [
        migrations.AddField(
            model_name='monkey',
            name='crest',
            field=models.ImageField(default=1, upload_to='crests/'),
            preserve_default=False,
        ),
    ]