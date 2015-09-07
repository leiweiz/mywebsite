from django.conf.urls import patterns, include, url
from django.contrib import admin

import leiweiz.views

urlpatterns = patterns('',

    url(r'^mitbbs.html$', leiweiz.views.mitbbs),
)
