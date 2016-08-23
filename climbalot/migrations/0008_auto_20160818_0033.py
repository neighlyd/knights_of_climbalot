# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 00:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('climbalot', '0007_auto_20160817_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='monkey',
            name='home_gym',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='climbalot.Gym'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='extra_points',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='y_routes',
            name='c5_10_a',
            field=models.IntegerField(default=0, verbose_name='5.10a'),
        ),
        migrations.AlterField(
            model_name='y_routes',
            name='c5_10_b',
            field=models.IntegerField(default=0, verbose_name='5.10b'),
        ),
        migrations.AlterField(
            model_name='y_routes',
            name='c5_10_c',
            field=models.IntegerField(default=0, verbose_name='5.10c'),
        ),
        migrations.AlterField(
            model_name='y_routes',
            name='c5_10_d',
            field=models.IntegerField(default=0, verbose_name='5.10d'),
        ),
        migrations.AlterField(
            model_name='y_routes',
            name='c5_11_a',
            field=models.IntegerField(default=0, verbose_name='5.11a'),
        ),
        migrations.AlterField(
            model_name='y_routes',
            name='c5_11_b',
            field=models.IntegerField(default=0, verbose_name='5.11b'),
        ),
        migrations.AlterField(
            model_name='y_routes',
            name='c5_11_c',
            field=models.IntegerField(default=0, verbose_name='5.11c'),
        ),
        migrations.AlterField(
            model_name='y_routes',
            name='c5_11_d',
            field=models.IntegerField(default=0, verbose_name='5.11d'),
        ),
        migrations.AlterField(
            model_name='y_routes',
            name='c5_12_a',
            field=models.IntegerField(default=0, verbose_name='5.12a'),
        ),
        migrations.AlterField(
            model_name='y_routes',
            name='c5_12_b',
            field=models.IntegerField(default=0, verbose_name='5.12b'),
        ),
        migrations.AlterField(
            model_name='y_routes',
            name='c5_12_c',
            field=models.IntegerField(default=0, verbose_name='5.12c'),
        ),
        migrations.AlterField(
            model_name='y_routes',
            name='c5_12_d',
            field=models.IntegerField(default=0, verbose_name='5.12d'),
        ),
        migrations.AlterField(
            model_name='y_routes',
            name='c5_7',
            field=models.IntegerField(default=0, verbose_name='5.7'),
        ),
        migrations.AlterField(
            model_name='y_routes',
            name='c5_8_neg',
            field=models.IntegerField(default=0, verbose_name='5.8-'),
        ),
        migrations.AlterField(
            model_name='y_routes',
            name='c5_8_pos',
            field=models.IntegerField(default=0, verbose_name='5.8+'),
        ),
        migrations.AlterField(
            model_name='y_routes',
            name='c5_9_neg',
            field=models.IntegerField(default=0, verbose_name='5.9-'),
        ),
        migrations.AlterField(
            model_name='y_routes',
            name='c5_9_pos',
            field=models.IntegerField(default=0, verbose_name='5.9+'),
        ),
    ]