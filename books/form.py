from django import forms
from .models import  fligth
from .models import travel
from .models import hotel


# Flight Booking Form

# Hotel Booking Form
class BookingForm(forms.ModelForm):
    class Meta:
         model =   fligth
         fields = ['name', 'email', 'phone_number', 'destination', 'date']
         widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
      
class BookingForm(forms.ModelForm):
       class Meta:
         model =   travel
         fields = ['name', 'email', 'phone_number', 'destination', 'date']
         widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
      
class BookingForm(forms.ModelForm):
       class Meta:
         model =   hotel
         fields = ['name', 'email', 'phone_number', 'destination', 'date']
         widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        } 
      