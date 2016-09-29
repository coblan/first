from django.shortcuts import render

def index(request):
    return render(request,'tmp_index.html')