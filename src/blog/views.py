# -*- encoding:utf-8 -*-

from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from models import ArticleModel,CatModel,Tag
from django.conf import settings
from django.core.urlresolvers import reverse
import json
from core.port import jsonpost
from contexts import CtxIndex,CtxPage,CtxTag

from core.db_tools import get_or_none
from datetime import datetime
import os.path as path
import os
from ajax import get_globe


def article(request,name=''):
    if request.method=='GET':
        ctx_page=CtxPage(name)
        return render(request,'blog/content.html',context=ctx_page.get_dict()) 
    else:
        return jsonpost(request, get_globe())

def index(request,cat_name=''):
    if request.method=='GET':
        try:
            page = int(request.GET.get('page'))
        except Exception:
            page=1
        if not cat_name:
            cat_name=CatModel.objects.first().name
        ctx_index=CtxIndex(cat_name,page)
        #ctx_index.build()
        return render(request,'blog/index.html',context=ctx_index.get_dict())  
    elif request.method=='POST':
        return jsonpost(request, get_globe())
    


def upload_file(request,Add):
    """ ADD = image """
    if request.method == 'POST':
        callback=request.GET.get('CKEditorFuncNum')
        f= request.FILES['upload']
        
        file_dir= path.join(settings.MEDIA_ROOT,'userdata',request.user.username,Add)
        try:
            os.makedirs(file_dir)
        except os.error as e:
            print(e)
        file_name=datetime.now().strftime('%Y%m%d%H%M%S')+f.name
        file_path=path.join(file_dir,file_name)
        handle_uploaded_file(f,file_path)
        file_url='/media/userdata/{user}/image/{file_name}'.format(user=request.user.username,file_name=file_name)
        if callback:
            return HttpResponse("""
            <script type="text/javascript">
            window.parent.CKEDITOR.tools.callFunction({callback},'{img_url}')
            </script>
            """.format(callback=callback,img_url=file_url))
        else:
            dc={"uploaded": 1,
                "fileName": f.name,
                'url':file_url
            }
            return HttpResponse(json.dumps(dc),content_type="application/json")



def handle_uploaded_file(f,file_path):
    with open( file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

   
def tag_view(request,tagname):
    if request.method=='GET':
        ctx=CtxTag(request.GET.get('crt_cat'),tagname)
        return render(request,'blog/tag.html',context=ctx.get_dict())