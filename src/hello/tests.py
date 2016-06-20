from django.test import TestCase
from core.db_tools import to_dict,from_dict
from share.models import DirModel
# Create your tests here.
class TestDb(TestCase):
    def setUp(self):
        root=DirModel.objects.create(name='hello')
        d1=DirModel.objects.create(name='d1',p_dir=root)
    
    def test_dict(self):
        out=[]
        for d in DirModel.objects.all():
            out.append(to_dict(d))
            print(to_dict(d))
        
        
        for j in out:
            print(from_dict(j,DirModel))
        
        
