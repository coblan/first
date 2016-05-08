from models import DirModel,NoteModel
from core.db_tools import to_dict,from_dict
import json
import logic

def get_globe():
    return globals()

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

def file_data_all(pk):
    file = NoteModel.objects.get(pk=pk)
    parents=logic.parents(file)
    sibling=logic.get_sibling(file)
    return {'file':to_dict(file),
            'parents':[to_dict(parent) for parent in parents[:-1]],
            'dir':to_dict(parents[-1]),
            'sibling':{'dirs':[to_dict(dir) for dir in sibling[0]],
                       'files':[to_dict(sib) for sib in sibling[1]]}
            }

def dir_data_all(pk):
    dir= DirModel.objects.get(pk=pk)
    return {
        'dir':to_dict(dir),
        'parents':[to_dict(p) for p in logic.parents(dir)],
        'child_dirs':[to_dict(child_dir) for child_dir in dir.dirmodel_set.all()],
        'child_files':[to_dict(child_file,exclude=['content']) for child_file in dir.notemodel_set.all()]
    }


def del_dirs(ids):
    DirModel.objects.filter(id__in=ids).delete()
    return {'status':'success'}

def del_files(ids):
    NoteModel.objects.filter(id__in=ids).delete()
    return {'status':'success'}
        