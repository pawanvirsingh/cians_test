# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-13 01:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180811_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_finder',
            name='experience',
            field=models.FloatField(null=True),
        ),
    ]
