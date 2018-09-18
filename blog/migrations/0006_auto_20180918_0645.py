# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-18 06:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180918_0644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='create_date',
        ),
        migrations.AddField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 18, 6, 45, 26, 970597, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 18, 6, 45, 26, 970270, tzinfo=utc)),
        ),
    ]
