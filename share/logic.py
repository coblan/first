from models import NoteModel , DirModel


def get_sibling(entry):
    if entry.p_dir:
        return get_dir_child(entry.p_dir)
    else:
        return [],[]

def get_dir_child(dir):
    dir_child = dir.dirmodel_set.all()
    file_child= dir.notemodel_set.all()
    return dir_child,file_child

def parents(entry):
    """
         file or dir
    """    
    ls= [parent for parent in _parents(entry)]
    ls.reverse()
    return ls    

def _parents(entry):
    while True:
        if entry.p_dir:
            yield entry.p_dir
            entry=entry.p_dir
        else:
            break