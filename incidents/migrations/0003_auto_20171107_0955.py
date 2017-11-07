# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-07 09:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0002_incidentaction_incident'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='reported',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Reported on'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='incident',
            name='resolved_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]