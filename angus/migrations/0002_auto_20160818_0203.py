# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-18 02:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('angus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='grade',
            field=models.CharField(choices=[('BR', 'Bronze'), ('SL', 'Silver'), ('GL', 'Gold'), ('PL', 'Platinum'), ('DI', 'Diamond'), ('MA', 'Master'), ('CH', 'Challenger')], default='BR', max_length=120),
        ),
    ]