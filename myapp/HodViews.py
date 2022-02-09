from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from myapp.models import CustomUser, Staffs, Courses, Subjects, Students


def admin_home(request):
    return render(request,"admin/hod_template/dashboard/home_content.html")