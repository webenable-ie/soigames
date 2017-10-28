from django.contrib import admin

from .models import Incident, IncidentAction
# Register your models here.


class IncidentModelAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "code",
        "venue",
        "is_athlete_involved",
    ]
    list_filter = [
        "code",
        "is_athlete_involved",
    ]

    class Meta:
        model = Incident


admin.site.register(Incident)
admin.site.register(IncidentAction)


