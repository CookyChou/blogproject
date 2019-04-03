#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/8 10:48
# @Author  : bgzhou

from django.conf.urls import url
from . import views

app_name = 'comments'
urlpatterns = [
    url('^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='comments'),
]