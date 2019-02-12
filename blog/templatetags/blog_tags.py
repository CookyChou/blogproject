#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/7 10:24
# @Author  : bgzhou
from ..models import Post, Category
from django import template

register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_category():
    return Category.objects.all()


@register.simple_tag
def get_category_num(category):
    return Post.objects.filter(category=category).count()
