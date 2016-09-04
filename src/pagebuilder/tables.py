from core.db_tools import to_dict,form_to_head
from models import MobilePage
from forms import MobilePageForm

class Table(object):
    def __init__(self,page=1,sort=[],filter={}):
        self.page=page
        self.sort=sort
        self.filter=filter   
    @classmethod
    def parse_request(cls,request):
        kw = request.GET.dict()
        page = kw.pop('_page','1')
        sort = kw.pop('_sort','').split(',')
        sort=filter(lambda x: x!='',sort)
        ifilter = kw
        return cls(page,sort,ifilter)
    
    def get_heads(self):
        pass
    def get_rows(self):
        pass
    def get_page(self):
        pass
    def get_filters(self):
        pass
    
    def add_filter_state(self,dc_ls):
        for dc in dc_ls:
            if dc.get('name') in self.filter:
                for option in dc.get('options',[]):
                    if option.get('name')==self.filter.get(dc.get('name')):
                        option['label']='%s:%s'%(dc.get('label'),option.get('label'))
                        dc['value']=option.get('name')
                        break

class ModelTable(Table):
    form=''
    model=''
    sortable=[]
    def __init__(self,page=1,sort=[],filter={}):
        super(ModelTable,self).__init__(page,sort,filter)
        field_names = [x.name for x in self.model._meta.fields]
        self.filter={}
        for k,v in filter.items():
            if k in field_names:
                self.filter[k]=v
    
    def get_heads(self):
        heads = form_to_head(self.form())
        for head in heads:
            if head.get('name') in self.sortable:
                head['sortable'] = True
                if head.get('name') in self.sort :
                    head['priority']=self.sort.index(head.get('name'))+1
                    self.order = ''
                if '-'+head.get('name') in self.sort:
                    head['priority'] = self. sort.index('-'+head.get('name'))+1
                    self.order ='-'
                
        return heads
    
    def get_rows(self):
        
        return [to_dict(x) for x in self.model.objects.filter(**self.filter).order_by(*self.sort)]    


class PageTable(ModelTable):
    form=MobilePageForm
    model = MobilePage
    sortable=['name']
    def get_page(self):
        pass
    
    def get_filters(self):
        
        filters= [
            {'name':'name',
             'label':'name',
             'value':'',
             'options':[{'label':x.name,'name':x.name} for x in MobilePage.objects.all()]
             },
            {'name':'label',
             'label':'label',
             'value':'',
             'options':[{'label':x.label,'name':x.label} for x in MobilePage.objects.all()]
             }            
           
        ]
        self.add_filter_state(filters)
        return filters
    
    

                        
            
    
    
    