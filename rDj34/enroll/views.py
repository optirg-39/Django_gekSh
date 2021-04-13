from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def showformdata(request):
    """If we override initial at views we have to write it as dictionary with key value pare and in forms.py we just
    have to write initial and give the value in individual fields"""
    fm=StudentRegistration(initial={"name":"Somya"})
    return render(request,"enroll/userregistration.html",{'stud':fm})
