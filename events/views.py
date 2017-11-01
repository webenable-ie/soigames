from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Venue
# Create your views here.

# Venues Views

def venue_list(request,):
    context = {"venues": Venue.objects.all()}
    template = 'venue_list.html'

    return render(request, template, context)


# def venue_detail(request, id):
#     venue = get_object_or_404(Venue, id=id)
#     context = {"venue": venue}
#
#     return render(request, 'venue_detail.html', context)

class VenueDetail(DetailView):
    template_name = 'venue_detail.html'
    model = Venue

    def get_context_data(self, **kwargs):
        context = super(VenueDetail, self).get_context_data(**kwargs)
        return context


