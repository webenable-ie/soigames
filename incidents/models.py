from django.db import models
from django.urls import reverse
from django.conf import settings
from events.models import Venue

# Create your models here.


class Incident(models.Model):
    objects = models.Manager()
    INCIDENTS_CODES = (
        ('nn', 'None'),
        ('mr', 'Minor'),
        ('sr', 'Serious'),
        ('cr', 'Critical'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=250, verbose_name="Title")
    venue = models.ForeignKey(Venue, verbose_name="Venue", related_name="Incidents", on_delete=None)
    code = models.CharField(max_length=2, choices=INCIDENTS_CODES, default='nn')
    description = models.TextField(verbose_name="Description")
    reported = models.DateTimeField(auto_now_add=True,
                                    auto_now=False,
                                    null=False,
                                    blank=False,
                                    verbose_name='Reported on')
    resolved = models.BooleanField,
    resolved_time = models.DateTimeField(auto_now=False,
                                         auto_now_add=False,
                                         null=True,
                                         blank=True)
    functional_area = models.ForeignKey('configtables.FunctionalArea',
                                        verbose_name="Functional Area",
                                        related_name="Incidents",
                                        on_delete=None)
    is_athlete_involved = models.BooleanField(default=False, verbose_name="Involves an Athlete")

    class Meta:
        verbose_name = 'Incident'
        verbose_name_plural = 'Incidents'

    def get_absolute_url(self):
        return reverse('incident_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class IncidentAction(models.Model):
    """ Model for actions taken related to Incidents"""
    ACTION_STATUSES = (
        ('P', 'Pending'),
        ('C', 'Complete'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=250, verbose_name="Title")
    status = models.CharField(max_length=1, choices=ACTION_STATUSES, default='P')
    created = models.DateTimeField(auto_now_add=True,
                                   auto_now=False,
                                   null=False,
                                   blank=False,
                                   verbose_name='Reported on')
    completed_time = models.DateTimeField(auto_now=False,
                                          auto_now_add=False,
                                          null=True,
                                          blank=True,)
    incident = models.ForeignKey(Incident,
                                 on_delete=models.CASCADE,
                                 verbose_name="Incidents",
                                 related_name="Actions",
                                 null=True,)
    details = models.TextField

    # def get_absolute_url(self):
    #     return reverse('incident_detail', kwargs={'pk': self.incident.pk})
