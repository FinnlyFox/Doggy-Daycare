from django.urls import path, include
from . import views

# Define the app name
app_name = 'doggy_daycare'

urlpatterns = [
    # URL for the home page
    path('', views.home, name='home'),
    
    # URL  for displaying all bookings
    path('bookings/', views.all_bookings, name='bookings'),
    
    # URL for adding a new booking
    path('add_booking/', views.add_booking, name='add-booking'),
    
    # URL for updating a booking
    path('update_booking/<booking_id>', views.update_booking, name='update-booking'),
    
    # URL for deleting a booking
    path('delete_booking/<booking_id>', views.delete_booking, name='delete-booking'),
]
