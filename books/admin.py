from django.contrib import admin
from .models import fligth

class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'destination', 'email', 'phone_number', 'date')  # Display fields
    search_fields = ('name', 'destination', 'email')  # Searchable fields
    list_filter = ('destination', 'date')  # Filterable fields

# Register the model with the custom admin class
admin.site.register(fligth, BookingAdmin)
