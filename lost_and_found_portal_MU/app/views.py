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
    
    items = Items.objects.all()
    return render(request, 'app/basic/items.html', {'items' : items, 'user' : user})



# Signup view
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password1'])
            if UserModel.objects.filter(email=user.email).exists():
                messages.error(request, 'Email already exists. Try logging in.')
                return redirect('app/authentication/signup.html')
            user.save()

            # create and store username
            fn = user.name.split()[0]
            un = fn + str(user.id)
            user.username = un

            user.save(update_fields=['username'])

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
                
                # fn = user.name.split()[0]
                # un = fn.lower() + str(user.id)
                # request.session['username'] = un
                # messages.success(request, f"Welcome back, {un}!")

                request.session['username'] = user.username
                messages.success(request, f"Welcome back, {user.username}!")
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
        messages.error(request, 'User not found.')
        return redirect('signin')
    

    if request.method == 'POST':
        form = VerificationForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # MU ID from user input
                MU_ID = form.cleaned_data['mu_id']
                # Depertment from user input
                Dept = form.cleaned_data['dept']

                # splitting id to get dept code
                MU_ID_check = MU_ID.split('-')

                # MU dept code
                idCode = MU_ID_check[1]

                if len(MU_ID_check) != 3 or any(len(x) != 3 for x in MU_ID_check):
                    messages.error(request, 'Invalid ID formate. Use XXX-YYY-ZZZ.')
                    return render(request, 'app/authentication/verification.html', {'form' : form})
                
                
                try:
                    user_MuId = user.mu_id
                    user_dept = user.dept
                    user_idCode = user_MuId.split('-')[1]
                except Exception:
                    messages.error(request, 'Your ID is not updated yet. Please update it on your account or contact to the admin.')
                    # ***This will be updated after implementing the user profile feature --- return redirect('user_profile)
                    return redirect('home')
                

                # checking an id is already verified by another user or not
                if UserModel.objects.filter(mu_id = MU_ID, is_valid=True).exclude(id = user.id).exists():
                    messages.error(request, 'This ID already verified by another user. Please enter a valid ID.')
                    return render(request, 'app/authentication/verification.html', {'form' : form})
                

                deptDict = {
                    '115': 'CSE',
                    '114': 'ENG',
                    '113': 'LLB',
                    '116': 'BBA',
                    '134': 'SWE',
                    # '': 'ECO',
                    # '': 'EEE'
                }

                # # Debug
                # print(f'input id = {MU_ID}')
                # print(f'user id = {user.mu_id}')
                # print(f'input dept = {Dept}')
                # print(f'user dept = {user.dept}')
                # print(f'input dept code = {idCode}')
                # print(f'user dept code = {user_idCode}')
                # print(f'dept dict value = {deptDict.get(idCode)}')
                # # end debug


                # Checking depertmentwise code for verification
                if MU_ID == user_MuId and Dept == user.dept and idCode == user_idCode:
                    if idCode in deptDict and Dept == deptDict[idCode]:
                        user.is_valid = True
                        user.save()
                        messages.success(request, 'Verification Successful!')
                        return redirect('itemList')
                else:
                    messages.error(request, 'Verification Failed. Enter your valid id and department.')


            except Exception:
                messages.error(request, 'Credentials missing.')

        else:
            messages.error(request, 'Something went wrong. Try again.')

    else:
        form = VerificationForm()


    return render(request, 'app/authentication/verification.html', {'form' : form})
