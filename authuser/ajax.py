from django.contrib.auth.models import User
from django.contrib import auth 
from core.db_tools import get_or_none

def get_globe():
    return globals()


def logout(request):
    auth.logout(request)
    return {'status':'success'}


def do_login(name,password,request):
    user= auth.authenticate(username=name,password=password)
    if user: 
        if user.is_active:  
            auth.login(request, user)
            return {'status':'success'}
        else:
            raise UserWarning,'[do_login] user has been disabled'
    else:
        user=get_or_none(User,username=name)
        if user:
            raise UserWarning,'[do_login] user exist,but password not match'
        else:
            raise UserWarning,'[do_login] user not exist'
    raise UserWarning,'[do_login] user or password not match'  

def registe(username,password):
    try:
        User.objects.get(username=username)
        raise UserWarning,'[registe] username has exist'
    except User.DoesNotExist:
        user=User.objects.create_user(username=username,password=password)
        user.is_active=True
        user.save()
        return {'status':'success'}


def changepswd(user,pswd):
    user.set_password(pswd)
    user.save()
    return {'status':'success'}
    

