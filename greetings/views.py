from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def greeting(request):
    return HttpResponse("Hello Lord in my World")

def personal_greeting(request, a):
    b = a.capitalize()
    return HttpResponse(f"Hello {b} in my World")