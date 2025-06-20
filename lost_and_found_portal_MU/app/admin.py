from django.contrib import admin
from .models import Items, UserModel, Backup
from django.contrib.admin.sites import AlreadyRegistered

# Register your models here.
admin.site.register(UserModel)
admin.site.register(Items)
admin.site.register(Backup)