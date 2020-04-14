from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('user/userInfo.html', views.userInfo),
    path('user/changePwd.html', views.changePwd),
    path('user/update_user', views.update_user),
    path('403.html', views.notfound1),
    path('404.html', views.notfound2),
    path('500.html', views.notfound3),
    path('systemParameter/systemParameter.html', views.systemParameter),
    # url(r'^updateuser/$', views.update_user, name='updateuser'),
]
