from django.contrib import admin
from .models import *
# Register your models here.

class BlogArticlesAdmin(admin.ModelAdmin):
    #列表显示的内容,分三类,标题,作者,发布时间
    list_display = ('title','author','publish','modifydate','articletype')
    #可能是过滤器
    list_filter = ('publish','author')
    #搜索依据选项
    search_fields = ('title','body')
    #不知道
    raw_id_fields = ('author',)
    #不知道
    date_hierarchy = 'publish'
    #未知,可能是排序
    ordering = ['publish','author']

class BlogArticlesTypeAdmin(admin.ModelAdmin):
    list_display = ('id','type')
    ordering = ['id']

#在admin默认页面导入表名,并使用上面的类进行修饰
admin.site.register(BlogArticles,BlogArticlesAdmin)
#按默认的方式导入表名,没有任何修饰
#admin.site.register(BlogArticles)

admin.site.register(BlogArticlesType,BlogArticlesTypeAdmin)