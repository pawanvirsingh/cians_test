# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-13 02:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20180813_0154'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='job_finder',
            new_name='JobFinder',
        ),
    ]