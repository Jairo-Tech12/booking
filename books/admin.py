from django.contrib import admin
from .models import fligth,travel,hotel
from .models import Explore
from .models import message
from django.utils.html import format_html
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

admin.site.register(Explore, )



class ExploreAdmin(admin.ModelAdmin):
    list_display = ('country', 'place_name', 'price', 'display_image')
    search_fields = ('country', 'place_name')
    list_filter = ('country',)

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="70" style="object-fit: cover; border-radius: 5px;" />', obj.image.url)
        return "No Image"

    display_image.short_description = "Image Preview"




 