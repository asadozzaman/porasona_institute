from django.shortcuts import render


def student_home(request):
    return render(request,"admin/student/dashboard/home_content.html")
