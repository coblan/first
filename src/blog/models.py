# -*- encoding:utf8 -*-

from django.db import models

class CatModel(models.Model):
    name=models.CharField(u'name',max_length=100,blank=True,unique=True)
    label=models.CharField(u'显示名字',max_length=100,blank=True)
    
    def __unicode__(self):
        return self.name+'_'+self.label

class Tag(models.Model):
    name=models.CharField(u'名称',max_length=100,blank=True,unique=True)
    label=models.CharField(u'标签',max_length=100,blank=True)
    category=models.ManyToManyField(CatModel,blank=True)
    
    def __unicode__(self):
        return self.name
    

class TagAble(models.Model):
    tag=models.ManyToManyField(Tag,blank=True)
    
    class Meta:
        abstract = True    

HTML_STATUS=(
    ('publish','publish'),
    ('draft','draft')
)
#CATEGORY=(
    #('common','common'),
    #('math','math'),
#)

SRC_TYPE=(
    ('html','html'),
    # ('rst','rst'),
    ('ck','ckEditor'),
)

class ArticleModel(TagAble):
    name=models.CharField(u'名称（url）',max_length=100,blank=True)
    type=models.CharField(u'类型',max_length=100,blank=True,choices=SRC_TYPE)
    src=models.TextField(u'源代码',blank=True)
    html=models.TextField(u'html代码',blank=True)
    title=models.CharField(u'标题',max_length=300,blank=True)
    category=models.ForeignKey(CatModel,verbose_name=u'分类',max_length=100,blank=True)
    statue=models.CharField(u'状态',max_length=100,blank=True,choices=HTML_STATUS)
    update_time=models.DateTimeField(u'更新日期',auto_now=True)
    #statue=models.CharField(u'状态',max_length=100,blank=True)

    def __unicode__(self):
        return self.title    


#class HtmlArt(TagAble):
    #name=models.CharField(u'名称',max_length=100,blank=True)
    #src=models.ForeignKey(SrcModel,verbose_name=u'源文件',blank=True,null=True)
    #title=models.CharField(u'标题',max_length=300,blank=True)
    #html=models.TextField(u'html代码',blank=True)
    ##tag=models.CharField(u'类型')
    #update_time=models.DateTimeField(u'更新日期',auto_now=True)
    #statue=models.CharField(u'状态',max_length=100,blank=True,choices=HTML_STATUS)
    #category=models.CharField(u'分类',max_length=100,blank=True,choices=CATEGORY)
    
    #def __unicode__(self):
        #return self.title

class ArtComment(models.Model):
    nickname=models.CharField(u'称呼',max_length=200,blank=True)
    art=models.ForeignKey(ArticleModel,verbose_name=u'文章',null=True,blank=True)
    comment=models.TextField(u'评论内容',blank=True)
    create_time=models.DateTimeField(u'创建时间',auto_now=True)


    
    