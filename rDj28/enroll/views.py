from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def showformdata(request):
    fm=StudentRegistration(auto_id='some_%s', label_suffix=' ?', initial={'name':'rishabh'})
    return render(request,"enroll/userregistration.html",{'stud':fm})
