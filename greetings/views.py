# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def greeting(request):
    return HttpResponse("Hello Lord in my World!! :) ")

def personal_greeting(request, a):
    return HttpResponse(f"Hello {a.capitalize()} in my World!!! :) ")