# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FunctionalArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fa_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Functional Area',
                'verbose_name_plural': 'Functional Areas',
                'ordering': ['fa_name'],
            },
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sp_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Sport',
                'verbose_name_plural': 'Sports',
                'ordering': ['sp_name'],
            },
        ),
    ]