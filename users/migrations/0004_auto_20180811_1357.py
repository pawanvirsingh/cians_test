# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-11 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_job_finder_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_finder',
            name='experience',
            field=models.IntegerField(null=True),
        ),
    ]