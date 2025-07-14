from django.shortcuts import render, redirect, get_object_or_404

# Models
from .models import Items, UserModel, Backup, NotificationModel


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods

# Forms
from .forms import SignupForm
# from .forms import VerificationForm
from .forms import ItemForm


from django.contrib.auth.hashers import make_password, check_password


from django.core.mail import send_mail
from django.conf import settings
import textwrap
from django.db.models import Q


# Create your views here.


# homepage view
def home(request):
    return render(request, 'app/basic/home.html')



# Signup view
def signup(request):
    if request.method == 'POST':

        if UserModel.objects.filter(email=request.POST.get('email')).exists():
                messages.error(request, 'Email already exists. Try logging in.')
                return redirect('signup')
            
        if UserModel.objects.filter(mu_id = request.POST.get('mu_id')).exists():
            messages.error(request, 'This ID already exists.')
            return redirect('signup')
        

        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password1'])
            try:
                muID = form.cleaned_data['mu_id'].split('-')
                dept = form.cleaned_data['dept']

            # DEBUG
                # print(f'DEBUG: MU_ID = {MU_ID}')

            # checking id format
            # MU_ID should be in the format of XXX-YYY-ZZZ
                if len(muID) != 3 or any(len(x) != 3 for x in muID):
                    messages.error(request, 'Invalid ID format. Use XXX-YYY-ZZZ.')
                    return render(request, 'app/authentication/signup.html', {'form' : form})

                temp = muID[1]
                idCode = ['115', '114', '113', '116', '134', '111', '141']
                checkDict = {
                    '115': 'CSE',
                    '114': 'ENG',
                    '113': 'LLB',
                    '116': 'BBA',
                    '134': 'SWE',
                    '111': 'ECO',
                    '141': 'EEE'
                }

                if temp not in idCode or dept != checkDict[temp]:
                        messages.error(request, 'Invalid ID. Enter a valid ID and Department.')
                        return render(request, 'app/authentication/signup.html', {'form' : form})
            except Exception as e:
                messages.error(request, 'Credentials missing.')
                return render(request, 'app/authentication/signup.html', {'form' : form})

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
                messages.success(request, f"Welcome, {user.username}!")
                return redirect('home')
            else :
                messages.error(request, 'Invalid email or password.')
        except UserModel.DoesNotExist:
            messages.error(request, 'User does not exist. Please sign up.')
    return render(request, 'app/authentication/signin.html')



# Logout view
def logout_(request):
    request.session.flush() # Clear the session data
    messages.success(request, 'Logged out successfully!')
    return redirect('home')



# Profile view
# Development Phase
def profile_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
        messages.error(request, 'Please Login first.')
        return redirect('signin')

    user = UserModel.objects.get(id=user_id)
    return render(request, 'app/user/profile.html', {'user' : user})



# # User verification based on University ID(Depertmentwise)---implemented in signup process
# def verify_user(request):
#     user_id = request.session.get('user_id')
#     if not user_id:
#         messages.error(request, 'Please Login first.')
#         return redirect('signin')
    
#     # to prevent error after clicking the items button
#     try:
#         user = UserModel.objects.get(id = user_id)
#     except UserModel.DoesNotExist:
#         messages.error(request, 'User not found.')
#         return redirect('signin')
    

#     if request.method == 'POST':
#         form = VerificationForm(request.POST, request.FILES)
#         if form.is_valid():
#             try:
#                 # MU ID from user input
#                 MU_ID = form.cleaned_data['mu_id']
#                 # Depertment from user input
#                 Dept = form.cleaned_data['dept']

#                 # splitting id to get dept code
#                 MU_ID_check = MU_ID.split('-')


#                 # checking id format
#                 # MU_ID should be in the format of XXX-YYY-ZZZ
#                 if len(MU_ID_check) != 3 or any(len(x) != 3 for x in MU_ID_check):
#                     messages.error(request, 'Invalid ID formate. Use XXX-YYY-ZZZ.')
#                     return render(request, 'app/authentication/verification.html', {'form' : form})

