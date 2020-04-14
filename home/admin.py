# from django.contrib import admin
#
# # Register your models here.
# from .models import book
# from .models import hits
#
# admin.site.register(book)
# admin.site.register(hits)
# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import *
# Register your models here.

class book_admin(admin.ModelAdmin):
    fields = ('name','price','cover',)
    list_display = ('id','name','price','cover',)
    list_per_page = 10
    search_fields = ['name',]

class hits_admin(admin.ModelAdmin):
    fields = ('userid','bookid','hitnum',)
    list_display = ('userid','bookid','hitnum',)
    list_per_page = 10


admin.site.register(book,book_admin)
admin.site.register(hits,hits_admin)
admin.site.site_header="图书推荐系统"
