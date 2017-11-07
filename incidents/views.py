from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect

from .models import Incident
from .forms import IncidentCreateForm

# Create your views here.


class IncidentList(ListView):
    template_name = 'incidents/incidents_list.html'
    model = Incident
    context_object_name = 'incidents'


class IncidentDetail(DetailView):
    template_name = 'incidents/incident_detail.html'
    model = Incident
    context_object_name = 'incident'

    def get_context_data(self, **kwargs):
        context = super(IncidentDetail, self).get_context_data(**kwargs)
        return context


class IncidentCreateView(LoginRequiredMixin, CreateView):
    form_class = IncidentCreateForm
    login_url = '/login/'
    template_name = 'incidents/incident_create.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super(IncidentCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(IncidentCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Record an Incident'
        return context


