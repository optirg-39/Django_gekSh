from django import forms

class StudentRegistration(forms.Form):

    name = forms.CharField()
    email = forms.EmailField()

    """Validation of complete Django form at once"""
    def clean(self):
        cleaned_data=super().clean()
        valname = self.cleaned_data['name']
        valemail = self.cleaned_data['email']
        if len(valname)<4: raise forms.ValidationError("Enter name length equal or more then 4")
        if len(valemail)<10: raise forms.ValidationError("Enter email length equal or more then 10")

