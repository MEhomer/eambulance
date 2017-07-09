# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-01 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20170425_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_id',
        ),
        migrations.AlterField(
            model_name='comment',
            name='from_timestamp',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='patient',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='to_timestamp',
            field=models.BigIntegerField(),
        ),
    ]