from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
import json
from django.views.decorators.csrf import csrf_exempt
import os
import time
from core.port import jsonpost
import ajax
import time
# Create your views here.




#@login_required
def hello(request):
    if request.method=='GET':
        #return HttpResponse('hello my world')
        return render(request,'hello/index.html',context={'hello':'fucking '})
    else:
        
        return HttpResponse(json.dumps({'name':'dog'}),content_type='application/json')


def talk(request):
    if request.method=='GET':
        
        return render(request,'hello/talk.html',context={'site_url':settings.SITE_URL,'id':int(time.time()*1000)})
    else:
        return jsonpost(request, ajax.get_globe())
                
        #return HttpResponse('ok')


@csrf_exempt
def upload_image_demo(request):
    if request.method=='PUT':
        return render(request,'hello/update_image_demo.html')
    else:
        file=request.FILES.get('file')
        name = u'{time}_{name}'.format(time=str(int(time.time())),name=file.name)
        path =  os.path.join(settings.MEDIA_ROOT,'upload_image_demo',name)
        
        # rt = HttpResponse()
        
        with open(path,'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)
                # n+= len(chunk)
           
        url = '/media/upload_image_demo/%s'%name
        return HttpResponse(json.dumps({'url':url}),content_type="application/json")
        # rt.write(json.dumps({'url':url}),content_type="application/json")
        # content=json.dumps({'url':url})
        # rt.write(content)
        # rt['content_type']="application/json"
        # rt['Content-Length'] =len(content)
        # rt['Access-Control-Allow-Origin']='*'
        # # rt['Content-Length'] = 24321
        # rt['Content-Encoding']='Utf-8'
        # return rt
    
    

def test_download(request):
    # url = request.GET.get('url')
    # resolution = request.GET.get('resolution')
    # mt = re.search('([^/-]+)-?(\d+x\d+)?(.jpg)',url,re.I)
    # if resolution:
        # name = mt.group(1)+'-'+str(resolution)+mt.group(3)
    # else:
        # name = mt.group(1)+mt.group(3)
    # url = url[:mt.start(1)]+name
    # rt = requests.get(url)
    # if rt.status_code!=200:
        # name = mt.group(1)+mt.group(3)
        # url = url[:mt.start(1)]+name 
        # rt = requests.get(url)
    # rs = HttpResponse(rt.content)
    with open(r'd:/try/bigfile/user_uploaded.tar.gz') as f:
        rs = HttpResponse(f.read())
    rs['Content-type'] = 'application/octet-stream'  # 'text/plain'
    # rs['Content-type'] = 'image/jpeg'
    rs['Content-Disposition'] = 'attachment; filename="{name}"'.format(name=name)
    return rs    

def normal_try(request):
    return render(request,'hello/normal_try.html')