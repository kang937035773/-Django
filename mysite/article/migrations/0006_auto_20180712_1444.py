# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-07-12 06:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20180712_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 12, 6, 44, 58, 810712, tzinfo=utc)),
        ),
    ]