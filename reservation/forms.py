from .models import Reservation
from django import forms
from django.forms import DateInput, TimeInput,Select,Textarea,NumberInput


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('how_many_people','date','time','area','have_kids','note')
        widgets ={
        'how_many_people': NumberInput(attrs={
            'class': "form-control",
            'min':'1',
            'max':'25',
            'type':'number',
            'style': 'max-width: 300px;',
            'placeholder': 'Name',
            'id':'ReservationDate'
            }),
        'date': DateInput(attrs={
            'class': "form-control",
            'type':'date',
            'style': 'max-width: 300px;',
            'placeholder': 'Name',
            'id':'ReservationDate'
            }),
        'time': TimeInput(attrs={
            'class': "form-control", 
            'type':'time',
            'style': 'max-width: 300px; margin-bottom:15px',
            'placeholder': 'Email',
            }),
        'area': Select(attrs={
        'class': "form-control", 
        'type':'select',
        'style': 'max-width: 300px; margin-bottom:15px',
        'placeholder': 'Email',
        }),
        'note': Textarea(attrs={
        'class': "form-control", 
        'style': 'max-width: 300px; margin-bottom:15px',
        'placeholder': 'Please input if you are allergic to anything',
        }
        )        
        }
