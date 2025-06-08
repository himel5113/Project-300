from django.shortcuts import render, redirect, get_object_or_404
from .models import Items
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserForm


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
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('home')
    else :
        form = UserForm()
    return render(request, 'app/authentication/signup.html', {'form': form})