#                 # MU dept code
#                 idCode = MU_ID_check[1]

                
                
                
#                 try:
#                     user_MuId = user.mu_id
#                     user_dept = user.dept
#                     user_idCode = user_MuId.split('-')[1]
#                 except Exception:
#                     messages.error(request, 'Your ID is not updated yet. Please update it on your account or contact to the admin.')
#                     # ***This will be updated after implementing the user profile feature --- return redirect('user_profile)
#                     return redirect('home')
                

#                 # checking an id is already verified by another user or not
#                 if UserModel.objects.filter(mu_id = MU_ID, is_valid=True).exclude(id = user.id).exists():
#                     messages.error(request, 'This ID already verified by another user. Please enter a valid ID.')
#                     return render(request, 'app/authentication/verification.html', {'form' : form})
                

#                 deptDict = {
#                     '115': 'CSE',
#                     '114': 'ENG',
#                     '113': 'LLB',
#                     '116': 'BBA',
#                     '134': 'SWE',
#                     # '': 'ECO',
#                     # '': 'EEE'
#                 }

#                 # # Debug
#                 # print(f'input id = {MU_ID}')
#                 # print(f'user id = {user.mu_id}')
#                 # print(f'input dept = {Dept}')
#                 # print(f'user dept = {user.dept}')
#                 # print(f'input dept code = {idCode}')
#                 # print(f'user dept code = {user_idCode}')
#                 # print(f'dept dict value = {deptDict.get(idCode)}')
#                 # # end debug


#                 # Checking depertmentwise code for verification
#                 if MU_ID == user_MuId and Dept == user.dept and idCode == user_idCode:
#                     if idCode in deptDict and Dept == deptDict[idCode]:
#                         user.is_valid = True
#                         user.save()
#                         messages.success(request, 'Verification Successful!')
#                         return redirect('itemPage')
#                 else:
#                     messages.error(request, 'Verification Failed. Enter your valid id and department.')


#             except Exception as e:
#                 # Debug
#                 # print(f'DEBUG ERROR: {e}')
#                 # end debug
#                 messages.error(request, 'Credentials missing.')

#         else:
#             messages.error(request, 'Something went wrong. Try again.')

#     else:
#         form = VerificationForm()


#     return render(request, 'app/authentication/verification.html', {'form' : form})






# Posted Item List

def itemPage(request):
    user_id = request.session.get('user_id')
    if not user_id:
        messages.error(request, 'Please Login first.')

    # to prevent error after clicking the items button
    try:
        user = UserModel.objects.get(id=user_id)
    except UserModel.DoesNotExist:
        messages.error(request, 'User not found!')
        return redirect('signin')
    
    
    found_items = Items.objects.filter(type='Found').order_by('-created_at')

    lost_items = Items.objects.filter(type='Lost').order_by('-created_at')

    return render(request, 'app/basic/items.html', {'user' : user, 'found_items': found_items, 'lost_items': lost_items})





# found item
def found_items_view(request):

    user = None

    try:
        loggedin_user_id = request.session.get('user_id')
        if loggedin_user_id:
            user = UserModel.objects.get(id = loggedin_user_id)
    except UserModel.DoesNotExist:
        user = None

    items = Items.objects.filter(type='Found').order_by('-created_at')
    ids = []
    for item in items:
        ids.append(item.publisherId)

    # Debug
    # print('ID: ')
    # for i in ids:
    #     print(i)


    publishers = UserModel.objects.filter(mu_id__in = ids)
    # for p in publishers:
    #     print(f'PublisherName = {p.name} \n PublisherId = {p.id} \n PublisherUserName = {p.username} \n PublisherDept = {p.dept} \n PublisherEmail = {p.email}')


    publisherDict = {}
    for p in publishers:
        publisherDict[p.mu_id] = p


    # added publisher info to item
    for item in items:
        item.publisherInfo = publisherDict.get(item.publisherId)


        #   # debug
        # if item.publisherInfo:
        #     print('----------')
        #     print(item.publisherInfo.name)
        #     print(item.publisherInfo.username)
        #     print(item.publisherInfo.id)
        #     print(item.publisherInfo.dept)
        #     print(item.publisherInfo.mu_id)
        # else :
        #     print('User not found!')
        # print('----------')

        # loggedin_user_id = request.session.get('user_id')
        # user = UserModel.objects.get(id = loggedin_user_id)


    return render(request, 'app/basic/found_items.html', {'items' : items, 'user' : user})





