from django import forms
from .models import Items, UserModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 

class UserForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = UserModel
        fields = ['name', 'email', 'password1', 'password2']


class Items(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['publisherId', 'publisherName', 'title', 'description', 'location', 'dateTime', 'image']
