# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-09 09:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20200609_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='reviewDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 9, 9, 15, 35, 776055, tzinfo=utc)),
        ),
    ]