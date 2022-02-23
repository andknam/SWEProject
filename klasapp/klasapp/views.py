from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'klasapp/home.html')

def about(request):
    return HttpResponse("<h1>This is the about page.</h1>")