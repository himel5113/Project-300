from django.shortcuts import render, redirect, get_object_or_404
from .models import Items, UserModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth.hashers import make_password


# Create your views here.
def home(request):
    return render(request, 'app/basic/home.html')



def itemList(request):
    items = Items.objects.all().order_by('-created_at')
    return render(request, 'app/basic/items.html')



# Signup view
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password1'])
            if User.objects.filter(email=user.email).exists():
                messages.error(request, 'Email already exists. Try logging in.')
                return redirect('app/authentication/signup.html')
            user.save()
            messages.success(request, 'Account created successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials. Try Again.')
    else:
        form = UserForm()
    return render(request, 'app/authentication/signup.html', {'form': form})

