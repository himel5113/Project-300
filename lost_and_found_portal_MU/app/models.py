from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

def images(instance, filename):
    return f'uploads/{filename}'

# User Model:
class UserModel(models.Model):

    deptChoice=[
        ('N/A', 'N/A'),
        ('CSE', 'CSE'),
        ('SWE', 'SWE'),
        ('ENG', 'ENG'),
        ('LLB', 'LLB'),
        ('ECO', 'ECO'),
        ('EEE', 'EEE'),
        ('BBA', 'BBA'),
    ]


    name = models.CharField(max_length=50)
    username = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=180, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    mu_id = models.CharField(max_length=11, null=True, blank=True)
    dept = models.CharField(choices=deptChoice, default='N/A', max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    profileImg = models.ImageField(upload_to='profileImg/', null=True, blank=True)
    is_valid = models.BooleanField(default=False)

    
    def __str__(self):
        return self.username


# Lost Item Model:
class Items(models.Model):

    itemsType = [
        ('N/A', 'N/A'),
        ('Found', 'Found'),
        ('Lost', 'Lost'),
    ]


    publisherId = models.CharField(max_length=11, null=True, blank=True)
    publisherUserName = models.CharField(max_length=50, null=True, blank=True)
    publisherName = models.CharField(max_length=50, null=True, blank=True)
    type = models.CharField(choices=itemsType, default='N/A')
    image = models.ImageField(upload_to=images, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

