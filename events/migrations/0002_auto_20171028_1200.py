# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 11:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configtables', '0002_venuetype'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
        migrations.AlterModelOptions(
            name='venue',
            options={'verbose_name': 'Venue', 'verbose_name_plural': 'Venues'},
        ),
        migrations.AddField(
            model_name='event',
            name='event_date',
            field=models.DateField(null=True, verbose_name='Date'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_end_time',
            field=models.TimeField(null=True, verbose_name='End Time'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_sport',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='configtables.Sport', verbose_name='Sport'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_start_time',
            field=models.TimeField(null=True, verbose_name='Start Time'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_name',
            field=models.CharField(max_length=250, verbose_name='Event'),
        ),
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='events.Venue', verbose_name='Venue'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='venue_name',
            field=models.CharField(max_length=250, verbose_name='Venue'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='venue_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configtables.VenueType', verbose_name='Type'),
        ),
    ]