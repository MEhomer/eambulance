# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-01 20:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('diagnoses', '0002_auto_20170423_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diagnosis',
            name='diagnosis_id',
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='created_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='from_timestamp',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='patient',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='to_timestamp',
            field=models.BigIntegerField(),
        ),
    ]