# -*- encoding:utf8 -*-
from __future__ import unicode_literals
from os import path
from models import CatModel,ArticleModel,Tag
import json
from core.db_tools import get_or_none,form_to_head,to_dict
from django.core.paginator import Paginator
from django.http import Http404
from forms import CommentForm
from django.conf import settings
base_dir=path.dirname(__file__)

class CtxHead(object):
    def __init__(self,name=''):
        self.crt_cat=name  # CatModel; 索引页当前所属的分类
        self.custom_js=['/static/js/blog.pack.js?%s'%int(path.getmtime(path.join(
            base_dir,'static/js/blog.pack.js')))]        
        self.title=u'我的网络日志'
        self.tags='' # 显示中右侧导航栏中的标签        
    
    def build(self):
        self.menus = CatModel.objects.all()
        for menu in self.menus:
            if menu.name==self.crt_cat:
                self.tags = menu.tag_set.all()

    
class CtxIndex(CtxHead):
    def __init__(self,name='',page=1):  
        CtxHead.__init__(self,name)
        self.categorys='' # 所有的分类，用json来表示的字典
        self.page=page
        self.articles=''
 
    
    def get_dict(self):
        self.build()
        return self.__dict__
    
    def build(self):
        super(CtxIndex,self).build()
        self.build_index()
        
    def build_index(self):
        pages= ArticleModel.objects.filter(category__name=self.crt_cat,statue='publish').order_by('-update_time')
        self.pgnt = Paginator(pages,settings.INDEX_PER_PAGE)
        self.articles = self.pgnt.page(self.page)
        ls = list(self.pgnt.page_range)
        c=self.page
        l=len(ls)
        k=3
        a=-1
        while a < 1:
            a=c-k
            k-=1
        self.page_nums = ls[a-1:min(l,c+(5-k))]
        self.page_count= l
        self.last_num=self.page_nums[-1]
        #articles=[]
        #for art in ArticleModel.objects.filter(category=crt_cat,statue='publish'):
            #articles.append({'title':art.title,'content':art.html,'name':art.name})
        #self.articles = articles


class CtxPage(CtxHead):
    def __init__(self,page_name):
        page=get_or_none(ArticleModel,name=page_name)
        if not page:
            raise Http404("%s not found"%page_name)
        super(CtxPage,self).__init__(page.category.name)
        self.article=page
        self.custom_js.append('https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML')

    
    def get_dict(self):
        self.build()
        return self.__dict__
    
    def build(self):
        super(CtxPage,self).build()
        #self.build_head()
        self.build_comment()
        
        self.heads= json.dumps(form_to_head( CommentForm()))
        #self.build_crt_cat(category.name)
        
    
    def build_comment(self):
        self.comments= json.dumps([to_dict(comment) for comment in self.article.artcomment_set.all()])


class CtxTag(CtxIndex):
    def __init__(self,cat_name,tag_name):
        super(CtxTag,self).__init__(cat_name)
        self.name=tag_name
    
    
    def get_dict(self):
        super(CtxTag,self).build()
        self.build()
        return self.__dict__
    
    def build(self):
        tag=get_or_none(Tag,name=self.name)
        #articles=[]
        if tag:
            self.articles=tag.articlemodel_set.filter(statue='publish') 
                #articles.append({'title':art.title,'content':art.html,'name':art.name})
        #self.articles = articles
        