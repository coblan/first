# -*- encoding:utf8 -*-
from __future__ import unicode_literals
from os import path
from models import CatModel,ArticleModel
import json
from core.db_tools import get_or_none
from django.core.paginator import Paginator

base_dir=path.dirname(__file__)

class CtxHead(object):
    def __init__(self,name=''):
        self.crt_cat=name  # CatModel; 索引页当前所属的分类
    
    def build_head(self):
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
        self.custom_js=['/static/js/blog.pack.js?%s'%int(path.getmtime(path.join(
            base_dir,'static/js/blog.pack.js'))),
                        'https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML']        
        self.title=u'我的网络日志'
        self.tags='' # 显示中右侧导航栏中的标签
    
    def get_dict(self):
        self.build()
        return self.__dict__
    
    def build(self):
        self.build_head()
        self.build_index()
        
    def build_index(self):
        self.pgnt = Paginator(ArticleModel.objects.filter(category__name=self.crt_cat,statue='publish'),1)
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
    def __init__(self,name):
        super(CtxPage,self).__init__(name)
        self.name=name
        self.article='' # ArticleModel
        self.art_pk='' # @int ; ArticleModel.pk 
    
    def get_dict(self):
        self.build()
        return self.__dict__
    
    def build(self):
        self.build_head()
        self.build_page()
        #self.build_crt_cat(category.name)
        
    
    def build_page(self):
        page=get_or_none(ArticleModel,name=self.name)
        if page:
            self.article = page
            self.crt_cat = page.category.name
            #self.art_pk=page.pk
            #return page.category
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
        