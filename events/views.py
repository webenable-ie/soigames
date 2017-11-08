from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Venue
# Create your views here.

# Venues Views


class VenueList(ListView):
    template_name = 'events/venue_list.html'
    model = Venue
    context_object_name = 'venues'


class VenueDetail(DetailView):
    template_name = 'events/venue_detail.html'
    model = Venue

    def get_context_data(self, **kwargs):
        context = super(VenueDetail, self).get_context_data(**kwargs)
        return context


