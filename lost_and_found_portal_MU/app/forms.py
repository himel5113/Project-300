from django import forms
from .models import Items, UserModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 

class SignupForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = UserModel
        fields = ['name', 'email', 'phone', 'dept', 'mu_id', 'profileImg', 'password1', 'password2']


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = UserModel
#         fields = ['name', 'email', 'dept', 'MU_id', 'phone', 'profileImg']


class VerificationForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['mu_id', 'dept']


class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['type', 'title', 'location', 'description', 'image']
        # fields = ['image', 'title', 'location', 'description']
