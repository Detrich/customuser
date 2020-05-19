from django.contrib import admin
from customuser.models import Myuser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
admin.site.register(Myuser, UserAdmin)