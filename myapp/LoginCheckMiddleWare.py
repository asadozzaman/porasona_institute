from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class LoginCheckMiddleWare(MiddlewareMixin):

    def process_view(self,request,view_func,view_args,view_kwargs):
        modulename=view_func.__module__
        print(modulename)
        user=request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "myapp.HodViews":
                    pass
                elif modulename == "myapp.views" or modulename == "django.views.static":
                    pass
                elif modulename == "django.contrib.auth.views" or modulename =="django.contrib.admin.sites":
                    pass
                else:
                    return HttpResponseRedirect(reverse("myapp_url:admin_home"))
            elif user.user_type == "2":
                if modulename == "myapp.StaffViews" or modulename == "myapp.EditResultVIewClass":
                    pass
                elif modulename == "myapp.views" or modulename == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("myapp_url:staff_home"))
            elif user.user_type == "3":
                if modulename == "myapp.StudentViews" or modulename == "django.views.static":
                    pass
                elif modulename == "myapp.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("myapp_url:student_home"))
            else:
                return HttpResponseRedirect(reverse("myapp_url:show_login"))

        else:
            if request.path == reverse("myapp_url:show_login") or request.path == reverse("myapp_url:do_login") or modulename == "django.contrib.auth.views" or modulename =="django.contrib.admin.sites" or modulename=="myapp.views":
                pass
            else:
                return HttpResponseRedirect(reverse("myapp_url:show_login"))