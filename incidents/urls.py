from django.conf.urls import url
from .views import incidents_list

urlpatterns = [
    url(r'^$', incidents_list, name="incidents_list")
]