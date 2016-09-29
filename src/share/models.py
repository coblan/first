# -*- encoding:utf8 -*-

from django.db import models
from django.contrib.auth.models import User
from bs4 import BeautifulSoup
# Create your models here.

class DirModel(models.Model):
    name = models.CharField('名字',max_length=100,blank=True)
    #p_dir=models.CharField('父文件夹',max_length=600,blank=True)
    p_dir=models.ForeignKey('DirModel',verbose_name='父文件夹',blank=True,null=True)
    owner=models.ForeignKey(User, verbose_name=u'owner', blank=True, null=True)
    
    def todict(self):
        return {'name':self.name,'id':self.id}
    def __unicode__(self):
        return self.name
    
class NoteModel(models.Model):
    name = models.CharField('名字',max_length=200,blank=True)
    content = models.TextField('内容',blank=True)
    p_dir = models.ForeignKey(DirModel,verbose_name='父文件夹',blank=True,null=True)
    owner=models.ForeignKey(User, verbose_name=u'owner', blank=True, null=True)
    
    def todict(self):
        return {'name':self.name,'content':self.content,'id':self.id}
    
    def save(self,*args,**kw):
        super(NoteModel,self).save(*args,**kw)
        if not hasattr(self,'searchcontent'):
            SearchContent.objects.create(ifile=self)
        soup = BeautifulSoup(self.content)
        self.searchcontent.content = soup.text
        self.searchcontent.save()
    


    def __unicode__(self):
        return self.name    

class SearchContent(models.Model):
    ifile = models.OneToOneField(NoteModel,verbose_name='article text')
    content=  models.TextField('内容',blank=True)
    