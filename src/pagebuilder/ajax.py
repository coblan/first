
from core.db_tools import to_dict,save_model
from models import PageModel,MobilePage
from core.db_tools import to_dict
import forms

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


def add_mobile_page():
    return to_dict(MobilePage())


def save(row):
    return save_model(row, forms.get_globle())