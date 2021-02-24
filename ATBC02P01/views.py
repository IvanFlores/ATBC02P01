import logging
from django.conf import settings
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

from ATBC02P01.settings import BASE_DIR

'''def index(request):
    now = datetime.datetime.now()
    html = "<html><body><h1>Here comes our Django Apps:</h1><p><a href='/admin'>Admin</a></p>" \
           "<p><a href='/endpoints'>End Points</a></p>It is now %s.</body></html>" % now
    return HttpResponse(html)
'''
logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'main.html', {})
