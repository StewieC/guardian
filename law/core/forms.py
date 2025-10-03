from django import forms
from .models import Incident, Case

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['title', 'description', 'location']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['title', 'description', 'category', 'incident_date']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'incident_date': forms.DateInput(attrs={'type': 'date'}),
        }