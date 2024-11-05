from django.shortcuts import render ,redirect
from books.form import BookingForm
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

def fligth1(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()  # Save the booking to the database
            return redirect('wow')  # Redirect to a success page
    else:
        form = BookingForm()
    return render(request, 'book/fligth1.html', {'form': form})
  
