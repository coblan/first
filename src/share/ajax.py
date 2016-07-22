from models import DirModel,NoteModel
from core.db_tools import to_dict,from_dict
from django.db.models import Q
import json
import logic

from authuser.ajax import logout

def get_globe():
    return globals()

def add_dir(name,p_dir,user):
    p_dir=from_dict(p_dir)
    d = DirModel(name=name,p_dir=p_dir,owner=user)
    d.save()


def add_file(name,content,p_dir,user):
    p_dir=from_dict(p_dir) 
    f = NoteModel(name=name,content=content,p_dir=p_dir,owner=user)
    f.save()
    return {'file':to_dict(f)}

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
        'child_dirs':[to_dict(child_dir) for child_dir in dir.dirmodel_set.all().order_by('name')],
        'child_files':[to_dict(child_file) for child_file in dir.notemodel_set.all().order_by('name')]
    }

def update(ele):
    ele=from_dict(ele)
    ele.save()

def del_elements(ele_array):
    for ele in ele_array:
        ele_obj=from_dict(ele)
        ele_obj.delete()

def move(ele_array,p_dir):
    p_dir=from_dict(p_dir)
    for ele in ele_array:
        ele_obj=from_dict(ele)
        ele_obj.p_dir=p_dir
        ele_obj.save()


def search(keywords,user):
    dirs=[]
    for dir in DirModel.objects.filter(name__icontains=keywords,owner=user):
        dirs.append(to_dict(dir))
        
    files=[]
    for file in NoteModel.objects.filter(Q(searchcontent__content__icontains=keywords)|Q(name__icontains=keywords),owner=user):
        files.append(to_dict(file))
    return {'files':files,'dirs':dirs}


        