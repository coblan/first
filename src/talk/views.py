from django.shortcuts import render
from helpers.db.redis_utils import redis_conn
from helpers.director.port import jsonpost
import ajax
# Create your views here.

def ajax_port(request):
    return jsonpost(request, ajax.get_globe())


def home(request):
    return render(request,'talk/home.html')

def talk_page(request,room):
    ctx={
        'room':room
    }
    return render(request,'talk/talk.html',context=ctx)
