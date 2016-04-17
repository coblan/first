# -*- encoding:utf-8 -*-

from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from models import HtmlArt
from django.conf import settings

from core.db_tools import get_or_none
import os.path as path

base_dir=path.dirname(__file__)
def index(request,category=''):
    dc={'category':category}
    articles=[]
    if category:
        for art in HtmlArt.objects.filter(category=category):
            articles.append({'title':art.title,'content':art.html,'name':art.name})
    dc['articles']=articles
    dc['custom_js']=['/static/js/blog.pack.js?%s'%int(path.getmtime(path.join(
                    base_dir,'static/js/blog.pack.js')))]
    return render(request,'blog/index.html',context=dc)


def art(request,name=''):
    if not name:
        redirect('/blog')
    page=get_or_none(HtmlArt,name=name)
    if page:
        dc={
            'art_content':page.html,
            'category':page.category
            }
        dc['custom_js']=['/static/js/blog.pack.js?%s'%int(path.getmtime(path.join(
            base_dir,'static/js/blog.pack.js')))]        
        return render(request,'blog/content.html',context=dc)
    else:
        return Http404()


def upload_file(request,Add):
    if request.method == 'POST':
        callback=request.GET.get('CKEditorFuncNum')
        f= request.FILES['upload']
        file_path= path.join(settings.MEDIA_ROOT,Add,f.name)
        handle_uploaded_file(f,file_path)
        file_url='/media/image/%s'%f.name
        return HttpResponse("""
        <script type="text/javascript">
        window.parent.CKEDITOR.tools.callFunction(%s,'%s')
        </script>
        """%(callback,file_url))

def handle_uploaded_file(f,file_path):
    with open( file_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)