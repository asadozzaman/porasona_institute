from django.shortcuts import render


def staff_home(request):
    return render(request,"admin/staff/dashboard/home_content.html")
