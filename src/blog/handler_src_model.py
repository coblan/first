from django.db.models.signals import pre_save
from models import ArticleModel
# from proc_src import rst_parse

def before_ArticleModel_save(sender,instance,**kw):
    # if instance.type=='rst':
        # html=rst_parse(instance.src)
    if instance.type=='ck':
        html=instance.src
    else:
        html='not parser'
    #ht,c=instance.htmlart_set.get_or_create()
    #ht.html=html
    #ht.name=instance.name
    #ht.title=instance.title
    #ht.category=instance.category
    instance.html=html
    #ht.save()
    

pre_save.connect(before_ArticleModel_save, sender=ArticleModel,dispatch_uid='src_proc')