# -*- encoding:utf8 -*-

from django.db import models

class Tag(models.Model):
    name=models.CharField(u'名称',max_length=100,blank=True)

class TagAble(models.Model):
    tag=models.ManyToManyField(Tag)
    
    class Meta:
        abstract = True    

class SrcModel(TagAble):
    type=models.CharField(u'类型',max_length=100,blank=True)
    src=models.TextField(u'源代码',blank=True)
    update_time=models.DateTimeField(u'更新日期',auto_now=True)
    statue=models.CharField(u'状态',max_length=100,blank=True)
    
class HtmlArt(TagAble):
    HTML_STATUS=(
        ('publish','publish'),
        ('draft','draft')
    )
    src=models.ForeignKey(SrcModel,verbose_name=u'源文件',blank=True,null=True)
    title=models.CharField(u'标题',max_length=300,blank=True)
    html=models.TextField(u'html代码',blank=True)
    #tag=models.CharField(u'类型')
    update_time=models.DateTimeField(u'更新日期',auto_now=True)
    statue=models.CharField(u'状态',max_length=100,blank=True,choices=HTML_STATUS)



    
    