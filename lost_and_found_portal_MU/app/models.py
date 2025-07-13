from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

def images(instance, filename):
    return f'uploads/{filename}'

# User Model:
class UserModel(models.Model):

    deptChoice=[
        ('Select Department', 'Select Department'),
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
    dept = models.CharField(choices=deptChoice, default='Select Department')
    created_at = models.DateTimeField(auto_now_add=True)
    profileImg = models.ImageField(upload_to='profileImg/', null=True, blank=True)
    # is_valid = models.BooleanField(default=False)   

    
    def __str__(self):
        return self.username


# Lost Item Model:
class Items(models.Model):

    itemsType = [
        ('Select post type', 'Select post type'),
        ('Found', 'Found'),
        ('Lost', 'Lost'),
    ]


    publisherId = models.CharField(max_length=11, null=True, blank=True)
    publisherUserName = models.CharField(max_length=50, null=True, blank=True)
    publisherName = models.CharField(max_length=50, null=True, blank=True)
    type = models.CharField(choices=itemsType, default='Select post type')
    image = models.ImageField(upload_to=images, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    


# Backup Deleted Items Model:
class Backup(models.Model):
    itemsType = [
        ('Select post type', 'Select post type'),
        ('Found', 'Found'),
        ('Lost', 'Lost'),
    ]

    original_item_id = models.IntegerField(null = True, blank = True)
    original_publisherId = models.CharField(max_length=11, null=True, blank=True)
    original_publisherUserName = models.CharField(max_length=50, null=True, blank=True)
    original_publisherName = models.CharField(max_length=50, null=True, blank=True)
    original_itemType = models.CharField(choices=itemsType, default='N/A')
    original_image = models.ImageField(upload_to=images, null=True, blank=True)
    original_title = models.CharField(max_length=100)
    original_description = models.TextField()
    original_location = models.CharField(max_length=100)
    deleted_at = models.DateTimeField(auto_now_add=True)




# Notification Model:
class NotificationModel(models.Model):

    types = [
        ('default', 'default'),
        ('claim_request', 'claim_request'),
        ('found_notification', 'found_notification'),
    ]


    statusChoice = [
        ('Pending', 'Pending'),
        ('Accept', 'Accept'),
        ('Reject', 'Reject'),
    ]

    recipient = models.CharField(max_length=50, null=True, blank=True)
    recipient_muID = models.CharField(max_length=11, null=True, blank=True)
    sender = models.CharField(max_length=50, null=True, blank=True)
    sender_muID = models.CharField(max_length=11, null=True, blank=True)
    item = models.ForeignKey(Items, on_delete=models.SET_NULL, null=True, blank=True)
    message = models.TextField()
    type = models.CharField(choices=types, default='default')
    status = models.CharField(choices=statusChoice, default='Pending')

    # def __str__(self):
    #     return f'Notification for {self.item.title}'

