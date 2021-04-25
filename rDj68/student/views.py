from django.shortcuts import render

# Create your views here.
def setcookie(request):
    respons = render(request,'student/setcookie.html')
    respons.set_cookie('name', 'rishabh')
    return respons

def getcookie(request):
    # name = request.COOKIES['name']
    name = request.COOKIES.get('name','guest')
    return render(request,'student/getcookie.html',{'name':name})

def delcookie(request):
    respons = render(request,'student/delcookie.html')
    respons.delete_cookie('name')
    return respons