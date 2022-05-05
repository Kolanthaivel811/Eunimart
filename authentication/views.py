import random
import http.client
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth

from .models import User


# Create your views here.

def home(request):
    return render(request, "authentication/index.html")


def signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        code = request.POST['code']
        phone = request.POST['phone']

        myuser = User.objects.create(fname=fname, lname=lname, code=code, phone=phone)
        myuser.save()
        return redirect('signin')

    return render(request, "authentication/signup.html")


def signin(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        phone = request.POST['phone']

        fname = User.objects.filter(fname=fname)
        phone = str(User.objects.filter(phone=phone))
        print(fname)
        user = authenticate(request, username=fname, password=phone)
        print(user)
        if user is not None:
            login(request, user)
            fname = fname
            return render(request, "authentication/home.html", {'fname': fname})

        else:

            messages.error(request, "Invalid Credentials")
            return redirect('signin')

    return render(request, "authentication/signin.html")


def home1(request):
    return render(request, "authentication/home.html")
