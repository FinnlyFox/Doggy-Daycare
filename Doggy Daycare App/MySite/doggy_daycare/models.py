from django.db import models

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField('Owner First Name', max_length=50)
    last_name = models.CharField('Owner Last Name', max_length=50)
    pet = models.CharField('Pet Name', max_length=120)
    date = models.DateTimeField('Booking date')
    number = models.CharField('Phone Number', max_length=15)
    email = models.EmailField('Email Address')
    description = models.TextField(blank=True)


    # Define a string representation for instances of the model
    def __str__(self):
        return self.first_name + ' ' + self.last_name + ', ' + self.pet
