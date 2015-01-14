from django.conf.urls import patterns, url
from todolist import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    )