# -*- encoding:utf-8 -*-

import sys
import os
sys.path.append('..')

os.environ["DJANGO_SETTINGS_MODULE"]= "first.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from django.contrib.auth.models import User
from share.models import NoteModel,DirModel

def func():
    coblan=User.objects.all()[0]
    for file in NoteModel.objects.all():
        file.owner=coblan
        file.save()
        print(file)
    
    for dir in DirModel.objects.all():
        dir.owner=coblan
        dir.save()
        print(dir)

if __name__=='__main__':
    func()
