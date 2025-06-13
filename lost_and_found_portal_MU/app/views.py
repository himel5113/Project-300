from django.shortcuts import render, redirect, get_object_or_404
from .models import Items, UserModel
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import SignupForm
from .forms import VerificationForm
# from .forms import UserForm
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.
def home(request):
    return render(request, 'app/basic/home.html')


# Item List

def itemList(request):
    user_id = request.session.get('user_id')
    if not user_id:
        messages.error(request, 'Please Login first.')
    try:
        user = UserModel.objects.get(id=user_id)
    except UserModel.DoesNotExist:
        messages.error(request, 'User not found!')
        return redirect('signin')
    
    items = Items.objects.all().order_by('-created_at')
    return render(request, 'app/basic/items.html', {'items' : items, 'user' : user})



# Signup view
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
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
        form = SignupForm()
    return render(request, 'app/authentication/signup.html', {'form': form})


# Login view
def signin(request):
    if request.method == 'POST':
        email_ = request.POST.get('email')
        password_ = request.POST.get('password')
        try:
            user = UserModel.objects.get(email=email_)
            if check_password(password_, user.password):
                request.session['user_id'] = user.id
                fn = user.name.split()[0]
                un = fn.lower() + str(user.id)
                request.session['username'] = un
                messages.success(request, f"Welcome back, {un}!")
                return redirect('home')
            else :
                messages.error(request, 'Invalid email or password.')
        except UserModel.DoesNotExist:
            messages.error(request, 'User does not exist. Please sign up.')
    return render(request, 'app/authentication/signin.html')



# Logout view
def logout_(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')



# Profile view

# def profile(request):
#     try:
#         user = UserModel.objects.get(email=request.user.email)
#     except UserModel.DoesNotExist:
#         return redirect('signin') 
#     return render(request, 'app/profile.html', {'user': user})



# User verification based on University ID(Depertmentwise)

def verify_user(request):
    user_id = request.session.get('user_id')
    if not user_id:
        messages.error(request, 'Please Login first.')
        return redirect('signin')
    

    try:
        user = UserModel.objects.get(id = user_id)
    except UserModel.DoesNotExist:
        messages.error(request, 'User not found. Please Login.')
        return redirect('signin')

    if request.method == 'POST':
        form = VerificationForm(request.POST, request.FILES)
        if form.is_valid():
            MU_ID = form.cleaned_data['mu_id']
            MU_ID_check = form.cleaned_data['mu_id'].split('-')[1]
            # print(f'id check : {MU_ID}')
            Dept = form.cleaned_data['dept']

            # mu_id from user
            user_mu_id = user.mu_id.split('-')[1]
            # print(f'id check from UserModel : {MU_ID}')

            # checking an id is already verified by another user or not
            if UserModel.objects.filter(mu_id = MU_ID, completed = True).exclude(id=user.id).exists():
                messages.error(request, 'This University ID is already verified by anothe user. Enter a valid ID.')
                return redirect('verify_user')
            

            if MU_ID == user.mu_id and MU_ID_check == user_mu_id and Dept == user.dept:
                if MU_ID_check == '115' and Dept == 'CSE':
                    user.completed = True
                    user.save()
                    messages.success(request, 'Verification Successful!')
                    return redirect('itemList')
                else:
                    messages.error(request, 'Verification Failed.')
            else:
                messages.error(request, 'Invalid Credentials.')
    else:
        form = VerificationForm()

    return render(request, 'app/authentication/verification.html', {'form' : form})