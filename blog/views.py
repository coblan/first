# -*- encoding:utf-8 -*-

from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from models import ArticleModel,CatModel,Tag
from django.conf import settings
from django.core.urlresolvers import reverse
import json
from core.port import jsonpost

from core.db_tools import get_or_none
import os.path as path
from ajax import get_globe
base_dir=path.dirname(__file__)


def article(request,name):
    if request.method=='GET':
        ctx_page=CtxPage()
        ctx_page.build(name)
        return render(request,'blog/content.html',context=ctx_page.__dict__) 
    else:
        return jsonpost(request, get_globe())

def index(request,cat_name=''):
    if request.method=='GET':
        ctx_index=CtxIndex()
        ctx_index.build( cat_name)
        return render(request,'blog/index.html',context=ctx_index.__dict__)  
    elif request.method=='POST':
        return jsonpost(request, get_globe())
    


def upload_file(request,Add):
    if request.method == 'POST':
        callback=request.GET.get('CKEditorFuncNum')
        f= request.FILES['upload']
        file_path= path.join(settings.MEDIA_ROOT,Add,f.name)
        handle_uploaded_file(f,file_path)
        file_url='/media/image/%s'%f.name
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

class CtxIndex(object):
    def __init__(self):   
        self.categorys='' # 所有的分类，用json来表示的字典
        self.crtCatName='' # CatModel; 索引页当前所属的分类
        self.articles=''
        self.custom_js=['/static/js/blog.pack.js?%s'%int(path.getmtime(path.join(
            base_dir,'static/js/blog.pack.js'))),
                        'https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML']        
        self.title=u'我的网络日志'
        self.tags='' # 显示中右侧导航栏中的标签
    
    def build(self,cat_name):
        self.build_head()
        crt_cat= self.build_crt_cat(cat_name)
        self.build_index(crt_cat)
        
    def build_head(self):
        cats=[{'name':cat.name,'label':cat.label} for cat in CatModel.objects.all()]
        self.categorys=json.dumps(cats)
    
    def build_crt_cat(self,cat_name):
        category=get_or_none(CatModel,name=cat_name)
        if not category:
            category=CatModel.objects.all()[0]
        self.crtCatName = category.name
        self.tags= category.tag_set.all()
        return category
    
    def build_index(self,crt_cat):
        articles=[]
        for art in ArticleModel.objects.filter(category=crt_cat,statue='publish'):
            articles.append({'title':art.title,'content':art.html,'name':art.name})
        self.articles = articles
        
        
 
class CtxPage(CtxIndex):
    def __init__(self):
        super(CtxPage,self).__init__()
        self.article='' # ArticleModel
        self.art_pk='' # @int ; ArticleModel.pk 
        
    def build(self,page_name):
        self.build_head()
        category = self.build_page(page_name)
        self.build_crt_cat(category.name)
        
    
    def build_page(self,page_name):
        page=get_or_none(ArticleModel,name=page_name)
        if page:
            self.article=page
            self.art_pk=page.pk
            return page.category
        else:
            raise UserWarning,'%s has not found'%name

class CtxTag(CtxIndex):
    def __init__(self,tag_name):
        super(CtxTag,self).__init__()
        self._tag_name=tag_name
    
    def build_index(self,*arg,**kw):
        tag=get_or_none(Tag,name=self._tag_name)
        articles=[]
        if tag:
            for art in tag.articlemodel_set.filter(statue='publish') :
                articles.append({'title':art.title,'content':art.html,'name':art.name})
        self.articles = articles
        
        
def tag_view(request,tagname):
    if request.method=='GET':
        ctx=CtxTag(tagname)
        ctx.build(request.GET.get('crtCatName'))
        return render(request,'blog/tag.html',context=ctx.__dict__)