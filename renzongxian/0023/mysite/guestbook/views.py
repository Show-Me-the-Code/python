from django.shortcuts import render
from guestbook.models import Messages
import datetime


def index(request):
    if request.method == 'POST':
        p = Messages(name=request.POST['name'], pub_date=datetime.datetime.now(), content=request.POST['content'])
        p.save()
    posted_messages = Messages.objects.order_by('-pub_date')
    context = {'posted_messages': posted_messages}
    return render(request, 'index.html', context)