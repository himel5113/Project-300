from django.db import models
from datetime import datetime

def images(instance, filename):
    return f'uploads/{filename}'

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

