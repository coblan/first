# -*- encoding:utf8 -*-

from django.db import models

class Tag(models.Model):
    name=models.CharField(u'名称',max_length=100,blank=True)

class TagAble(models.Model):
    tag=models.ManyToManyField(Tag,blank=True)
    
    class Meta:
        abstract = True    

HTML_STATUS=(
    ('publish','publish'),
    ('draft','draft')
)
CATEGORY=(
    ('common','common'),
    ('math','math'),
)

SRC_TYPE=(
    ('rst','rst'),
    ('ck','ckEditor'),
)

class SrcModel(TagAble):
    name=models.CharField(u'名称',max_length=100,blank=True)
    type=models.CharField(u'类型',max_length=100,blank=True,choices=SRC_TYPE)
    src=models.TextField(u'源代码',blank=True)
    title=models.CharField(u'标题',max_length=300,blank=True)
    category=models.CharField(u'分类',max_length=100,blank=True,choices=CATEGORY)
    statue=models.CharField(u'状态',max_length=100,blank=True,choices=HTML_STATUS)
    
    update_time=models.DateTimeField(u'更新日期',auto_now=True)
    #statue=models.CharField(u'状态',max_length=100,blank=True)

    def __unicode__(self):
        return self.title    


class HtmlArt(TagAble):
    name=models.CharField(u'名称',max_length=100,blank=True)
    src=models.ForeignKey(SrcModel,verbose_name=u'源文件',blank=True,null=True)
    title=models.CharField(u'标题',max_length=300,blank=True)
    html=models.TextField(u'html代码',blank=True)
    #tag=models.CharField(u'类型')
    update_time=models.DateTimeField(u'更新日期',auto_now=True)
    statue=models.CharField(u'状态',max_length=100,blank=True,choices=HTML_STATUS)
    category=models.CharField(u'分类',max_length=100,blank=True,choices=CATEGORY)
    
    def __unicode__(self):
        return self.title



    
    