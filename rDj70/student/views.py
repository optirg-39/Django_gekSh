from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name']='Rishabh'
    request.session['lname']='Gupta'
    return render(request,'student/setsession.html')

def getsession(request):
    # response = request.session['name']
    response = request.session.get('name',"GUEST")
    l_response = request.session.get('lname')
    return render(request,'student/getsession.html',{'name':response,'lname':l_response})

def delsession(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request,'student/delsession.html')