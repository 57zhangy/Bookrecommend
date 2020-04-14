from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('main', views.main),
    url(r'^search/$', views.search, name='search'),
    path('manage', views.manage),
    url(r'^addpage/$', views.add_page, name='addpage'),  # 前往新增学生的网页
    url(r'^addlist/$', views.add_list, name='addlist'),
    url(r'^delete/(?P<book_id>[0-9]*)/$', views.delete_booklist),
    url(r'^updatelist/$', views.update_list,name='updatelist'),

]
