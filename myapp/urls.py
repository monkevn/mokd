# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^login/$', sign_in),
    url(r'^reg/$', sign_up),
    url(r'^logout/$', sign_out),
    url(r'^comment/$', comment),
    url(r'^members/$', members),
    url(r'^detail/(\d+)$', detail),
    url(r'^item/(\d+)$', item),
    url(r'^account/$', account),
    url(r'^article/(\d+)$', article),
    url(r'^guide/$', guide),
    url(r'^order/$', order),
    url(r'^scenic/$', scenic),
    url(r'^publish/$', publish),
    url(r'^search/$', search),
    url(r'^hotel/$', hotel),
]
