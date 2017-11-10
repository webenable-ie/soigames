from django.conf.urls import url
from .views import incident_list_view, incident_detail_view, \
    IncidentCreateView, IncidentEditView, ActionCreateView

urlpatterns = [
    url(r'^$', incident_list_view, name="incidents_list"),
    url(r'^incident_detail/(?P<pk>\d+)$', incident_detail_view, name="incident_detail"),
    url(r'^incident_detail/(?P<pk>\d+)/add_action', ActionCreateView.as_view(), name="add_action"),
    url(r'^create/$', IncidentCreateView.as_view(), name="create_incident"),
    url(r'^incident_detail/(?P<pk>\d+)/edit$', IncidentEditView.as_view(), name="edit_incident")
]