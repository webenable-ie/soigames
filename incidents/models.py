from django.db import models

# Create your models here.


class Incident(models.Model):
    INCIDENTS_CODES = (
        ('nn', 'None'),
        ('mr', 'Minor'),
        ('sr', 'Serious'),
        ('cr', 'Critical'),
    )

    title = models.CharField(max_length=250, verbose_name="Title")
    venue = models.ForeignKey('events.Venue', verbose_name="Venue", related_name="Incidents", on_delete=None)
    code = models.CharField(max_length=2, choices=INCIDENTS_CODES, default='nn')
    description = models.TextField(verbose_name="Description")
    functional_area = models.ForeignKey('configtables.FunctionalArea',
                                        verbose_name="Functional Area",
                                        related_name="Incidents",
                                        on_delete=None)
    is_athlete_involved = models.BooleanField(default=False, verbose_name="Involves an Athlete")

    class Meta:
        verbose_name = 'Incident'
        verbose_name_plural = 'Incidents'


class IncidentAction(models.Model):
    ACTION_STATUSES = (
        ('P', 'Pending'),
        ('C', 'Complete'),
    )
    title = models.CharField(max_length=250, verbose_name="Title")
    status = models.CharField(max_length=1, choices=ACTION_STATUSES, default='P')
    incident = models.ForeignKey(Incident,
                                 on_delete=models.CASCADE,
                                 verbose_name="Incidents",
                                 related_name="Actions",
                                 null=True,
                                 )
