import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from myapp.EmailBackEnd import EmailBackEnd


def showDemoPage(request):
    return render(request,"admin/demo.html")

def ShowLoginPage(request):
    return render(request,"admin/user/login.html")

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            return HttpResponseRedirect(reverse("myapp_url:admin_home"))
        else:
            messages.error(request,"Invaliv Login Details")
            return HttpResponseRedirect("/")

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        print(user)
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                return HttpResponseRedirect(reverse('myapp_url:admin_home'))
            elif user.user_type=="2":
                return HttpResponseRedirect(reverse("myapp_url:staff_home"))
            else:
                return HttpResponseRedirect(reverse("myapp_url:student_home"))
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")



def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email+"usertype"+request.user.user_type)
    else:
        return HttpResponse("Please Login First")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")