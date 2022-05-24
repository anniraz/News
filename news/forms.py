from django import forms
from .models import *


class AdminForm(forms.ModelForm):
    class Meta:
        model=News
        fields=['category','title','description','image','url','tags']


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    message = forms.CharField(max_length=1000) 


class SocialSidebarForm(forms.ModelForm):
    class Meta:
        model = SocialSidebar
        fields = '__all__'
        widgets = {
            'background': forms.TextInput(attrs={'type': 'color'}),
        }