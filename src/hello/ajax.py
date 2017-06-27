# -*- encoding:utf8 -*-

import json
from ws4redis.publisher import RedisPublisher
from ws4redis.redis_store import RedisMessage

from helpers.director.db_tools import name_to_model
from .admin import LeaveMsgForm
from django.core.exceptions import ValidationError
import pages

def get_global():
    return globals()

def publish_msg(msg):
    redis_publisher = RedisPublisher(facility='talk', broadcast=True)
    message = RedisMessage(msg.encode('utf8'))
    redis_publisher.publish_message(message)    
    return {'status':'success'}


def notify_refresh_user(id,name):
    redis_publisher = RedisPublisher(facility='talk', broadcast=True)
    message = RedisMessage(json.dumps({'op':'notify_refresh_user','id':id,'name':name}))
    redis_publisher.publish_message(message)    
    return {'status':'success'}    

def page_heads(cls_name):
    PageCls=pages.get_globe().get(cls_name)
    if PageCls:
        page_obj =PageCls()
        return page_obj.get_heads()
    else:
        raise UserWarning,'not matched page class : %s'%cls_name

def save_msg(row):
    form_obj = LeaveMsgForm(row,nolimit=True)
    if form_obj.is_valid():
        form_obj.save_form()
        return {'status':'success'}
    else:
        return {'errors': dict(form_obj.errors) }
        

