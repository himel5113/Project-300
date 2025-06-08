from django import forms
from .models import Items
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 

class UserForm(UserCreationForm):
    name = forms.CharField(max_length=30, required=True, help_text='Required. Enter your full name.')
    phone_number = forms.CharField(max_length=15, required=True, help_text='Optional. Enter your phone number.')
    email = forms.EmailField(max_length=50, required=True, help_text='Required. Enter a valid email address.')
    profile_img = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2', 'phone_number', 'profile_img']


class Items(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['publisherId', 'publisherName', 'title', 'description', 'location', 'dateTime', 'image']
