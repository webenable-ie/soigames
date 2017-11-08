from django import forms
from .models import Incident
from events.models import Venue
from configtables.models import FunctionalArea

INCIDENTS_CODES = (
        ('nn', 'None'),
        ('mr', 'Minor'),
        ('sr', 'Serious'),
        ('cr', 'Critical'),
    )

class IncidentCreateForm(forms.ModelForm):
        title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}))
        venue = forms.ModelChoiceField(queryset=Venue.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
        functional_area = forms.ModelChoiceField(queryset=FunctionalArea.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
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

