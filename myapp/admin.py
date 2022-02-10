from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from myapp.models import CustomUser,SessionYearModel,Students


class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser,UserModel)

admin.site.register(SessionYearModel)

admin.site.register(Students)