from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def infos(request):
    nazwa = "Strona Główna"
    t = loader.get_template("infos/main.html")
    c={"nazwa": nazwa}
    return HttpResponse(t.render(c))

def me(request):
    t = loader.get_template("infos/me.html")
    return HttpResponse(t.render())

def contact(request):
    t = loader.get_template("infos/contact.html")
    return HttpResponse(t.render())
