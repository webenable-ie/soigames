from django.conf.urls import url
from .views import IncidentList, IncidentDetail, IncidentCreateView

urlpatterns = [
    url(r'^$', IncidentList.as_view(), name="incidents_list"),
    url(r'^incident_detail/(?P<pk>\d+)', IncidentDetail.as_view(), name="incident_detail"),
    url(r'^create/$', IncidentCreateView.as_view(), name="create_incident")
]