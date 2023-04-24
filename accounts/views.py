# https://gist.github.com/akshith6212/42cc32e6932e1d5df273de5387360bbf
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def logout(request):
    auth_logout(request)
    return redirect('/')

def login(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(username, password)
        print(user)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invalid username or Password')
            return redirect('login')
    else:
        return render(request,"accounts/login.html")

def register(request):
    if(request.method == 'POST'):
        email = request.POST['email']
        password = request.POST['pass']
        username = request.POST['username']
        print(email,password)
        
        if User.objects.filter(email=email).exists():
            print("User already Registered")
            messages.info(request,'email already registered')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            print("Username already taken")
            messages.info(request,'Username already taken')
            return redirect('register')
        else:
            user = User(username=username,email=email,password=password)
            user.set_password(password)
            user.save()
            print("User Created")
            return redirect('login')
    else:
        return render(request,"accounts/register.html")
