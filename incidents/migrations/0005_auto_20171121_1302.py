# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 13:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0004_auto_20171107_1139'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incident',
            options={'ordering': ['-reported'], 'verbose_name': 'Incident', 'verbose_name_plural': 'Incidents'},
        ),
    ]
