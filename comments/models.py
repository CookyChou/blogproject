from django.db import models

# Create your models here.


class Comment(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    email = models.EmailField(verbose_name='邮箱')
    url = models.URLField(verbose_name='个人网站链接')
    text = models.TextField(verbose_name='评论')
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    post = models.ForeignKey('blog.Post', verbose_name='文章')

    def __str__(self):
        return self.text[:20]
