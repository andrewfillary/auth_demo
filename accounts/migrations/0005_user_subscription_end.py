# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-11 19:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_user_subscription_end'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='subscription_end',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
