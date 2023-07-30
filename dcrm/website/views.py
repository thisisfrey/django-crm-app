from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def home(request):
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in!")
            return redirect('home')
        else:
            messages.warning(request, "An error occured, please try again!")
    else:
        return render(request, 'home.html', {})


def logout_user(request):
    pass


"""
def login_user(request):
    pass
"""
