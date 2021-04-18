from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','password']
        labels = {'name':'Your Name'}
        error_messages = {'name':{'required':'Enter your name here'},
                          'email':{'required':'email is required'}}

        widgets ={'password':forms.PasswordInput}






