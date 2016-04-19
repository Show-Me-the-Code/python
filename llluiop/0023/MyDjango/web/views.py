from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import Person
from models import Message
import datetime

def current_time(request):
    now = datetime.datetime.now()

    html = "<html><body>It is now %s.</body></html>" % now

    return HttpResponse(html)


def add(request, a, b):
    c = int(a) + int(b)

    return HttpResponse(c)


def home(request):
    return render(request, 'index.html')

def person(request):
    name = 'person in table are:'
    for p in Person.objects.all():
        name += p.name

    return HttpResponse(name)

def board(request):
    messages = Message.objects.all()
    content = {'messages': messages}
    return render(request, 'board.html', content)


def postmessage(request):
    name = request.POST['name']
    text = request.POST['text']

    m = Message(name=name, text=text)
    m.save()

    return HttpResponseRedirect(reverse('board'))
