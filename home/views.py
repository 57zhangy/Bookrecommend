from django.contrib.auth.hashers import check_password, make_password
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
# Create your views here.

import importlib, sys

from django.views.decorators.csrf import csrf_exempt

importlib.reload(sys)
from Bookrecommend import settings
import uuid
import os
from django.shortcuts import render, HttpResponse
from authorize.models import user
from home.models import book, hits

import redis

pool = redis.ConnectionPool(host='192.168.43.50', port=6379)
redis_client = redis.Redis(connection_pool=pool)


def getRecommendBook(request):
    userid = request.GET.get('userid')
    recommendbook = redis_client.get(int(userid))
    booklist = str(recommendbook).split('|')
    bookset = []
    for bk in booklist[:-1]:
        bookid = bk.split(',')[1]
        bk_entry = book.objects.get(id=bookid)
        bookset.append(bk_entry)
    return render(request, 'home/recommend.html', locals())


def writeToLocal(filename, data):
    with open(os.path.join(settings.BASE_DIR, filename), 'a') as fp:
        fp.write(data + '\n')


def getBookInfo(request):
    id = request.GET.get('id')
    bk = book.objects.get(id=id)
    # 设置点击量
    username = request.session.get('user', None)
    currentuser = user.objects.get(name=username)
    # currentuser=request.user
    try:
        hit = hits.objects.get(userid=currentuser.id, bookid=id)
        hit.hitnum += 1
        hit.save()

    except:
        hit = hits()
        hit.bookid = id
        hit.hitnum = 1
        hit.userid = currentuser.id
        hit.save()
    data = str(currentuser.id) + ',' + str(id) + ',' + str(1)
    # writeToLocal('hits.txt',data)
    with open('./recommend/hit.txt', 'a') as fp:
        fp.write(data + '\n')

    return render(request, 'home/detail.html', locals())

def index(request):
    # book_list= book.objects.all()[:25]
    usr = request.session.get('user', None)
    uer = user.objects.get(name=usr)
    userid = request.session.get('userid', None)
    return render(request, 'index.html', locals())


def main(request):
    # book_list= book.objects.all()[:25]
    # usr = request.session.get('user', None)
    # userid = request.session.get('userid', None)
    book_num = book.objects.count()
    # book_num=gesh['book_nu']
    geshu = user.objects.aggregate(pepole_nu=Count('password'))
    pepole_num = geshu['pepole_nu']
    print(geshu)
    return render(request, 'page/main.html', locals())


def search(request):
    usr = request.session.get('user', None)
    userid = request.session.get('userid', None)
    rs = book.objects.all()
    p = Paginator(rs, 15)
    book_list = request.GET.get('book_list')
    try:
        book_list = p.page(book_list)
    except:
        book_list = p.page(1)
    q = request.GET.get('q')
    error_msg = ''
    print(q)
    if not q:
        error_msg = '请输入关键词'
        return render(request, 'home/search.html', {'error_msg': error_msg, 'book_list': book_list, 'userid': userid})
    post_list = book.objects.filter(Q(name__icontains=q) | Q(publish__icontains=q))
    # print(type(post_list))
    # print(post_list)
    return render(request, 'home/search1.html', {'error_msg': error_msg, 'post_list': post_list, 'userid': userid})


def manage(request):
    rs = book.objects.all()
    p = Paginator(rs, 20)
    book_list = request.GET.get('book_list')
    try:
        book_list = p.page(book_list)
    except:
        book_list = p.page(1)
    usr = request.session.get('user', None)
    userid = request.session.get('userid', None)
    return render(request, 'page/list/booklist.html', locals())


# 1.2.前往 add 页
def add_page(request):
    return render(request, 'page/list/addlist.html')


# 2.增
@csrf_exempt
def add_list(request):
    b_no = request.POST['no']
    b_name = request.POST['name']
    b_price = request.POST['price']
    b_url = request.POST['url']
    b_publish = request.POST['publish']
    b_rating = request.POST['rating']
    b_cover = request.FILES['cover']
    fname = os.path.join(settings.MEDIA_ROOT, b_cover.name)
    with open(fname, 'wb') as pic:
        for c in b_cover.chunks():
            pic.write(c)

    book_add = book()
    book_add.no = b_no
    book_add.name = b_name
    book_add.price = b_price
    book_add.url = b_url
    book_add.publish = b_publish
    book_add.rating = b_rating
    # 存访问路径到数据库
    book_add.cover = os.path.join("img", b_cover.name)
    book_add.save()

    return redirect('/page/manage')


# 删
def delete_booklist(request, book_id):
    book.objects.filter(id=book_id).delete()
    return redirect('/page/manage')

def getbook(request):
    id = request.GET.get('id')
    book1 = bookk.objects.get(id=id)
    username = request.session.get('user', None)
    currentuser = user.objects.get(name=username)
    # currentuser=request.user
    try:
        hit = hits.objects.get(userid=currentuser.id, bookid=id)
        hit.hitnum += 1
        hit.save()

    except:
        hit = hits()
        hit.bookid = id
        hit.hitnum = 1
        hit.userid = currentuser.id
        hit.save()
    data = str(currentuser.id) + ',' + str(id) + ',' + str(1)
    # writeToLocal('hits.txt',data)
    with open('./recommend/hit.txt', 'a') as fp:
        fp.write(data + '\n')

    return render(request,'page/list/updatelist.html',locals())
# 改
@csrf_exempt
def update_list(request):
    id = request.POST['id']
    b_price = request.POST['price']
    b_rating = request.POST['rating']
    b_cover = request.FILES['cover']
    fname = os.path.join(settings.MEDIA_ROOT, b_cover.name)
    with open(fname, 'wb') as pic:
        for c in b_cover.chunks():
            pic.write(c)
    b_cover= os.path.join("img", b_cover.name)
    book.objects.filter(id=id).update(price=b_price,cover=b_cover,rating=b_rating)
    return redirect('/page/manage')
