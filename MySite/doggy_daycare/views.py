from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm
from django.http import HttpResponseRedirect

def home(request):
    """
    Render the home page.

    This view function renders the home page of the Doggy Daycare website.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: The rendered home page.
    :rtype: HttpResponse
    """
    return render(request, 'doggy_daycare/home.html', {})

def all_bookings(request):
    """
    Display a list of all bookings.

    This view function retrieves all Booking objects from the database and orders them by date.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: The rendered booking list page.
    :rtype: HttpResponse
    """
    # Query the database to retrieve all Booking objects and order them by date
    booking_list = Booking.objects.all().order_by('date')
    return render(request, 'doggy_daycare/booking_list.html', {
        'booking_list': booking_list,
    })

def add_booking(request):
    """
    Add a new booking.

    This view function allows users to submit a new booking using a form. If the form is valid, the booking is saved,
    and the user is redirected to a success page.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: The rendered booking form or a success page upon successful submission.
    :rtype: HttpResponse
    """
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

def update_booking(request, booking_id):
    """
    Update an existing booking.

    This view function allows users to update an existing booking. It retrieves the Booking object with the specified
    booking_id from the database and pre-fills a form with the existing data. If the form is valid, the updated booking
    is saved, and the user is redirected to the bookings list.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :param booking_id: The ID of the booking to be updated.
    :type booking_id: int
    :return: The rendered booking update form or a redirect to the booking list upon successful update.
    :rtype: HttpResponse
    """
    # Retrieve the Booking object with the specified booking_id from the database
    booking = Booking.objects.get(pk=booking_id)
    # Create a form with the booking data so that we can see what's already there to be updated
    form = BookingForm(request.POST or None, instance=booking)
    if form.is_valid():
        # If the form is valid, save the updated booking and redirect to the bookings list
        form.save()
        return redirect('/bookings/')

    return render(request, 'doggy_daycare/update_booking.html', {
        'booking': booking,
        'form': form,
    })

def delete_booking(request, booking_id):
    """
    Delete an existing booking.

    This view function allows users to delete an existing booking. It retrieves the Booking object with the specified
    booking_id from the database and deletes it. After deletion, the user is redirected to the bookings list.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :param booking_id: The ID of the booking to be deleted.
    :type booking_id: int
    :return: A redirect to the booking list after deletion.
    :rtype: HttpResponse
    """
    # Retrieve the Booking object with the specified booking_id from the database
    booking = Booking.objects.get(pk=booking_id)
    # Delete the booking
    booking.delete()
    # Redirect to the bookings list
    return redirect('/bookings/')
