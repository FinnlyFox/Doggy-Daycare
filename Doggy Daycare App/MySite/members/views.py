from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from .forms import RegisterUserForm

# View function for user login
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticates the user using provided username and password
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # If authentication is successful, log the user in and redirect to home
            login(request, user)
            return redirect(reverse('doggy_daycare:home'))
        else:
            # If authentication fails, display an error message and redirect to the login page
            messages.success(request, "There was an error logging in, try again!")
            return redirect('login')
    else:
        # If it's not a POST request, render the login form
        return render(request, 'authenticate/login.html', {})

# View function for user logout
def logout_user(request):
    logout(request)
    
    # Display a success message upon successful logout and redirect to the home page
    messages.success(request, "You have been logged out successfully!")
    return redirect(reverse('doggy_daycare:home'))

# View function for user registration
def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            # If the registration form is valid, save the user's registration data
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            
            # Login the newly registered user
            user = authenticate(username=username, password=password)
            login(request, user)
            
            # Display a success message upon successful registration and redirect to home
            messages.success(request, "You have registered successfully!")
            return redirect(reverse('doggy_daycare:home'))
    else:
        form = RegisterUserForm()

    # Render the registration form template
    return render(request, 'authenticate/register_user.html', {
        'form': form,
    })
