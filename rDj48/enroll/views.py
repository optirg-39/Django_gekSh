from django.shortcuts import render
from .forms import UserForm

# Create your views here.
def showformdata(request):
    if request.method=='POST':
        fm = UserForm(request.POST)
        if fm.is_valid():
            print('Name:', fm.cleaned_data['name'])
            print('Email:', fm.cleaned_data['email'])
            print('Password:', fm.cleaned_data['password'])

    else:
        fm=UserForm()
    return render(request,"enroll/userregistration.html",{'stud':fm})
