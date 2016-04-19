# -*- encoding:utf-8 -*-

from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from models import ArticleModel,CatModel,Tag
from django.conf import settings
from django.core.urlresolvers import reverse
import json

from core.db_tools import get_or_none
import os.path as path

base_dir=path.dirname(__file__)



def content(request,cat_name='',page_name=''):
    #cats=[{'name':cat.name,'label':cat.label} for cat in CatModel.objects.all()]
    #dc={'categorys': json.dumps(cats)}
    #category=get_or_none(CatModel,name=cat_name)
    #if not category:
        #category=CatModel.objects.all()[0]
    #dc['crt_cat']=category
    #articles=[]
    category,dc=build_categrory(cat_name)
    dc['tags']=category.tag_set.all()
    if not page_name:
        return build_index(request,category,dc)
    else:
        return build_page(request,dc,page_name)
    

def build_categrory(cat_name):
    cats=[{'name':cat.name,'label':cat.label} for cat in CatModel.objects.all()]
    dc={
        'categorys': json.dumps(cats),
        }
    
    category=get_or_none(CatModel,name=cat_name)
    if not category:
        category=CatModel.objects.all()[0]
    dc['crt_cat']=category
    return category,dc 

def build_index(request,category,dc):
    articles=[]
    for art in ArticleModel.objects.filter(category=category):
        articles.append({'title':art.title,'content':art.html,'name':art.name})
    dc['articles']=articles
    dc['custom_js']=['/static/js/blog.pack.js?%s'%int(path.getmtime(path.join(
        base_dir,'static/js/blog.pack.js')))]
    return render(request,'blog/index.html',context=dc)    

def build_page(request,dc,name):
    page=get_or_none(ArticleModel,name=name)
    if page:
        dc['article']=page
        dc['custom_js']=['/static/js/blog.pack.js?%s'%int(path.getmtime(path.join(
            base_dir,'static/js/blog.pack.js')))]        
        return render(request,'blog/content.html',context=dc)
    else:
        return Http404()

def art(request,name=''):
    if not name:
        redirect('/blog')
    page=get_or_none(ArticleModel,name=name)
    if page:
        dc={
            'article':page,
            'category':page.category,
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