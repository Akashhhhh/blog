# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-18 05:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180918_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 18, 5, 26, 17, 593753, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 18, 5, 26, 17, 593437, tzinfo=utc)),
        ),
    ]
