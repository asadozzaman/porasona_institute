from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from myapp.models import CustomUser, Staffs, Courses, Subjects, Students


def admin_home(request):
    return render(request,"admin/hod_template/dashboard/home_content.html")

def add_staff(request):
    return render(request,"admin/hod_template/staff/add_staff_template.html")

def add_staff_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        address=request.POST.get("address")
        print(first_name)
        print(last_name)
        print(username)
        print(email)
        print(password)
        print(address)
        try:
            print('rrrrrrrrr')
            user=CustomUser.objects.create_user(username=username,password=password,email=email,last_name=last_name,first_name=first_name,user_type=2)
            print('ffffffffffffff')
            user.staffs.address=address
            print('yyyyyyyyyyyyy')
            user.save()
            print('mmmmmmmmmm')
            messages.success(request,"Successfully Added Staff")
            return HttpResponseRedirect(reverse("myapp_url:add_staff"))
        except:
            messages.error(request,"Failed to Add Staff")
            return HttpResponseRedirect(reverse("myapp_url:add_staff"))

def manage_staff(request):
    staffs=Staffs.objects.all()
    return render(request,"admin/hod_template/staff/manage_staff_template.html",{"staffs":staffs})

def edit_staff(request,staff_id):
    staff=Staffs.objects.get(admin=staff_id)
    return render(request,"admin/hod_template/staff/edit_staff_template.html",{"staff":staff,"id":staff_id})

def edit_staff_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        staff_id=request.POST.get("staff_id")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        username=request.POST.get("username")
        address=request.POST.get("address")

        try:
            user=CustomUser.objects.get(id=staff_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=username
            user.save()

            staff_model=Staffs.objects.get(admin=staff_id)
            staff_model.address=address
            staff_model.save()
            messages.success(request,"Successfully Edited Staff")
            return HttpResponseRedirect(reverse("myapp_url:edit_staff",kwargs={"staff_id":staff_id}))
        except:
            messages.error(request,"Failed to Edit Staff")
            return HttpResponseRedirect(reverse("myapp_url:edit_staff",kwargs={"staff_id":staff_id}))


def add_course(request):
    return render(request,"admin/hod_template/course/add_course_template.html")

def add_course_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        course=request.POST.get("course")
        try:
            course_model=Courses(course_name=course)
            course_model.save()
            messages.success(request,"Successfully Added Course")
            return HttpResponseRedirect(reverse("myapp_url:add_course"))
        except:
            messages.error(request,"Failed To Add Course")
            return HttpResponseRedirect(reverse("myapp_url:add_course"))

def manage_course(request):
    courses=Courses.objects.all()
    return render(request,"admin/hod_template/course/manage_course_template.html",{"courses":courses})


def edit_course(request,course_id):
    course=Courses.objects.get(id=course_id)
    return render(request,"admin/hod_template/course/edit_course_template.html",{"course":course,"id":course_id})

def edit_course_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        course_id=request.POST.get("course_id")
        course_name=request.POST.get("course")

        try:
            course=Courses.objects.get(id=course_id)
            print(Courses.course_name)
            course.course_name=course_name
            course.save()
            messages.success(request,"Successfully Edited Course")
            return HttpResponseRedirect(reverse("myapp_url:edit_course",kwargs={"course_id":course_id}))
        except:
            messages.error(request,"Failed to Edit Course")
            return HttpResponseRedirect(reverse("myapp_url:edit_course",kwargs={"course_id":course_id}))