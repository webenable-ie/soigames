from django.contrib import admin
from . models import Sport, FunctionalArea, VenueType

# Register your models here.

admin.site.register(Sport)
admin.site.register(FunctionalArea)
admin.site.register(VenueType)
