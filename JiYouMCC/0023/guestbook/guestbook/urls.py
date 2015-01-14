from django.conf.urls import patterns, include, url
from django.contrib import admin
from commits.views import guestbook, guesttalk

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^guest/', guestbook),
                       url(r'^guesttalk', guesttalk),
                       )
