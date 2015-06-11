from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

def current_time(request):
    #now = datetime.datetime.now()

    #html = "<html><body>It is now %s.</body></html>" % now

    return "html"
