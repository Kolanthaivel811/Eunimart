from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request,"authentication/signup.html")

def signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        code = request.POST['code']
        phone = request.POST['phone']


        myuser = User.objects.create_user(fname, code, phone)
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your account has been successfully created")

        return redirect('signin')

    return render(request, "authentication/signup.html")

def signin(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        phone = request.POST['phone']

        user = authenticate(fname=fname, phone=phone)
        if user is None:
           # print("hi")
            login(request, user)
            fname = user.fname
            return render(request, "authentication/home.html", {'fname': fname})

        else:

            messages.error(request, "Invalid Credentials")
            return redirect('signin')

    return render(request, "authentication/signin.html")