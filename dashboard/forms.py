from attr import field
from django import forms
from matplotlib import widgets
from . models import *

class Notesform(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title','description']
     