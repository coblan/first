from django.contrib.auth.models import User
from django.contrib import auth 
from core.db_tools import get_or_none

def get_globe():
    return globals()

def logout(request):
    auth.logout(request)
    return {'status':'success'}


def do_login(name,password,request):
    #if re.search('@',name):
        #try:
            #user = User.objects.get(email=name)
            #name = user.username
        #except User.DoesNotExist:
            #return {'status':'fail','msg':'email not exist'}
    user= auth.authenticate(username=name,password=password)
    if user: 
        if user.is_active:  
            auth.login(request, user)
            return {'status':'success'}
        else:
            return {'status':'fail','msg':'user has been disabled'}
    else:
        user=get_or_none(User,username=name)
        if user:
            return {'status':'fail','msg':'user exist,but password not match'}
        else:
            return {'status':'fail','msg':'user not exist'}
    #user = auth.authenticate(token=name)
    #if user and user.is_active:
        #auth.login(request, user)
        #return {'status':'success'}
    #else:
    return {'status':'fail','msg':'user or password not match'}  

def registe(username,password):
    try:
        User.objects.get(username=username)
        return {'status':'fail','msg':'username has exist'}
    except User.DoesNotExist:
        user=User.objects.create_user(username=username,password=password)
        user.is_active=True
        user.save()
        return {'status':'success'}