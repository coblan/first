from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Page(models.Model):
    name=models.CharField('name',max_length=200,blank=True)
    label=models.CharField('label',max_length=300,blank=True)
    page_cls=models.CharField('page class',max_length=100,blank=True)
    text=models.TextField(verbose_name='content',blank=True)
    status=models.CharField('status',max_length=100,blank=True)