from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm
from django.shortcuts import render_to_response, RequestContext
from django.contrib.auth.models import User
from todoList.list.models import List, Status
import datetime


def process(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/?next=%s' % request.path)
    status_result = Status.objects.all()
    last = ''
    if request.method == "GET":
        if not request.GET.get('detail', '') is '':
            l = List(
                user=request.user,
                createdate=datetime.datetime.now(),
                duedate=datetime.datetime.now(),
                status=status_result[0],
                detail=request.GET.get('detail', '')
            )
            l.save()
        if not request.GET.get('move', '') is '':
            l = List.objects.get(id=request.GET.get('move', ''))
            l.status=Status.objects.get(id=l.status.id+1)
            l.save()
    
    list_result = []
    for item in status_result:
        list_result.append(List.objects.filter(user=request.user, status=item))
        last=item
    return render_to_response("process.html",
                              {'user_name': str(request.user),
                               'status': status_result,
                               'lists': list_result,
                               'laststatus':last,})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/redirect_to_login")
    else:
        form = UserCreationForm()
    return render_to_response("registration/register.html", {
        'form': form, },
        context_instance=RequestContext(request))
