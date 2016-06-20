from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
# Create your views here.
from ws4redis.publisher import RedisPublisher
from ws4redis.redis_store import RedisMessage



#@login_required
def hello(request):
    #return HttpResponse('hello my world')
    return render(request,'hello/index.html',context={'hello':'fucking '})


def talk(request):
    if request.method=='GET':
        return render(request,'hello/talk.html',context={'site_url':settings.SITE_URL})
    else:
        msg=request.body
        redis_publisher = RedisPublisher(facility='talk', broadcast=True)
        message = RedisMessage(msg)
        # and somewhere else
        redis_publisher.publish_message(message)        
        return HttpResponse('ok')