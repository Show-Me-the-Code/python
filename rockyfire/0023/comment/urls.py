from django.conf.urls import url
from .views import CommentFormView
urlpatterns = [
    url(r'^$',CommentFormView,name="comment_form"),
]