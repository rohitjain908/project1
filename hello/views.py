from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
  return HttpResponse("Hello!")

def rohit(request):
  return HttpResponse("Hello, Rohit!")

def atul(request):
  return HttpResponse("Happy Birthday Atul!")

def greet(request,name):
  return HttpResponse(f"Hello, {name.capitalize()}!")

def number_plus_five(request,num):
  return HttpResponse(f"The Magical number is {num+5}")



