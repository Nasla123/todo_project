from .models import task
from django import forms

class ModelForm(forms.ModelForm):
    class Meta:
        model= task
        fields=['name','priority','date']

