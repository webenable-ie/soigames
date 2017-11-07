# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 15:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidentaction',
            name='incident',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Actions', to='incidents.Incident', verbose_name='Incidents'),
        ),
    ]