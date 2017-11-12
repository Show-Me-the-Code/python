from django.shortcuts import render
from .forms import CommentForm
from .models import Comment


# Create your views here.
def CommentFormView(request):
    comment_all = Comment.objects.all()
    new_comment = None
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.save()
    else:
        form = CommentForm()
    return render(request, 'comment/index.html',
                          {'comment_form': form,
                           'new_comment': new_comment,
                           'comments': comment_all})
