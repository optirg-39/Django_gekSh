from django import forms
from django.core import validators

"""Create Custom Validators in Django forms"""
def start_with_r(value):
    if value[0]!='r':
        raise forms.ValidationError('First letter should be r')

class StudentRegistration(forms.Form):

    name = forms.CharField(validators=[start_with_r])
    email = forms.EmailField(validators=[start_with_r])



