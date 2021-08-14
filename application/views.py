from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def hai(request):
    return HttpResponse('This is our first fbv')

def hello(request):
    return HttpResponse('<h1><marquee>This is our second FBV</marquee></h1>')  

def pop(request):
    return HttpResponse('<h2>This is my first project of django</h2>')      
