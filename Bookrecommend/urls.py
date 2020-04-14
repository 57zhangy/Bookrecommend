"""Bookrecommend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
from django.contrib import admin
from django.conf.urls import url
from home.views import *
from authorize.views import *
from django.views.static import serve
from django.urls import path, include

from django.urls import path, re_path

from django.contrib import admin
from django.urls import path, include

# from apscheduler.scheduler import Scheduler
#
# from home.views import aaa

urlpatterns = [
    # path('admin/', admin.site.urls),
    # # path('home/', include('home.urls')),
    # # path('home/', include('authorize.urls')),
    #
    # url(r'^login/', login, name='login'),
    # url(r'^logout/', logout, name='logout'),
    # url(r'^register/', register, name='register'),
    url(r'^$', index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^open/', open, name='open'),
    url(r'^login/', login, name='login'),
    url(r'^logout/', logout, name='logout'),
    url(r'^register/', register, name='register'),
    path('page/', include('home.urls')),
    path('auth/', include('authorize.urls')),
    url(r'^getbookinfo$', getBookInfo, name='getbookinfo'),
    url(r'^getbook$', getbook, name='getbook'),
    url(r'^bookpush$', getRecommendBook, name='getrecommendbook'),
    # url(r'^upload$',importBookData,name='importBookData'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
