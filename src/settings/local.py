from base import *


#STATIC_ROOT= os.path.join(BASE_DIR,'static')
STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)
#STATICFILES_DIRS = (os.path.join(BASE_DIR,'pub_static'),)

ROUT_MEDIA=True


import os
if os.environ.get('TEST'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
        }
    }  
else:
    DATABASES = {
        'default': {
            'NAME': 'first',
            'ENGINE': 'django.db.backends.mysql',
            'USER': 'root',
            'PASSWORD': 'root',
            'HOST': '127.0.0.1', 
            'PORT': '3306',        
          },
        }


SITE_URL='localhost:8000'
PER_PAGE=10