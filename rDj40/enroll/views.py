from django.shortcuts import render
from .forms import StudentRegistration
from django.http import HttpResponseRedirect

# Create your views here.



def showformdata(request):
    if request.method=='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print("Post request")
            print('All DATA', fm.cleaned_data)
            print('Name:', fm.cleaned_data['name'])
            print('Email:', fm.cleaned_data['email'])
            print('Password:', fm.cleaned_data['password'])

    else:
        fm=StudentRegistration()
    return render(request,"enroll/userregistration.html",{'stud':fm})
