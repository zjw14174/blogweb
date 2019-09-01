from django.urls import path
from . import views

urlpatterns = [
    #访问blog/后引用views文件种的blog_list函数
    #path(r'',views.blog_list,name='index'),
    path(r'',views.blog_pages,name='index'),
    path(r'pages/<int:page_id>/', views.blog_pages, name='pages'),

    path(r'article/<int:article_id>/', views.blog_detail, name='detail'),
    #<int:...>表示将接收到的请求转换为int类型

    path(r'types/<int:type_id>/', views.blog_type_page_list, name='types'),
    path(r'types/<int:type_id>/<int:type_page_id>/', views.blog_type_page_list, name='type_pages'),

]