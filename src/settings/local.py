<<<<<<< HEAD
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

REDIS_HOST='127.0.0.1'
REDIS_PORT=6379
REDIS_DB=5
#WSGI_APPLICATION = 'wsgi.application'
=======
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
>>>>>>> bed9c449cb869d6caf8eff06ea7143c7f1aab9af
