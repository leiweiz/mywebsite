from django.conf.urls import patterns, include, url
from django.contrib import admin

import leiweiz.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webapps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^webcrawler/', include('leiweiz.urls')),
    url(r'^$', leiweiz.views.index),
)
