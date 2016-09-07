from core.db_tools import to_dict,model_to_head
from models import MobilePage
#from forms import MobilePageForm

class Table(object):
    def __init__(self,page=1,sort=[],filter={}):
        self.page=page
        self.sort=sort
        self.arg_filter=filter 
        
    @classmethod
    def parse_request(cls,request):
        kw = request.GET.dict()
        page = kw.pop('_page','1')
        sort = kw.pop('_sort','').split(',')
        sort=filter(lambda x: x!='',sort)
        arg_filter = kw
        return cls(page,sort,arg_filter)
    
    def get_heads(self):
        pass
    def get_sort(self):
        return self.sort
    def get_rows(self):
        pass
    def get_page(self):
        pass
    def get_options(self):
        pass
    
class ModelTable(Table):
    #form=''
    model=''
    sortable=[]
    include=[]
    def __init__(self,page=1,sort=[],filter={}):
        super(ModelTable,self).__init__(page,sort,filter)
        field_names = [x.name for x in self.model._meta.fields]
        self.arg_filter={}
        for k,v in filter.items():
            if k in field_names:
                self.arg_filter[k]=v
    
    def get_heads(self):
        heads = model_to_head(self.model,include=self.include)
        for head in heads:
            if head.get('name') in self.sortable:
                head['sortable'] = True 
        return heads
    
    def get_rows(self):
        query = self.out_filter(self.model.objects.all())
        query = self.inn_filter(query)
        return [to_dict(x) for x in query]   
    
    def inn_filter(self,query):
        return query
    
    def out_filter(self,query):
        return query.filter(**self.arg_filter).order_by(*self.sort)
       
    def get_options(self):
        query = self.inn_filter(self.model.objects.all())
        options=[]
        for name in self.sortable:
            tmp = []
            option =[]
            label = filter(lambda x :x.name == name,self.model._meta.fields)[0]._verbose_name,
            value = self.arg_filter.get(name,'')
            for x in query: # get rid of duplicated row
                if getattr(x,name) not in tmp:
                    tmp.append(getattr(x,name))
                    if value == getattr(x,name):
                        option.append({'label': '%s:%s'%(name,getattr(x,name)),'name':getattr(x,name)})
                    else:
                        option.append({'label': getattr(x,name),'name':getattr(x,name)})
            options.append({
                'name':name,
                'label':label,
                'value': value,
                'options':option,
            })
        return options    


class PageTable(ModelTable):
    #form=MobilePageForm
    model = MobilePage
    sortable=['name','label']
    include= ['name','label']
    def get_page(self):
        pass
    
    