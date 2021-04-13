from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(label="Your name", label_suffix=" ", initial="Rishabh", required=False, disabled=True,
                           help_text=" Limit 70 characters")
