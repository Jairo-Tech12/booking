from django.shortcuts import render ,redirect
from books.form import BookingForm
# from books.form import TravelBookingForm
# from books.form import HotelBookingForm
# Create your views here.
def index(request):
         return render(request, "book/index.html")
     
def services(request):
    return render( request,"book/services.html")  

def about(request):
    return render( request,"book/about.html") 
     
def contact(request):
    return render( request,"book/contact.html")

def fligth(request):
    return render( request,"book/fligth.html")


def travel(request):
    return render( request,"book/travel.html")


def hotel(request):
    return render( request,"book/hotel.html")


def fligth1(request):
      return render(request, 'book/fligth1.html')

  
def travel1(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()  # Save the booking to the database
            return redirect('wow')  # Redirect to a success page
    else:
        form = BookingForm()
    return render( request,"book/travel1.html")



def hotel1(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()  # Save the booking to the database
            return redirect('wow')  # Redirect to a success page
    else:BookingForm()
    return render( request,"book/hotel1.html")


def wow(request):
    return render( request,"book/wow.html")

def explore(request):
    return render( request,"book/explore.html")
