from django import forms
from .models import *

class todoForm(forms.ModelForm):
    class Meta:
        model = todo
        fields ='__all__'