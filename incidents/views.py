from django.views.generic import DetailView, CreateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.urls import reverse

from .models import Incident, IncidentAction
from .forms import IncidentCreateForm, IncidentEditForm, ActionCreateForm

# Create your views here.


class IncidentListView(ListView):
    """List all incidents and paginates by 3 """
    model = Incident
    template_name = 'incidents/incidents_list.html'
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        context = super(IncidentListView, self).get_context_data(*args, **kwargs)
        incident_list = Incident.objects.all()
        paginator = Paginator(incident_list, self.paginate_by)

        page = self.request.GET.get('page')
        try:
            objects = paginator.page(page)
        except PageNotAnInteger:
        # If page is not an integer, deliver first page.
            objects = paginator.page(1)
        except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
            objects = paginator.page(paginator.num_pages)
            context['objects'] = objects
        return context


class IncidentDetailView(LoginRequiredMixin, DetailView):
    template_name = 'incidents/incident_detail.html'
    login_url = '/login/'
    model = Incident
    context_object_name = 'incident'

    def get_context_data(self, **kwargs):
        context = super(IncidentDetailView, self).get_context_data(**kwargs)
        return context


class IncidentEditView(LoginRequiredMixin, UpdateView):
    form_class = IncidentEditForm
    login_url = '/login/'
    template_name = 'incidents/incident_create.html'

    def get_context_data(self, *args, **kwargs):
        context = super(IncidentEditView, self).get_context_data(*args, **kwargs)
        title = self.get_object().title
        context['title'] = f'Update Incident: {title}'
        return context

    def get_queryset(self):
        return Incident.objects.filter(user=self.request.user)


class IncidentCreateView(LoginRequiredMixin, CreateView):
    model = Incident
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


class ActionCreateView(LoginRequiredMixin, CreateView):
    model = IncidentAction
    form_class = ActionCreateForm
    login_url = '/login/'
    template_name = 'incidents/action_create.html'

    def form_valid(self, form):
        action = form.save(commit=False)
        incident_id = form.data['incident_id']
        incident = get_object_or_404(Incident, id=incident_id)
        action.incident = incident
        return super(ActionCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ActionCreateView, self).get_context_data(**kwargs)
        context['i_id'] = self.kwargs['incident_id']
        return context

    def get_success_url(self):
        return reverse('incident_detail', args=(self.object.incident.pk,))