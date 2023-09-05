from django import forms
from .models import *
from datetimewidget.widgets import DateTimeWidget

class EventCreationForm(forms.ModelForm):
    
    class Meta:
        model = EventCreation
        fields = [
            'title',
            'type',
            'description',
            'location',
            'prefered_date_time',
            'time_alloted',
            'total_slots'
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'prefered_date_time': DateTimeWidget(attrs={'class': 'form-control'}),
            'time_alloted': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_slots': forms.NumberInput(attrs={'class': 'form-control'}),
        }
