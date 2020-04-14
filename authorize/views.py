import os

from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from Bookrecommend import settings
from .models import user


def login(request):
    error_msg = ""
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        print(name, password)
        userEntry = user.objects.filter(name=name, password=password)
        if userEntry.exists():
            request.session['user'] = name
            request.session['userid'] = userEntry[0].id
            return HttpResponseRedirect('/')
        else:
            error_msg = '用户名或密码错误'
    return render(request, 'auth/login.html', {'error_msg': error_msg})


def open(request):
    return render(request, 'auth/open.html', locals())


def logout(request):
    del request.session['user']
    return HttpResponseRedirect('/login')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        try:
            userEntry = user(name=name, password=password, email=email)
            userEntry.save()
            return HttpResponseRedirect('/login')
        except Exception as e:
            return render(request, 'auth/register.html', locals())
    else:
        return render(request, 'auth/register.html', locals())

def notfound1(request):
    return render(request,'page/403.html',locals())


def notfound2(request):
    return render(request,'page/404.html',locals())


def notfound3(request):
    return render(request,'page/500.html',locals())


def userInfo(request):
    usr = request.session.get('user', None)
    uer=user.objects.get(name=usr)
    return render(request, 'page/user/userInfo.html', locals())

# # 改
# @csrf_exempt
# def update_user(request):
#     id = request.POST.get('id')
#     u_img = request.FILES['u_img']
#     fname = os.path.join(settings.MEDIA_ROOT, u_img.name)
#     with open(fname, 'wb') as pic:
#         for c in u_img.chunks():
#             pic.write(c)
#     u_img= os.path.join("img", u_img.name)
#     obj=user.objects.filter(id=id).update(u_img=u_img)
#     result = -1
#     if obj:
#         result = 0
#     return JsonResponse({"result": result})

def changePwd(request):
    usr = request.session.get('user', None)
    uer = user.objects.get(name=usr)
    return render(request, 'page/user/changePwd.html',locals())
#  更新数据
@csrf_exempt
def update_user(request):
    id = request.POST.get('id')
    passwordd = request.POST.get('password')
    obj = user.objects.filter(id=id).update(password=passwordd)
    result = -1
    if obj:
        result = 0
    return JsonResponse({"result": result})

def systemParameter(request):
    return render(request,'page/systemParameter/systemParameter.html',locals())