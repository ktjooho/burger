# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 05:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('angus', '0005_auto_20160824_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guestbook',
            name='mod_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 24, 5, 22, 5, 893389, tzinfo=utc), verbose_name='datetime'),
        ),
        migrations.AlterField(
            model_name='guestbook',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 24, 5, 22, 5, 893124, tzinfo=utc), verbose_name='datetime'),
        ),
    ]