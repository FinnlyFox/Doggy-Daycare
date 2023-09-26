from django.contrib import admin
from .models import Booking

# Register the Booking model with the admin site
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    # Customize the display columns in the admin list view
    list_display = ('first_name', 'last_name', 'pet', 'number', 'email', 'date')
    
    # Set the default ordering of records in the admin list view by the 'date' field
    ordering = ('date',)
    
    # Enable searching for records by 'first_name', 'last_name', and 'pet' fields
    search_fields = ('first_name', 'last_name', 'pet')
