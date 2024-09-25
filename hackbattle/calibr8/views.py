from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'calibr8/index.html')

def register(request):
    return render(request, 'calibr8/register.html')

def login(request):
    return render(request, 'calibr8/login.html')

def preferences(request):
    return render(request, 'calibr8/settings.html')

def scheduling(request):
    return render(request, 'calibr8/timetable.html')