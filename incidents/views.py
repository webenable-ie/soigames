from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404

from .models import Incident, IncidentAction
from .forms import IncidentCreateForm, IncidentEditForm, ActionCreateForm

# Create your views here.


def incident_list_view(request):
    """Incident List View Function"""
    object_list = Incident.objects.all()
    paginator = Paginator(object_list, 3)

    page = request.GET.get('page')
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        objects = paginator.page(paginator.num_pages)
    return render(request, 'incidents/incidents_list.html', {'objects': objects})

@login_required
def incident_detail_view(request, pk=None):
    instance = get_object_or_404(Incident, pk=pk)
    context = {
        "title": instance.title,
        "instance": instance
    }

    return render(request, 'incidents/incident_detail.html', context)


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
        instance = form.save(commit=False)
        instance.incident = self.request.incident
        return super(ActionCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(ActionCreateView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Record an Incident'
        return context




