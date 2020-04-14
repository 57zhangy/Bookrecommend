from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from Bookrecommend.settings import WHITESITE
class AuthMiddleware(MiddlewareMixin):
    def process_request(self,request):
        if request.path_info in WHITESITE or str(request.path_info).startswith('/admin'):
            print (request.path_info)
        elif request.session.get('user',None):
            print (request.path_info)
        else:
            return HttpResponseRedirect('/open/')
