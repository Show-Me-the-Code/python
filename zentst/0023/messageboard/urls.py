from django.conf.urls import patterns, include, url
from messageboard import views
from django.views.generic import ListView
from messageboard.models import Message


urlpatterns = patterns('',
    url(r'^$', views.index, name = 'index'),
    url(r'^postmessage/$', views.postmessage, name = 'postmessage'),
)
