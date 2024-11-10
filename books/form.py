from django import forms
from .models import  hotel
from .models import travel


# Flight Booking Form

# Hotel Booking Form
class BookingForm(forms.ModelForm):
    class Meta:
        model = hotel  # Ensure 'hotel' model exists with the same fields
        fields = ['name', 'email', 'phone_number', 'destination', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        
        class BookingForm(forms.ModelForm):
         class Meta:
            model = travel # Ensure 'hotel' model exists with the same fields
            fields = ['name', 'email', 'phone_number', 'destination', 'date']
            widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
  
  
