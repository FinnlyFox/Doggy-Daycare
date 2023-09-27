from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        # Specifies the User model as the target model
        model = User
        # Fields to include in the form
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        # Calling the parent class constructor
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        
        # styling the text boxes
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
