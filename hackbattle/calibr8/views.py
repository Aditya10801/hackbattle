from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'calibr8/index.html')

def register(request):
    return render(request, 'calibr8/register.html')

def login(request):
    return render(request, 'calibr8/login.html')

@login_required
def logout(request):
    return redirect('index')

@login_required
def preferences(request):
    return render(request, 'calibr8/settings.html')

@login_required
def scheduling(request):
    return render(request, 'calibr8/timetable.html')