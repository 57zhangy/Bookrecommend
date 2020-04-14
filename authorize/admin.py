# from django.contrib import admin
#
# # Register your models here.
# from .models import book
# from .models import hits
#
#
# admin.site.register(book)
# admin.site.register(hits)
# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.

class user_admin(admin.ModelAdmin):
    fields = ('name','password','email')

admin.site.register(user,user_admin)