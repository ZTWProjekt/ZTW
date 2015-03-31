from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^$', 'Filmland.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),

    # user auth urls
    url(r'^accounts/login/$', 'accounts.views.login'),
    url(r'^accounts/auth/$', 'accounts.views.auth_view'),
    url(r'^accounts/logout/$', 'accounts.views.logout'),
    url(r'^accounts/loggedin/$', 'accounts.views.loggedin'),
    url(r'^accounts/invalid/$', 'accounts.views.invalid_login'),
    url(r'^accounts/register/$', 'accounts.views.register_user'),
    url(r'^accounts/register_success/$', 'accounts.views.register_success'),

)
