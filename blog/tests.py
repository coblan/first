from django.test import TestCase
from proc_src import rst_parse
from models import SrcModel,HtmlArt
class TT(TestCase):
    def setUp(self):
        pass
    
    def test_parser(self):
        print(rst_parse('*hello*'))
        
    def test_handler(self):
        a=SrcModel(src='*hello world*')
        a.save()
        