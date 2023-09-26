from django import forms
from django.forms import ModelForm
from .models import Booking

# Define a form class
class BookingForm(ModelForm):
    class Meta:
        # Specify the model to which this form is related
        model = Booking
        
        # Define the fields to be included in the form
        fields = ('first_name', 'last_name', 'pet', 'date', 'number', 'email', 'description')
        
        # Customize the labels for form fields (empty strings here for no labels)
        labels = {
            'first_name': '',
            'last_name': '',
            'pet': '',
            'date': '',
            'number': '',
            'email': '',
            'description': '',
        }

        # Customize the widgets for form fields to specify attributes
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the owner\'s first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the owner\'s last name'}),
            'pet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the name of the pet'}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Enter the date of the booking (format: yyyy-mm-dd/00:00:00)'}),
            'number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the owner\'s phone number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter the owner\'s email address'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter a short description of what to do for the pet'}),
        }
