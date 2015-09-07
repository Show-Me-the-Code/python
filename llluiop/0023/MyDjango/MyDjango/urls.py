"""MyDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from web.views import current_time
from web.views import add
from web.views import person
from web.views import home
from web.views import board
from web.views import postmessage

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/', current_time),
    url(r'^add/(\d+)/(\d+)', add),
    url(r'^home', home),
    url(r'^person', person),
    url(r'^board', board, name='board'),
    url(r'^postmessage/$', postmessage, name='postmessage')

]
