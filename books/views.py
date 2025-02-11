from django.shortcuts import render ,redirect
from django.http import HttpResponse
from books.form import BookingForm
from books.form import  ContactForm

from django import forms

def index(request):
         return render(request, "book/index.html")
     
def services(request):
    return render( request,"book/services.html")  

def about (request):
    return render( request,"book/about.html") 

     
def contact(request):
     submitted = False
     if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True  # Flag to trigger the popup
            form = ContactForm()  # Reset form
     else:
        form = ContactForm()
     return render(request, 'book/contact.html', {'form': form, 'submitted': submitted})
    
    

def fligth(request):
    return render( request,"book/fligth.html")


def travel(request):
    return render( request,"book/travel.html")


def hotel(request):
    return render( request,"book/hotel.html")

def fligth1(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()  # Save the booking to the database
            return HttpResponse("Flight booked successfully!")  # You could also use redirect
        else:
            # Return the form with validation errors
            return render(request, 'book/fligth1.html', {'form': form})
    else:
        # Render the empty form on GET request
        form = BookingForm()
        return render(request, 'book/fligth1.html', {'form': form})

  
def travel1(request):
     if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()  # Save the booking to the database
            return HttpResponse("Flight booked successfully!")  # You could also use redirect
        else:
            # Return the form with validation errors
            return render(request, 'book/travel1.html', {'form': form})
     else:
        # Render the empty form on GET request
        form = BookingForm()
        return render(request, 'book/travel1.html', {'form': form})



def hotel1(request):
       if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()  # Save the booking to the database
            return HttpResponse("Flight booked successfully!")  # You could also use redirect
        else:
            # Return the form with validation errors
            return render(request, 'book/hotel1.html', {'form': form})
       else:
        # Render the empty form on GET request
        form = BookingForm()
        return render(request, 'book/hotel1.html', {'form': form})


def wow(request):
    return render( request,"book/wow.html")

def explore(request):
    return render( request,"book/explore.html")
