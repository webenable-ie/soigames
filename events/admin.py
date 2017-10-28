from django.contrib import admin
from .models import Event, Venue


# Register your models here.

class EventModelAdmin(admin.ModelAdmin):
    list_display = [
        "event_name",
        "event_date",
        "event_start_time",
        "event_end_time",
    ]
    list_filter = [
        "event_date"
    ]

    class Meta:
        model = Event


admin.site.register(Event, EventModelAdmin)
admin.site.register(Venue)