# lost item
def lost_items_view(request):

    user = None

    try:
        loggedin_user_id = request.session.get('user_id')
        if loggedin_user_id:
            user = UserModel.objects.get(id = loggedin_user_id)
    except UserModel.DoesNotExist:
        user = None

    items = Items.objects.filter(type='Lost').order_by('-created_at')
    ids = []
    for item in items:
        ids.append(item.publisherId)

    # Debug
    # print('ID: ')
    # for i in ids:
    #     print(i)


    publishers = UserModel.objects.filter(mu_id__in = ids)
    # for p in publishers:
    #     print(f'PublisherName = {p.name} \n PublisherId = {p.id} \n PublisherUserName = {p.username} \n PublisherDept = {p.dept} \n PublisherEmail = {p.email}')


    publisherDict = {}
    for p in publishers:
        publisherDict[p.mu_id] = p


    # added publisher info to item
    for item in items:
        item.publisherInfo = publisherDict.get(item.publisherId)


        #   # debug
        # if item.publisherInfo:
        #     print('----------')
        #     print(item.publisherInfo.name)
        #     print(item.publisherInfo.username)
        #     print(item.publisherInfo.id)
        #     print(item.publisherInfo.dept)
        #     print(item.publisherInfo.mu_id)
        # else :
        #     print('User not found!')
        # print('----------')



    return render(request, 'app/basic/lost_items.html', {'items' : items, 'user':user})





# Create Post

def create_post(request):
    user_id = request.session.get('user_id')
    user = UserModel.objects.get(id = user_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.publisherId = user.mu_id
            item.publisherName = user.name
            item.publisherUserName = user.username

            item.save()
            messages.success(request, 'Successfuly Posted!')
            if item.type == 'Found':
                return redirect('found_items_view')
            else:
                return redirect('lost_items_view')
    else:
        form = ItemForm()
    return render(request, 'app/basic/create_post.html', {'form' : form})



# Edit Post

def edit_post_view(request, item_id):
    user = get_object_or_404(UserModel, id = request.session.get('user_id'))
    item = get_object_or_404(Items, id = item_id)


    if item.publisherId != user.mu_id:
        messages.error(request, 'You are not authorized to edit this post.')
        return redirect('itemPage')
    
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            if item.type == 'Found':
                return redirect('found_items_view')
            else:
                return redirect('lost_items_view')
        else:
            messages.error(request, 'Something went wrong. Try again later.')
    else:
        form = ItemForm(instance=item)
    return render(request, 'app/basic/edit_post.html', {'form' : form, 'item' : item})



# Delete and Backup post
@require_http_methods(["GET"])
def delete_and_backup_post(request, item_id):
    item = get_object_or_404(Items, id = item_id)
    
    # Abstract (only for admin)
    backup = Backup.objects.create(
        original_item_id=item.id,
        original_publisherId=item.publisherId,
        original_publisherUserName=item.publisherUserName,
        original_publisherName=item.publisherName,
        original_itemType=item.type,
        original_image=item.image,
        original_title=item.title,
        original_description=item.description,
        original_location=item.location,
    )
    backup.save()


    temp = item.type

    item.delete()
    messages.success(request, 'Post deleted successfully!')
    if temp == 'Found':
        return redirect('found_items_view')
    else:
        return redirect('lost_items_view')
    



# Details post view
def details_post_view(request, item_id):
    item = get_object_or_404(Items, id=item_id)
    user = UserModel.objects.get(mu_id=item.publisherId)
    return render(request, 'app/basic/details.html', {'item': item, 'user': user})




# send claim request

def claim_request(request, item_id):
    item = get_object_or_404(Items, id=item_id)
    claimer = get_object_or_404(UserModel, id=request.session.get('user_id'))
    publisher = get_object_or_404(UserModel, mu_id=item.publisherId)

    subject = f"Claim Request for Item: {item.title}"
    message = textwrap.dedent(f"""
    Dear {publisher.name},

    {claimer.name} (email: {claimer.email}) has requested to claim the item you posted.

    Item Details:
    Item Title: {item.title}
    Location: {item.location}
    Description: {item.description}

    Please contact the claimer directly.

    Here's the claimer details:
    Name: {claimer.name}
    Email: {claimer.email}
    Department: {claimer.dept}
    University ID: {claimer.mu_id}
    Phone: {claimer.phone}

    With best regards,
    Lost & Found Team
    """)

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [publisher.email],
        fail_silently=False
    )


    recipient = publisher.name
    sender = claimer.name
    message = f"{sender} wants to claim your item: {item.title}"

    NotificationModel.objects.create(
        recipient=recipient,
        recipient_muID=publisher.mu_id,
        sender=sender,
        sender_muID=claimer.mu_id,
        item=item,
        message=message,
        type='claim_request'
    )


    messages.success(request, 'Claim request sent successfully!')
    return redirect('found_items_view') 



