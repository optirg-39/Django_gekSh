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
    keys = request.session.keys()
    items = request.session.items()
    age_= request.session.setdefault('age',25)

    return render(request,'student/getsession.html',{'keys':keys, 'items':items, 'age':age_})

def delsession(request):
    request.session.flush()
    return render(request,'student/delsession.html')