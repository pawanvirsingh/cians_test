# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-11 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='job_finder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=255, null=True)),
                ('resume', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('current_address', models.CharField(max_length=255, null=True)),
                ('corrected_address', models.CharField(max_length=255, null=True)),
                ('nearest_city', models.CharField(max_length=100, null=True)),
                ('prefered_location', models.CharField(max_length=255, null=True)),
                ('company_current', models.CharField(max_length=255, null=True)),
                ('ctc', models.FloatField(blank=True, null=True)),
                ('designation', models.CharField(max_length=255, null=True)),
                ('skills', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='user_company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('company_address', models.CharField(max_length=255, null=True)),
                ('company_name', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]