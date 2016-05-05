from django.shortcuts import render
from django.http import HttpResponse
from models import NoteModel,DirModel
from django.conf import settings
import json
from django.contrib.auth.decorators import login_required


@login_required
def hello(request):
    d,c = DirModel.objects.get_or_create(name='/',owner=request.user)
    dc = get_files(d.id)
    ps = get_dirParents(d.id)
    dc = {
        'crt_dir':json.dumps(d.todict()),
        'ps':json.dumps(ps),
        'dirs':json.dumps(dc.get('dirs')),
        'files':json.dumps(dc.get('files')),
        #'OTHER_STATIC':settings.OTHER_STATIC
    }
    return render(request,'share/selfinfo.html',context=dc)

def jsonpost(request):
    """PORT
    """
    cmddc = json.loads(request.body)
    outdc = {}
    orderls = cmddc.pop('order',None)
    if orderls:
        for k in orderls:
            outdc[k]=globals()[k](**cmddc.pop(k))
    for k,kw in cmddc.items():
        outdc[k]=globals()[k](**kw)
    return HttpResponse(json.dumps(outdc), content_type="application/json")

def add_dir(name,pid=None):
    if pid is None:
        p = DirModel(name='/')
        p.save()
    else:
        p = DirModel.objects.get(id=pid)
    d = DirModel(name=name,p_dir=p)
    d.save()
    return {'name':d.name,'id':d.id}

def modify_dir(name,id):
    d = DirModel.objects.get(id=id)
    d.name=name
    d.save()
    return {'name':d.name,'id':d.id}

def add_file(name,content,pid):
    if pid is None:
        p = DirModel(name='/')
        p.save()
    else:
        p = DirModel.objects.get(id=pid)   
    f = NoteModel(name=name,content=content,p_dir=p)
    f.save()
    return {'name':f.name,'content':f.content,'id':f.id}

def modify_file(name,content,id):
    f = NoteModel.objects.get(id=id)
    f.name=name
    f.content=content
    f.save()
    return {'name':f.name,'content':f.content,'id':f.id}

def get_dirParents(id):
    ps=[]
    while True:
        d = DirModel.objects.get(id=id)
        p = d.p_dir
        if p is not None:
            ps.append({'id':p.id,'name':p.name})
            id=p.id
        else:
            ps.reverse()
            return ps
        
def get_files(did):
    dirs=[d.todict() for d in DirModel.objects.filter(p_dir__id=did)]
    
    files = [f.todict() for f in NoteModel.objects.filter(p_dir__id=did)]
    return {'dirs':dirs,'files':files}


def del_dirs(ids):
    DirModel.objects.filter(id__in=ids).delete()
    return {'status':'success'}

def del_files(ids):
    NoteModel.objects.filter(id__in=ids).delete()
    return {'status':'success'}
        