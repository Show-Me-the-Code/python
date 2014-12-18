from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout, redirect_to_login
from views import process, register

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^login/$',  login,
                           {'extra_context': {'next': '/'}}),
                       url(r'^logout/$', logout, {'next_page': '/'}),
                       url(r'^redirect_to_login/$', redirect_to_login,
                           {'login_url': '/login'}),
                       url(r'^register/$', register),
                       url(r'^$', process),
                       )
urlpatterns += staticfiles_urlpatterns()
