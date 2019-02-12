# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-02-08 01:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0002_auto_20190208_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='姓名')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('url', models.URLField(verbose_name='个人网站链接')),
                ('text', models.TextField(verbose_name='评论')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post', verbose_name='文章')),
            ],
        ),
    ]