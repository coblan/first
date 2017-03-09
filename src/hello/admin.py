from django.contrib import admin
from models import Page
# Register your models here.
from django.core.urlresolvers import reverse
from helpers.director.model_admin.tabel import ModelTable,RowSearch,RowFilter,RowSort
from helpers.director.model_admin.render import model_page_dc,model_dc,TablePage,render_dc,FormPage
from helpers.director.model_admin.fields import ModelFields

import pages


menus=[{'name':'hello','label':'home','url':lambda: reverse('model_table',kwargs={'name':'page'}),'icon':'<i class="fa fa-home" aria-hidden="true"></i>'},]

render_dc['menu']=menus


class PageTable(ModelTable):
    model = Page

    include=['name','label','page_cls','status']

class PageTablePage(TablePage):
    tableCls=PageTable


class PageForm(ModelFields):
    class Meta:
        model=Page
        fields=['name','label','page_cls','status','text']
    
    def get_heads(self):
        heads=super(PageForm,self).get_heads()
        for head in list(heads):
            if head['name']=='page_cls':
                head['type']='sim_select'
                head['options']=[{'value':'FirstPage','label':'FirstPage'},
                                 {'value':'SecondPage','label':'SecondPage'}]
            if head['name']=='status':
                head['type']='sim_select'
                head['options']=[
                    {'value':'active','label':'Active'},
                    {'value':'deactive','label':'Deactive'}
                ]
                head['default']='deactive'
            if head['name']=='text':
                heads.remove(head)
                
        return heads
        
    

class PageFormPage(FormPage):
    fieldsCls=PageForm
    template='hello/page_form.html'


model_dc[Page]={'fields':PageForm}
model_page_dc['page']={'table':PageTablePage,'form':PageFormPage}

