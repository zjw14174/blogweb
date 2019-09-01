from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField
# Create your models here.

#定义数据库关系

# 添加分类数据库
class BlogArticlesType(models.Model):
    type = models.CharField(max_length=50,verbose_name='分类')

    class Meta:
        verbose_name_plural='分类'
        verbose_name='分类'

    def __str__(self):
        return self.type

#添加文章数据库
class BlogArticles(models.Model):
    #标题
    title = models.CharField(max_length=300,verbose_name='标题')
    #作者
    #外键,多对一,一个作者可以有多篇文章,定义在多的一方.
    author = models.ForeignKey(User,related_name="blog_posts",on_delete=models.CASCADE,verbose_name='作者')
    #内容
    body = MDTextField(verbose_name='内容')
    #发表公布时间
    publish = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    #修改时间
    modifydate = models.DateTimeField(auto_now=True,verbose_name='修改时间')

    articletype = models.ForeignKey(BlogArticlesType,on_delete=models.CASCADE,verbose_name='分类',default=10)
    #按时间倒序排列,里面是元组,比忘记写逗号
    class Meta:
        ordering= ('-publish',)
        verbose_name='文章'
        verbose_name_plural='文章'

    #对应后台文章列表中的默认显示字段
    def __str__(self):
        return self.title

