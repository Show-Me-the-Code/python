# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from models import Message


def guestbook(request):
    try:
        name = request.COOKIES["name"]
    except:
        name = u"这家伙连名字也没有"
    return render(request, 'guestbook.html', {'commits': selectTextMsg(), 'name': name})


def guesttalk(request):
    response = HttpResponseRedirect("/guest")
    if request.method == "GET":
        name = request.GET.get('name', '')
        commit = request.GET.get('commits', '')
        date = datetime.datetime.now()
        if len(name) > 0 and len(commit) > 0 and len(name) < 41 and len(commit) < 4096:
            response.set_cookie("name", name.encode('utf8'))
            insertTextMsg(name, date, commit)
    return response


def insertTextMsg(user, date, message):
    message = Message(name=user,
                      message=message,
                      date=date,)
    message.save()


def selectTextMsg():
    return Message.objects.all().order_by("-date")
