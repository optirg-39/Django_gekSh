from django import forms

class StudentRegistration(forms.Form):

    name = forms.CharField()
    email = forms.EmailField()
    password =forms.CharField( widget=forms.PasswordInput)

    """Cleaning And Validating specific Fields"""
    def clean_name(self):
        valname = self.cleaned_data.get('name')
        if len(valname)<4:
            raise forms.ValidationError("Enter length more or Equal to 4")
        return valname
