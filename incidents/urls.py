from django.conf.urls import url
from .views import (
    incident_list_view,
    incident_delete_view,
    IncidentDetailView,
    IncidentCreateView,
    IncidentEditView,
    ActionCreateView,
    ActionDeleteView
)

urlpatterns = [
    url(r'^$', incident_list_view, name="incidents_list"),
    url(r'^incident_detail/(?P<pk>\d+)$', IncidentDetailView.as_view(), name="incident_detail"),
    url(r'^incident_detail/(?P<incident_id>\d+)/add_action$', ActionCreateView.as_view(), name="add_action"),
    url(r'^delete/(?P<pk>\d+)$', incident_delete_view, name='delete_incident'),
    url(r'^create/$', IncidentCreateView.as_view(), name="create_incident"),
    url(r'^incident_detail/(?P<pk>\d+)/edit$', IncidentEditView.as_view(), name="edit_incident"),
    url(r'^incident_detail/action/delete/(?P<pk>\d+)$', ActionDeleteView.as_view(), name="delete_action"),
]
