from django import forms
from .models import User

from django.forms import ModelForm

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','password']








