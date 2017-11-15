from django import forms
from events.models import Venue
from configtables.models import FunctionalArea
from .models import Incident, IncidentAction


INCIDENTS_CODES = (
    ('nn', 'None'),
    ('mr', 'Minor'),
    ('sr', 'Serious'),
    ('cr', 'Critical'),
)

ACTION_STATUSES = (
    ('P', 'Pending'),
    ('C', 'Complete'),
)

class IncidentCreateForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}))
    venue = forms.ModelChoiceField(
        queryset=Venue.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}))
    functional_area = forms.ModelChoiceField(
        queryset=FunctionalArea.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}))
    code = forms.CharField(max_length=2,
        widget=forms.Select(choices=INCIDENTS_CODES,
        attrs={'class': 'form-control'}))
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Details here'}))

    class Meta:
        model = Incident
        fields = [
            'title',
            'venue',
            'functional_area',
            'code',
            'description'
        ]


class IncidentEditForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}))
    venue = forms.ModelChoiceField(queryset=Venue.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    functional_area = forms.ModelChoiceField(queryset=FunctionalArea.objects.all(),
                                             widget=forms.Select(attrs={'class': 'form-control'}))
    code = forms.CharField(max_length=2, widget=forms.Select(choices=INCIDENTS_CODES, attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                               'placeholder': 'Details here'}))

    class Meta:
        model = Incident
        fields = [
            'title',
            'venue',
            'functional_area',
            'code',
            'description'
        ]


class ActionCreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput({'class': 'form-control', 'placeholder': 'Title'}))
    status = forms.CharField(max_length=1, widget=forms.Select(choices=ACTION_STATUSES, attrs={'class': 'form-control'}))
    completed_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control', 'id': 'datepicker'}))
    details = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Details here'}))
    class Meta:
        model = IncidentAction
        fields = [
            'title',
            'status',
            'completed_time',
            'details'
        ]

    # def __init__(self, *args, **kwargs):
    #     super(ActionCreateForm,self).__init__(*args, **kwargs)
    #     self.fields['incident_id'] = forms.CharField()
       
        
