from helpers.db.redis_utils import redis_conn
import json
from django.utils import timezone
import pickle
from helpers.ge.long_link import long_link

def get_globe():
    return globals()

def pub_msg(room,msg,user_name):
    key='talk_%s'%room
    msgs = redis_conn.get(key)
    if msgs:
        ls=pickle.loads(msgs)
    else:
        ls=[]
    now=timezone.now()
    if ls:
        delta = timezone.timedelta(minutes=3)
        early_limit = now-delta
        #early_limit=early_limit.strftime('%Y-%m-%d %H:%M:%S')
        ls=filter(lambda x : x.get('time') >early_limit,ls)
        
    #now=now.strftime('%Y-%m-%d %H:%M:%S')
    dc={
        'time':now,
        'content':msg,
        'name':user_name
    }
    ls.append(dc)
    redis_conn.set(key,pickle.dumps(ls))
    return {'status':'success'}

def get_msg(room,time_str,user_name,user_id,user_names):
    utc=timezone.UTC()
    crt = timezone.get_current_timezone() 
    utc_last=None
    if time_str:
        last=timezone.datetime.strptime(time_str,'%Y-%m-%d %H:%M:%S %f')
        last=last.replace(tzinfo=crt)
        utc_last=last.astimezone(utc)
    
    
    redis_conn.set('room__%s.user_id.%s'%(room,user_id),user_name,ex=60)
    redis_conn.sadd('room__%s.user_list'%room,user_id)
    
    dc=has_new_msg(room,utc_last,user_names)
    if not dc:
        dc={}
    if 'chats' not in dc:
        dc['chats']=[]
    else:
        for item in dc.get('chats'):
            item['time']=timezone.localtime(item['time']).strftime('%Y-%m-%d %H:%M:%S %f')        
    if 'user_names' not in dc:
        dc['user_names']=get_user_names(room)
    dc['status']='success'
    return dc

@long_link(span=30)
def has_new_msg(room,utc_last,org_user_names):
    key='talk_%s'%room
    msgs = redis_conn.get(key)
    ls=[]
    if msgs:
        ls=pickle.loads(msgs)
        if utc_last:
            ls=filter(lambda x:x.get('time')>utc_last,ls) 
    user_names=get_user_names(room)
    if ls:
        return {'chats':ls}
    if user_names != org_user_names:
        return {'user_names':user_names}


def get_user_names(room):
    
    user_ids = redis_conn.smembers('room__%s.user_list'%room)
    user_names=[]
    for user_id in user_ids:
        user_name=redis_conn.get('room__%s.user_id.%s'%(room,user_id))
        if user_name:
            user_names.append(user_name)
        else:
            redis_conn.srem('room__%s.user_list'%room,user_id)
    return sorted(user_names)

def set_name(room,user_id,user_name):
    redis_conn.set('room__%s.user_id.%s'%(room,user_id),user_name,ex=60)
    return {'status':"success"}
    
def hello():
    return {'name':'hello'}