from django.shortcuts import render

def students_info(request):
    datas=Students.objests.all()
    return render(request,'')
# Create your views here.
