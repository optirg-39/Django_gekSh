from django.shortcuts import render
from .forms import UserForm
from .models import User

# Create your views here.
def showformdata(request):
    if request.method=='POST':

        fm = UserForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()


    else:
        fm=UserForm()
    return render(request,"enroll/userregistration.html",{'stud':fm})