# Found notification

def found_notification(request, item_id): 
    item = get_object_or_404(Items, id=item_id)
    finder = get_object_or_404(UserModel, id=request.session.get('user_id'))
    publisher = get_object_or_404(UserModel, mu_id=item.publisherId)

    subject = f"Found Notification for Item: {item.title}"
    message = textwrap.dedent(f"""
        Dear {publisher.name},

        {finder.name} (email: {finder.email}) has reported that they found the item you posted.

        Item Details:
        Title: {item.title}
        Location Found: {item.location}
        Description: {item.description}

        Please get in touch with the finder to arrange the return of your item.

        Here's the finder details:
        Name: {finder.name}
        Email: {finder.email}
        Department: {finder.dept}
        University ID: {finder.mu_id}
        Phone: {finder.phone}

        Best regards,
        Lost & Found Team
        """)

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [publisher.email],
        fail_silently=False
    )

    recipient = publisher.name
    sender = finder.name
    message = f"{sender} wants to claim your item: {item.title}"

    NotificationModel.objects.create(
        recipient=recipient,
        recipient_muID=publisher.mu_id,
        sender=sender,
        sender_muID=finder.mu_id,
        item=item,
        message=message,
        type='found_notification'
    )

    messages.success(request, 'Found notification sent successfully!')
    return redirect('lost_items_view')



# Notification view
def notification_view(request):
    user_id = request.session.get('user_id')
    user = UserModel.objects.get(id=user_id) if user_id else None
    # print(f'User ID: {user.mu_id}')  # Debugging line
    # print(f'User ID: {user.mu_id}')  # Debugging line
    notifications = NotificationModel.objects.filter(recipient_muID=user.mu_id)
    return render(request, 'app/basic/notification.html', {'notifications': notifications})



# accept request

@require_http_methods(["GET"])
def accept_request(request, notification_id, item_id):

    item = get_object_or_404(Items, id=item_id)
    sender = get_object_or_404(UserModel, id=request.session.get('user_id'))
    reciever = get_object_or_404(UserModel, mu_id=item.publisherId)

    notification = NotificationModel.objects.get(
        Q(id=notification_id) & (Q(status='Pending') | Q(status='Reject'))
    )


    
    # Abstract (only for admin)
    backup = Backup.objects.create(
        original_item_id=item.id,
        original_publisherId=item.publisherId,
        original_publisherUserName=item.publisherUserName,
        original_publisherName=item.publisherName,
        original_itemType=item.type,
        original_image=item.image,
        original_title=item.title,
        original_description=item.description,
        original_location=item.location,
        recipient=reciever.name,
        recipient_muID=reciever.mu_id,
        sender=sender.name,
        sender_muID=sender.mu_id
    )
    backup.save()
    
    

    notification.status = 'Accept'
    notification.save()


    temp = item.type

    item.delete()
    messages.success(request, 'Request Accepted!')
    return redirect('notification_view')



# reject reqiest
@require_http_methods(["GET"])
def reject_request(request, notification_id, item_id):
    item = get_object_or_404(Items, id=item_id)
    sender = get_object_or_404(UserModel, id=request.session.get('user_id'))
    reciever = get_object_or_404(UserModel, mu_id=item.publisherId)

    notification = NotificationModel.objects.get(
        Q(id=notification_id) & (Q(status='Pending') | Q(status='Reject'))
    )


    notification.status='Reject'
    notification.save()

    messages.success(request, 'Request Rejected. If any query please contact to the admin.')
    return redirect('notification_view')