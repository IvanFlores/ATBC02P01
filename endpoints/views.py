from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, endpoints world.")


def hello(request):
    return HttpResponse("Hello, you.")


def hello_name(request, name):
    return HttpResponse("Hello: " + name)
