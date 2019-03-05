from django.contrib import admin
from  . import models
# Register your models here.
admin.site.register(models.User)        #超级管理员的子用户组
admin.site.register(models.Store)