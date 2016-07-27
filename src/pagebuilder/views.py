from django.shortcuts import render
from core.port import jsonpost
import ajax

# Create your views here.
def build(request):
    return render(request,'builder.html')


def pagebuild(request):
    if request.method=='GET':
        return render(request,'pagebuilder.html')
    else:
        return jsonpost(request, ajax.get_globle())