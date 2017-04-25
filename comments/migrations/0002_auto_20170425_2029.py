# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-25 20:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_timestamp']},
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_id',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='comment',
            name='from_timestamp',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='patient',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='to_timestamp',
            field=models.BigIntegerField(null=True),
        ),
    ]
