from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.

def signup(request):

    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check Username
          if User.objects.filter(username=username).exists():
              messages.error(request, 'Username already exists!')
              return redirect('/signup')
          else:
            if User.objects.filter(email=email).exists():
              messages.error(request, 'That email is being used')
              return redirect('/signup')
            else:
                #looks good
                user = User.objects.create_user(username=username, password=password, email=email,first_name=first_name, last_name=last_name)
                user.save()
                return redirect('/')

        else:

            messages.error(request, 'Passwords do not match')
            return redirect('/signup')
    else:
        return render(request, 'register/signup.html')

       

def signin(request):

    if request.method == 'POST':

        username = request.POST.get('uname')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('pages/dashboard')

        else:

            messages.error(request, 'Invalid username or password')
            return redirect('/')
    else:
        
        return render(request, 'register/login.html')

def logout(request):

    auth.logout(request)
    return redirect('/')
