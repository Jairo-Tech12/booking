from django.contrib import admin
from .models import fligth,travel,hotel
from .models import message
# from .models import travel


class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'destination', 'email', 'phone_number', 'date')  # Display fields
    search_fields = ('name', 'destination', 'email')  # Searchable fields
    list_filter = ('name', )  # Filterable fields

  
admin.site.register(fligth, BookingAdmin)
admin.site.register(travel, BookingAdmin)
admin.site.register(hotel, BookingAdmin)


                 
class ContactAdmin(admin.ModelAdmin):
             list_display = ('name', 'phone', 'gender', 'message')
    
  
admin.site.register(message, ContactAdmin)




 