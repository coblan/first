from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

#@login_required
def hello(request):
    #return HttpResponse('hello my world')
    return render(request,'hello/index.html',context={'hello':'fucking '})