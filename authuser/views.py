from django.shortcuts import render
from django.http import HttpResponse
from core.port import jsonpost
from django.core.urlresolvers import reverse
from ajax import get_globe
import json

def login(request):
    if request.method=='GET':
        next_url=request.GET.get('next')
        if not next_url:
            next_url='/'
        dc={
            'next':next_url,
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
        return render(request,'authuser/regist.html',context=dc)
    elif request.method=='POST':
        return jsonpost(request,get_globe()) 


def change_pswd(request):
    if request.method=='GET':
        dc={
            'login_url':reverse('login')
        }        
        return render(request,'authuser/changepswd.html',context=dc)
    elif request.method=='POST':
        #try:
        return jsonpost(request,get_globe())  
        #except UserWarning as e:
            #return HttpResponse(json.dumps({'status':'fail','msg':str(e)}),content_type="application/json")