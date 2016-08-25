from django import forms
from models import MobilePage

def get_globle():
    return globals()

class MobilePageForm(forms.ModelForm):
    class Meta:
        model=MobilePage
        exclude=[]