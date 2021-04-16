from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def showformdata(request):
    fm = StudentRegistration(request.POST)
    if fm.is_valid():
        print("Post request")
        print("Post request with ", request.POST['name'])
        print("Post request with ", request.POST['email'])
        print(fm.cleaned_data['name'])
        print(fm.cleaned_data['password'])

    else:
        fm=StudentRegistration()
    return render(request,"enroll/userregistration.html",{'stud':fm})
