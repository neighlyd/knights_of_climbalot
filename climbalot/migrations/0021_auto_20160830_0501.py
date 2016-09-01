# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 05:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climbalot', '0020_auto_20160830_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monkey',
            name='main_color_grade',
            field=models.CharField(blank=True, choices=[(1, 'Yellow'), (2, 'Green'), (3, 'Red'), (4, 'Blue'), (5, 'Orange'), (6, 'Purple'), (7, 'Black')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='monkey',
            name='main_v_grade',
            field=models.CharField(blank=True, choices=[(1, 'V1'), (2, 'V2'), (3, 'V3'), (4, 'V4'), (5, 'V5'), (6, 'V6'), (7, 'V7'), (8, 'V8'), (9, 'V9'), (10, 'V10')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='monkey',
            name='main_y_grade',
            field=models.CharField(blank=True, choices=[(1, '5.7'), ('5.8', ((2, '5.8-'), (3, '5.8+'))), ('5.9', ((4, '5.9-'), (5, '5.9+'))), ('5.10', ((6, '5.10a'), (7, '5.10b'), (8, '5.10c'), (9, '5.10d'))), ('5.11', ((10, '5.11a'), (11, '5.11b'), (12, '5.11c'), (13, '5.11d'))), ('5.12', ((14, '5.12a'), (15, '5.12b'), (16, '5.12c'), (17, '5.12d')))], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='quest',
            name='c_value',
            field=models.CharField(blank=True, choices=[(1, 'Yellow'), (2, 'Green'), (3, 'Red'), (4, 'Blue'), (5, 'Orange'), (6, 'Purple'), (7, 'Black')], max_length=1),
        ),
        migrations.AlterField(
            model_name='quest',
            name='v_value',
            field=models.CharField(blank=True, choices=[(1, 'V1'), (2, 'V2'), (3, 'V3'), (4, 'V4'), (5, 'V5'), (6, 'V6'), (7, 'V7'), (8, 'V8'), (9, 'V9'), (10, 'V10')], max_length=3),
        ),
        migrations.AlterField(
            model_name='quest',
            name='y_value',
            field=models.CharField(blank=True, choices=[(1, '5.7'), ('5.8', ((2, '5.8-'), (3, '5.8+'))), ('5.9', ((4, '5.9-'), (5, '5.9+'))), ('5.10', ((6, '5.10a'), (7, '5.10b'), (8, '5.10c'), (9, '5.10d'))), ('5.11', ((10, '5.11a'), (11, '5.11b'), (12, '5.11c'), (13, '5.11d'))), ('5.12', ((14, '5.12a'), (15, '5.12b'), (16, '5.12c'), (17, '5.12d')))], max_length=5),
        ),
    ]