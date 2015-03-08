from django.shortcuts import render
from todolist.models import List


def index(request):
    if request.method == 'POST':
        for key in request.POST.keys():
            if key == 'newtask' and request.POST.get('newtask'):
                p = List(task=request.POST['newtask'])
                p.save()
            elif key.startswith('delete'):
                delete_id = key[len('delete'):]
                p = List.objects.get(id=delete_id)
                p.delete()
    task_list = List.objects.all
    context = {'task_list': task_list}
    return render(request, 'index.html', context)

