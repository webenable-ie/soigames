from django.conf.urls import url
from .views import VenueDetail, VenueList

urlpatterns = [
    url(r'^$', VenueList.as_view(), name="venue_list"),
    url(r'^venue-detail/(?P<slug>[\w-]+)', VenueDetail.as_view(), name="venue_detail"),
]
