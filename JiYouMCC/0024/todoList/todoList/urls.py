from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, redirect_to_login
from views import process, register

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'todoList.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^login/$',  login,
                           {'extra_context': {'next': '/'}}),
                       url(r'^logout/$', logout, {'next_page': '/'}),
                       url(r'^password_reset/$', password_reset,
                           {'post_reset_redirect': '/password_reset_done'}),
                       url(r'^password_reset_done/$', password_reset_done),
                       url(r'^redirect_to_login/$', redirect_to_login,
                           {'login_url': '/login'}),
                       url(r'^register/$', register),
                       url(r'^$', process),
                       )
