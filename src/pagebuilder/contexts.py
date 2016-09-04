from django.shortcuts import render,Http404
from core.db_tools import form_to_head,to_dict
from models import MobilePage
from forms import MobilePageForm
import json
from tables import PageTable

def get_cls(step):
    name = 'MB%s%s'%(step[0].capitalize(),step[1:].lower())
    return globals().get(name)

class Object(object):
    pass

class MBBase(object):
    abstract=True
    template=''
    def __init__(self):
        self.ctx=Object()
    
    def get_dict(self):
        return self.ctx.__dict__
    
    def get(self,request,step):
        self.step = step
        self.build(request)
        return render(request,self.template,context=self.get_dict())
    
    def build(self,request):
        self.ctx.menu_active = 'content'
        self.ctx.submenu_active=self.step

class MBPage(MBBase):
    template='mobile/mbpage.html'
    
    def build(self,request):
        MBBase.build(self,request)
        
        #self.ctx.heads = json.dumps(form_to_head( MobilePageForm())) 
        #self.ctx.pages = json.dumps([to_dict(x) for x in MobilePage.objects.all()] )
        
        table = PageTable.parse_request(request)
        self.ctx.heads=json.dumps(table.get_heads())
        self.ctx.pages = json.dumps(table.get_rows())
        self.ctx.filters = json.dumps(table.get_filters())

class MBMenu(MBBase):
    template = 'mobile/mbmenu.html'


class MBGroup(MBBase):
    template = 'mobile/mbgroup.html'
          
