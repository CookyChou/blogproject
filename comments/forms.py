#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/8 10:29
# @Author  : bgzhou

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']
