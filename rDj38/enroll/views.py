from django.shortcuts import render
from .forms import StudentRegistration
from django.http import HttpResponseRedirect

# Create your views here.
def thankyou(request):
    return render(request,"enroll/success.html",{'candidate': name})


def showformdata(request):
    if request.method=='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print("Post request")
            global name
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            print(f'Name is {name}')
            print(f'Email is {email}')
            print(f'Password is {password}')

            return HttpResponseRedirect('/reg/success')

    else:
        fm=StudentRegistration()
    return render(request,"enroll/userregistration.html",{'stud':fm})
