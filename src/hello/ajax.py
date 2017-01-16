# -*- encoding:utf8 -*-

import json
from ws4redis.publisher import RedisPublisher
from ws4redis.redis_store import RedisMessage

def get_globe():
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