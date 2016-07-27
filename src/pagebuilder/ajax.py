from models import PageModel
from core.db_tools import to_dict

def get_globle():
    return globals()

def save_page(name,label,content):
    row,c = PageModel.objects.get_or_create(name=name)
    row.label=label
    row.content=content
    row.save()
    return {'status':'success'}

def get_page(name):
    try:
        row = PageModel.objects.get(name=name)
        return to_dict(row)
    except PageModel.DoesNotExit:
        return {}