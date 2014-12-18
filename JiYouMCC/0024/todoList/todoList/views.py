from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from todoList.list.models import List, Status
from todoList.list.views import get_first_status, get_last_status, create_new_list, next_step_list,pre_step_list
import datetime


def process(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/?next=%s' % request.path)
    status_result = Status.objects.all()
    if request.method == "POST":
        if 'detail' in request.POST:
            create_new_list(request.user, request.POST.get('detail'))
        if 'next' in request.POST:
            next_step_list(request.POST.get('next'))
        if 'pre' in request.POST:
            pre_step_list(request.POST.get('pre'))
    list_result = []
    for item in status_result:
        list_result.append(List.objects.filter(user=request.user, status=item))
    return render_to_response("process.html",
                              {'user_name': request.user,
                               'status': status_result,
                               'lists': list_result,
                               'laststatus': get_last_status(),
                               'firststatus': get_first_status() }, context_instance=RequestContext(request))


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/redirect_to_login")
    else:
        form = UserCreationForm()
    return render_to_response("registration/register.html",
                              {'form': form, },
                              context_instance=RequestContext(request),)
