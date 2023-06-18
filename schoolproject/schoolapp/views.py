from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request,"home.html")
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid")
    return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exist")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,password=password,email=email)
                user.save();
                return redirect('login')

        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
def newpage(request):
    return render(request,"new_page.html")
def form(request):
    return render(request,"form.html")
def onclick(request):
    return render(request,"onclick.html")







