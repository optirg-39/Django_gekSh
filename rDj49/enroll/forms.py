from django import forms
from .models import User

from django.forms import ModelForm

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','password']
        labels = {'name':'Your Name'}
        label_suffixs = {'name':''}
        error_messages = {'name':{'required':'Enter your name here', 'min_length':'Length should more then 12'},
                          'email':{'required':'email is required','max_length':'Length should be less then 10'}}

        widgets ={'password':forms.PasswordInput,
                  'name':forms.TextInput(attrs={'class':'myclass','placeholder':'Rishabh gupta name'})}






