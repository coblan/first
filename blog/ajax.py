from models import ArtComment,ArticleModel
from core.db_tools import to_dict
def get_globe():
    return globals()

def get_art_comment(art_pk):
    out=[]
    for comment in ArtComment.objects.filter(art_id=art_pk):
        out.append(to_dict(comment))
    return {'comments':out}

def add_art_comment(art_pk,nickname,comment):
    art=ArticleModel.objects.get(pk=art_pk)
    ArtComment.objects.create(art=art,nickname=nickname,comment=comment)
    
