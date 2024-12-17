from .models import Reservation
from django import forms
from django.forms import (
    DateInput,
    TimeInput,
    Select,
    Textarea,
    NumberInput,
    CheckboxInput,
    TextInput)


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = (
            'how_many_people',
            'date',
            'time',
            'area',
            'have_kids',
            'special_request',
            'note')
        widgets = {
            'how_many_people': NumberInput(attrs={
                'class': "form-control",
                'min': '1',
                'max': '25',
                'style': 'max-width: 300px;'
                }),
            'date': DateInput(attrs={
                'class': "form-control my-2",
                'type': 'date',
                'style': 'max-width: 300px;'
                }),
            'time': TimeInput(attrs={
                'class': "form-control",
                'type': 'time',
                'style': 'max-width: 300px; margin-bottom:15px',
                }),
            'area': Select(attrs={
                'class': "form-control my-2",
                'style': 'max-width: 300px;',
            }),
            'special_request': TextInput(attrs={
                'class': "form-control my-2",
                'style': 'max-width: 300px;',
                'placeholder': 'Your special request',
            }),
            'note': Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;;',
                'placeholder': 'Please input if you are allergic to anything',
            })}
