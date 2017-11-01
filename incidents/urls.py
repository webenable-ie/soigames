from django.conf.urls import url
from .views import incidents_list, incident_detail

urlpatterns = [
    url(r'^$', incidents_list, name="incidents_list"),
    url(r'^incident_detail/', incident_detail, name="incident_detail")
]