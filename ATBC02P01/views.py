from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime


def index(request):
    now = datetime.datetime.now()
    html = "<html><body><h1>Here comes our Django Apps:</h1><p><a href='/admin'>Admin</a></p>" \
           "<p><a href='/endpoints'>End Points</a></p>It is now %s.</body></html>" % now
    return HttpResponse(html)
