# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-13 03:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0006_auto_20180813_0200'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThortalDownload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('download_count', models.IntegerField(default=0)),
                ('download_allowd', models.IntegerField(default=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
