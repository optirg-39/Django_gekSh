from django import forms

class StudentRegistration(forms.Form):

    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    repassword = forms.CharField(label='Re-Password',widget=forms.PasswordInput)

    def clean(self):
        cleaned_data=super().clean()
        valpaw=self.cleaned_data['password']
        valrpaw=self.cleaned_data['repassword']

        if valpaw!=valrpaw:
            raise forms.ValidationError("Password not matched")





