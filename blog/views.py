from django.shortcuts import render,get_object_or_404
from .models import *
from django.core.paginator import *

# Create your views here.

types = BlogArticlesType.objects.all()

def blog_pages(request,page_id=1):
    blogs=BlogArticles.objects.all()
    paginator=Paginator(blogs,3)
    pages=paginator.page(page_id)
    context={
        'blogs':blogs,
        'types':types,
        'pages':pages,
    }
    return render(request,'blog/blog_page.html',context)


def blog_type_page_list(request,type_id,type_page_id=1):
    articles = BlogArticles.objects.filter(articletype=type_id)
    title=get_object_or_404(BlogArticlesType,id=type_id)

    #####分页
    paginator=Paginator(articles,3)
    pages=paginator.page(type_page_id)

    context={
        'articles':articles,
        'types':types,
        'title':title,
        'pages':pages,
        'article_type':type_id,
    }
    return render(request,'blog/type_page_list.html',context)

def blog_detail(request,article_id):
    #根据ID查询具体内容
    article = get_object_or_404(BlogArticles,id=article_id)
    context={
        'article':article,
        'publish':article.publish,
        'types':types,
    }

    return render(request,'blog/blog_detail.html',context)





#最主要的就解决如何减少分类栏的加载次数,因为每次都会执行一次后台查询
#现在:加载每个页面都要执行一次header.html文件
#想要:加载每个页面,只执行一次header.html文件,然后调用它就行了

#如果把导航栏放在header.html里面,导致每个引用它的文件必须存在types:types这个键值
#如果取消了,导致每个主体html文件必须都写一遍导航栏的div,更郁闷的是这个div包含在  <div id="wrap">这个里面.

'''
def blog_list(request):
    #查询所有数据存储到blogs变量中
    blogs=BlogArticles.objects.all()
    #有请求时返回blogs字典,并使用templates/blog/blog_list.html文件渲染
    #blog_list.html文件会继承base.html文件渲染

    #####分页
    #创建分页类,所有数据按照3个一页分页
    #paginator=Paginator(blogs,3)
    #获取传入参数的页面的数据
    #pages=paginator.page(page_index)

    context={
        'blogs':blogs,
        'types':types,
    #    'pages':pages,
    }
    return render(request,'blog/blog_list.html',context)

def blog_type_list(request,type_id):
    articles = BlogArticles.objects.filter(articletype=type_id)
    title=get_object_or_404(BlogArticlesType,id=type_id)

    #####分页
    paginator=Paginator(articles,3)
    pages=paginator.page(1)
    context={
        'articles':articles,
        'types':types,
        'title':title,
        'pages':pages,
    }
    return render(request,'blog/type_list.html',context)
'''