from __future__ import unicode_literals

from django.db import models

# Create your models here.

class PageModel(models.Model):
    name = models.CharField('name',max_length=300,blank=True)
    label = models.CharField('label',max_length=400,blank=True)
    content = models.TextField(verbose_name='content',blank=True)
    
class MobilePage(models.Model):
    name = models.CharField('name',max_length=300,blank=True)
    label = models.CharField('label',max_length=400,blank=True)
    content=models.TextField(verbose_name='content',blank=True)
