from django.shortcuts import render, get_object_or_404
from .models import Incident
# Create your views here.


def incidents_list(request):
    context = {"incidents": Incident.objects.all()}
    template = "incidents_list.html"

    return render(request, template, context)


def incident_detail(request):
    pass

