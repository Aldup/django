from django.shortcuts import render
from loginapp.forms import UserForm , UserprofileInfo
from django.contrib.auth.models import User

#
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, "loginapp/index.html")

@login_required
def special(request):
    return render(request, 'loginapp/special.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def register(request):
    registered = False

    if request.method == 'POST':
        form = UserForm(request.POST)
        profile_form = UserprofileInfo(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True

        else:
            print(form.errors, profile_form.errors)
    else:
        form = UserForm()
        profile_form = UserprofileInfo()

    return render(request,"loginapp/registration.html",{'form':form , 'profile_form':profile_form, 'registered':registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed")
            print(f"Username : {username} and password: {password}")
            return HttpResponse("invalid login details supplied")
    else:
        return render(request, 'loginapp/login.html',{})
