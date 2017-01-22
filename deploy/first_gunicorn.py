import multiprocessing
import os
bind = '127.0.0.1:10000'
workers = multiprocessing.cpu_count() * 2 + 1
backlog = 2048
#worker_class = "sync"
worker_class = 'gevent'
debug = True
proc_name = 'first'
pidfile = '/pypro/first/run/first.pid'
#logfile = '/pypro/mysite/log/debug.log'
accesslog='/pypro/first/log/first.log'
errorlog='/pypro/first/log/first_error.log'
loglevel = 'debug'
chdir = '/pypro/first/src'
timeout=60

#stdout_logfile='/pypro/mysite/log/mysite_std.log'
#stderr_logfile='/pypro/mysite/log/mysite_std.log'
#gunicorn -c gunicorn.py.ini wsgi:application