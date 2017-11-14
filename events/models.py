from django.db import models
from django.urls import reverse
from configtables.models import VenueType, Sport

# Create your models here.


class Venue(models.Model):
    venue_name = models.CharField(max_length=250, verbose_name='Venue')
    venue_type = models.ForeignKey(VenueType, on_delete=None, verbose_name='Type')

    def __str__(self):
        return self.venue_name

    def get_absolute_url(self):
        return reverse('venue_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Venue'
        verbose_name_plural = 'Venues'


class Event(models.Model):
    event_name = models.CharField(max_length=250, verbose_name='Event')
    venue = models.ForeignKey(Venue, on_delete=None, verbose_name='Venue', related_name='events')
    event_date = models.DateField(verbose_name='Date', null=True)
    event_start_time = models.TimeField(verbose_name='Start Time', null=True)
    event_end_time = models.TimeField(verbose_name='End Time', null=True)
    event_sport = models.ForeignKey(Sport, verbose_name='Sport', related_name='events', null=True)

    def __str__(self):
        return self.event_name

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

