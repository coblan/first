# -*-encoding:utf-8 -*-
"""
sync webcode with first

Usage:
    python sync_webcode.py
    
"""
import sys
import os
sys.path.append(r'D:\coblan\py2')
from heTools.sync_code import sync

#import wingdbstub

tp = ('port.py','db_tools.py')
def func(src,dst):
    if src.endswith('.pyc'):
        return False
    if src.endswith(tp):
        return True

dc={
    'dirs':[(ur'D:\coblan\webcode\core',ur'D:\coblan\web\first\src\core'),],
    'include_file':func,
    }

sync(dc)