from django.http import HttpResponseRedirect
from django.template import Context
from django.shortcuts import render
from django.utils import timezone
from django.core.urlresolvers import reverse
from messageboard.models import Message
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def index(request):
    messages = Message.objects.all().order_by('-vote_date')
    context = {'messages' : messages,}
    return render(request, 'message/index.html', context)


def postmessage(request):
    postname = request.POST['name']
    postcontext = request.POST['context']
    if postname == '':
        return render(request, 'message/index.html', {'error_message' : 'You did not input your name',})
    elif postcontext == '':
        return render(request, 'message/index.html', {'error_message' : 'You did not input context',})
    else:
        m = Message(name = postname, context = postcontext, vote_date = timezone.now())
        m.save()
        return HttpResponseRedirect(reverse('index'))
        
