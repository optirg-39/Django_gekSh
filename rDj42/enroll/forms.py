from django import forms
from django.core import validators
class StudentRegistration(forms.Form):
    """Built-in Validators in Django"""
    name = forms.CharField(validators=[validators.MaxLengthValidator(9)])
    email = forms.EmailField(validators=[validators.MinLengthValidator(10)])



