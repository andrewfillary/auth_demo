# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-11 20:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0009_auto_20170411_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 11, 20, 20, 55, 964254, tzinfo=utc)),
        ),
    ]
