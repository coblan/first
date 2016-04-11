from django.shortcuts import render
from django.http import HttpResponse
from core.port import jsonpost
from django.core.urlresolvers import reverse
from ajax import get_globe

def login(request):
    if request.method=='GET':
        next_url=request.GET.get('next')
        if not next_url:
            next_url='/'
        #if request.user.is_authenticated():
            #is_login='true'
        #else:
            #is_login='false'
        dc={
            'next':next_url,
            #'is_login':is_login,
            'regist_url':reverse('regist')
        }
        return render(request,'authuser/login.html',context=dc)
        #return render(request,'lintool/login.html',context=dc)
        
    elif request.method=='POST':
        return jsonpost(request,get_globe())
    
    
def regist_user(request):
    if request.method=='GET':
        dc={
            'login_url':reverse('login')
        }
        return render(request,'lintool/regist.html',context=dc)
    elif request.method=='POST':
        return json_proc(request) 