from django.shortcuts import render
from enroll.models import Student

# Create your views here.
def studentinfo(request):
    # stu=Student.objects.all()
    stu=Student.objects.get(pk=1)
    print('Moules_DATA',stu)
    return render(request,'enroll/studetails.html', {'stud':stu})

