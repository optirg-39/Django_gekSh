from django.shortcuts import render, HttpResponseRedirect
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create signup View.
def sign_up(request):
    if request.method == "POST":
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account created successfully')
            fm.save()
    else:
        fm = SignupForm()
    return render(request, 'enroll/sign_up.html', {'form': fm})

# Create login View.
def log_in(request):
    if not request.user.is_authenticated:

        if request.method=='POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user_permision = authenticate(username = uname, password= upass)

                if user_permision is not None:
                    login(request,user_permision)
                    messages.success(request,'Login Successfully !!!')
                    return HttpResponseRedirect('/user_profile/')
        else:
            fm = AuthenticationForm()
        return render(request,'enroll/log_in.html', {'form':fm})
    else:
        return HttpResponseRedirect('/user_profile/')

# Profile
def user_profile(request):
    if request.user.is_authenticated:
        return render(request,'enroll/profile.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/log_in/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/log_in/')

def change_password(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('/user_profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request,'enroll/change_password.html', {'form':fm})
    else:
        return HttpResponseRedirect('/user_profile/')