from django import forms
from .models import Incident


class IncidentCreateForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = [
            'title',
            'venue',
            'functional_area',
            'code',
            'description',
        ]