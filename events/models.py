from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save
from configtables.models import VenueType, Sport

# Create your models here.


class Venue(models.Model):
    objects = models.Manager()
    venue_name = models.CharField(max_length=250, verbose_name='Venue')
    slug = models.SlugField(null=True, blank=True)
    venue_type = models.ForeignKey(VenueType, on_delete=None, verbose_name='Type')

    def __str__(self):
        return self.venue_name

    def get_absolute_url(self):
        return reverse('venue_detail', kwargs={'slug': self.slug})

    def create_slug(self, new_slug=None):
        slug = slugify(self.venue_name)
        if new_slug is not None:
            slug = new_slug
        else:
            slug = slugify(self.venue_name)
        
        return slug
            
    class Meta:
        verbose_name = 'Venue'
        verbose_name_plural = 'Venues'


def pre_save_venue_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = Venue.create_slug(instance)


pre_save.connect(pre_save_venue_receiver, sender=Venue)


class Event(models.Model):
    objects = models.Manager()
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

