from django.shortcuts import render
from core.port import jsonpost
import ajax
import json
from forms import MobilePageForm
from core.db_tools import form_to_head,to_dict
from models import MobilePage
# Create your views here.
def build(request):
    return render(request,'builder.html')


def pagebuild(request):
    if request.method=='GET':
        return render(request,'pagebuilder.html')
    else:
        return jsonpost(request, ajax.get_globle())

def mobile_page(request):
    if request.method=='GET':
        context = {'heads':json.dumps(form_to_head( MobilePageForm()) ),
                   'pages':json.dumps([to_dict(x) for x in MobilePage.objects.all()])
                   }
        return render(request,'mbpage.html',context=context)
    else:
        return jsonpost(request, ajax.get_globle())    