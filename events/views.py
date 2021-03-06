from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Venue, Event
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



def event_list_view(request):
    template_name = 'events/event_list.html'
    events = Event.objects.all()
    context = {'events': events}
    return render(request, template_name, context)
