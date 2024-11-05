from django import forms
from .models import fligth

class BookingForm(forms.ModelForm):
    class Meta:
        model = fligth
        fields = ['name', 'email', 'phone_number', 'destination', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
