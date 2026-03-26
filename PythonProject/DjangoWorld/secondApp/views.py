from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return render(request,'App_2/home.html')

def aboutpage(request):
    return render(request,'App_2/about.html')