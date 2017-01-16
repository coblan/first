from base import *

DEBUG=True
ALLOWED_HOSTS=['enjoyst.com','www.enjoyst.com','115.29.99.226']

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
    ('coblan', 'coblan@163.com'),
)

MANAGERS = (
    ('coblan', 'coblan@163.com'),
)

EMAIL_HOST='smtp.163.com'
EMAIL_HOST_PASSWORD='he7125158'
EMAIL_HOST_USER='coblan'
EMAIL_SUBJECT_PREFIX='[FIRST]'
SERVER_EMAIL='coblan@163.com'
DEFAULT_FROM_EMAIL='coblan@163.com'


DATABASES = {
    'default': {
        'NAME': 'first',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': 'he123811',
        'HOST': '127.0.0.1', 
        'PORT': '3306',        
      },
    }

SITE_URL='enjoyst.com'


REDIS_HOST='127.0.0.1'
REDIS_PORT=6379
REDIS_DB=5