from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

def images(instance, filename):
    return f'uploads/{filename}'

# User Model:
class UserModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    MU_id = models.CharField(max_length=11, unique=True, null=True, blank=True)
    dept = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    profileImg = models.ImageField(upload_to='profileImg/', null=True, blank=True)
    completed = models.BooleanField(default=False)

    
    


# Lost Item Model:
class Items(models.Model):
    publisherId = models.CharField(max_length=11)
    publisherName = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    dateTime = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to=images, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

