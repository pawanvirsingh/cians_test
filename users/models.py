from __future__ import unicode_literals
from datetime import date
from django.db import models


class JobFinder(models.Model):
    serial = models.CharField(max_length=255, null=True)
    resume = models.BooleanField(default=False,)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=20, null=True)
    current_address = models.CharField(max_length=255, null=True)
    corrected_address = models.CharField(max_length=255, null=True)
    nearest_city = models.CharField(max_length=100, null=True)
    prefered_location = models.CharField(max_length=255, null=True)
    company_current = models.CharField(max_length=255, null=True)
    ctc = models.FloatField(null=True, blank=True)
    designation = models.CharField(max_length=255, null=True)
    skills = models.CharField(max_length=255, null=True)
    experience = models.FloatField(null=True)

    