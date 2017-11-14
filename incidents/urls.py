from django.conf.urls import url
from .views import IncidentListView, IncidentDetailView, IncidentCreateView, IncidentEditView, ActionCreateView

urlpatterns = [
    url(r'^$', IncidentListView.as_view(), name="incidents_list"),
    url(r'^incident_detail/(?P<pk>\d+)$', IncidentDetailView.as_view(), name="incident_detail"),
    url(r'^incident_detail/(?P<pk>\d+)/add_action', ActionCreateView.as_view(), name="add_action"),
    url(r'^create/$', IncidentCreateView.as_view(), name="create_incident"),
    url(r'^incident_detail/(?P<pk>\d+)/edit$', IncidentEditView.as_view(), name="edit_incident")
]