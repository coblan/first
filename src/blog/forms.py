from django import forms
from models import ArtComment

def get_globe():
    return globals()

class CommentForm(forms.ModelForm):
    class Meta:
        model=ArtComment
        exclude=['create_time']
        
