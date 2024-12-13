from .models import Reservation
from django import forms
from django.forms import DateInput, TimeInput


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('date','time','table')
        widgets ={
        'date': DateInput(attrs={
            'class': "form-control",
            'type':'date',
            'style': 'max-width: 300px;',
            'placeholder': 'Name'
            }),
        'time': TimeInput(attrs={
            'class': "form-control", 
            'type':'time',
            'style': 'max-width: 300px; margin-bottom:15px',
            'placeholder': 'Email',
            })            
        }