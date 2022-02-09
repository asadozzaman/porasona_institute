"""student_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from myapp import views,HodViews


app_name = 'myapp_url'

urlpatterns = [
    path('',views.ShowLoginPage,name="show_login"),
    path('doLogin', views.doLogin, name="do_login"),
    path('get_user_details', views.GetUserDetails, name="get_user_details"),
    path('logout_user', views.logout_user),

    # hod views
    path('admin_home',HodViews.admin_home,name="admin_home"),

    path('add_staff',HodViews.add_staff,name="add_staff"),
    path('add_staff_save',HodViews.add_staff_save,name="add_staff_save"),
    path('manage_staff', HodViews.manage_staff,name="manage_staff"),
    path('edit_staff/<str:staff_id>', HodViews.edit_staff,name="edit_staff"),
    path('edit_staff_save', HodViews.edit_staff_save,name="edit_staff_save"),


]
