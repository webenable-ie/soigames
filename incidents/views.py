from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Incident
# Create your views here.


def incidents_list(request):
    incidents = Incident.objects.all()
    template = "incidents_list.html"

    return render(request, template, {"incidents": incidents})

