from django.db.models.signals import post_save
from models import SrcModel,HtmlArt
from proc_src import rst_parse

def after_src_model_save(sender,instance,**kw):
    if instance.type=='rst':
        html=rst_parse(instance.src)
    elif instance.type=='ck':
        html=instance.src
    else:
        html='not parser'
    ht,c=instance.htmlart_set.get_or_create()
    ht.html=html
    ht.name=instance.name
    ht.title=instance.title
    ht.category=instance.category
    ht.save()
    

post_save.connect(after_src_model_save, sender=SrcModel,dispatch_uid='src_proc')