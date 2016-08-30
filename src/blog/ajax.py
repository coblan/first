from models import ArtComment,ArticleModel
from core.db_tools import to_dict,save_model
#from forms import CommentForm
import forms




def get_globe():
    return globals()

def save(row):
    return save_model(row, forms.get_globe())
    #return save_model(models, forms.get_globe())



def get_art_comment(art_pk):
    out=[]
    for comment in ArtComment.objects.filter(art_id=art_pk):
        out.append(to_dict(comment))
    return out


#def add_art_comment(models):
    #return model_form_save(CommentForm,models=models)
    #art=ArticleModel.objects.get(pk=art_pk)
    #form = CommentForm({'art':art,'nickname':nickname,'comment':comment})
    #if form.is_valid():
       
        #ArtComment.objects.create(form.cleaned_data)
    #else:
        #return {'errors':form.errors}
    
