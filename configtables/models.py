from django.db import models

# Create your models here.


class Sport(models.Model):
    sp_name = models.CharField(max_length=100)

    def __str__(self):
        return self.sp_name

    class Meta:
        verbose_name = 'Sport'
        verbose_name_plural = 'Sports'
        ordering = ['sp_name']


class FunctionalArea(models.Model):
    objects = models.Manager()
    fa_name = models.CharField(max_length=100)

    def __str__(self):
        return self.fa_name

    class Meta:
        verbose_name = 'Functional Area'
        verbose_name_plural = 'Functional Areas'
        ordering = ['fa_name']


class VenueType(models.Model):
    vt_name = models.CharField(max_length=200)

    def __str__(self):
        return self.vt_name

    class Meta:
        verbose_name = 'Venue Type'
        verbose_name_plural = 'Venue Types'
        ordering = ['vt_name']

