import os
import sys
sys.path.append('..')
sys.path.append('../src')
os.environ['DJANGO_SETTINGS_MODULE'] = 'src.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from share.models import NoteModel

for note in NoteModel.objects.all():
    print(note)
    note.save()
    

