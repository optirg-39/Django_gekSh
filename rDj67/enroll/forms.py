from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


class SignupForm(UserCreationForm):
    password2 = forms.CharField(label='Conferm Password (again)', widget=forms.PasswordInput) #override
    class Meta:
        model=User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email':'Email'}

class EditProfileForm(UserChangeForm):
    password = None
    class Meta:
        model=User
        fields = ['username', 'first_name', 'last_name', 'email', 'last_login','date_joined']
        labels = {'email':'Email'}