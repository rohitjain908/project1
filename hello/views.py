from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request,"hello/index.html")

def rohit(request):
  return HttpResponse("Hello, Rohit!")

def atul(request):
  return HttpResponse("Happy Birthday Atul!")

def greet(request,name):
  return render(request,"hello/greet.html",{"name":name.capitalize()})

def number_plus_five(request,num):
  return HttpResponse(f"The Magical number is {num+5}")



