from django.conf.urls import patterns, url
from guestbook import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    )
