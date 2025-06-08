from django.contrib import admin
from .models import Items
from django.contrib.admin.sites import AlreadyRegistered

# Register your models here.
admin.site.register(Items)