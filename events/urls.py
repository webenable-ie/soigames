from django.conf.urls import url
from .views import venue_list, VenueDetail

urlpatterns = [
    url(r'^$', venue_list, name="venue_list"),
    url(r'^venue-detail/(?P<pk>\d+)', VenueDetail.as_view(), name="venue_detail")
]
