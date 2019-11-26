from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.

def signup(request):

    # User has info and wants to create an account.
    if request.method == 'POST':

        # If passwords match.
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Seeing if there is already a user with this username.
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username has already been taken.'})

            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], '', request.POST['password1'])
                auth.login(request, user)
                return redirect('home')

        else:
            return render(request, 'accounts/signup.html', {'error': 'Password do not match.'})


    # Else, it's a get request.
    # User wants to see the sign up page.
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    # User has info and wants to create an account.
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Username or password is incorrect.'})


    # Else, it's a get request.
    # User wants to see the login page.
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')