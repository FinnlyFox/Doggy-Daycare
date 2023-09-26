from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm
from django.http import HttpResponseRedirect

# Define a view function for the home page
def home(request):
    return render(request, 'doggy_daycare/home.html', {})

# Define a view function to display a list of all bookings
def all_bookings(request):
    # Query the database to retrieve all Booking objects and order them by date
    booking_list = Booking.objects.all().order_by('date')
    return render(request, 'doggy_daycare/booking_list.html', {
        'booking_list': booking_list,
    })

# Define a view function to add a new booking
def add_booking(request):
    submitted = False
    if request.method == 'POST':
        # If the request method is POST, process the form data
        form = BookingForm(request.POST)
        if form.is_valid():
            # If the form is valid, save the booking and redirect to a success page
            form.save()
            return HttpResponseRedirect('/add_booking?submitted=True')
    else:
        # If the request method is not POST, display the booking form
        form = BookingForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'doggy_daycare/add_booking.html', {
        'form': form,
        'submitted': submitted,
    })

# Define a view function to update an existing booking
def update_booking(request, booking_id):
    # Retrieve the Booking object with the specified booking_id from the database
    booking = Booking.objects.get(pk=booking_id)
    # Create a form with the booking data so that we can see whats already there to be updated
    form = BookingForm(request.POST or None, instance=booking)
    if form.is_valid():
        # If the form is valid, save the updated booking and redirect to the bookings list
        form.save()
        return redirect('/bookings/')

    return render(request, 'doggy_daycare/update_booking.html', {
        'booking': booking,
        'form': form,
    })

# Define a view function to delete an existing booking
def delete_booking(request, booking_id):
    # Retrieve the Booking object with the specified booking_id from the database
    booking = Booking.objects.get(pk=booking_id)
    # Delete the booking
    booking.delete()
    # Redirect to the bookings list
    return redirect('/bookings/')
