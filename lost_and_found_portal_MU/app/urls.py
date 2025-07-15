from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('item/', views.itemPage, name = "itemPage"),
    path('signup/', views.signup, name = 'signup'),
    path('signin/', views.signin, name = 'signin'),
    path('logout/', views.logout_, name = 'logout_'),
    path('user-profile/', views.profile_view, name = 'profile_view'),
    # path('verify-user/', views.verify_user, name = 'verify_user'),
    path('create-post/', views.create_post, name = 'create_post'),
    path('found-item/', views.found_items_view, name = 'found_items_view'),
    path('lost-item/', views.lost_items_view, name = 'lost_items_view'),
    path('edit-post/<int:item_id>', views.edit_post_view, name = 'edit_post_view'),
    path('delete-post/<int:item_id>', views.delete_and_backup_post, name = 'delete_and_backup_post'),
    # path('backup/<int:item_id>', views.backup_items, name = 'backup_items'),
    path('details-post/<int:item_id>', views.details_post_view, name = 'details_post_view'),
    path('claim-request/<int:item_id>', views.claim_request, name = 'claim_request'),
    path('found-notification/<int:item_id>', views.found_notification, name = 'found_notification'),
    path('notifications/', views.notification_view, name='notification_view'),
    path('accept_request/<int:notification_id>/<int:item_id>', views.accept_request, name='accept_request'),
    path('reject_request/<int:notification_id>/<int:item_id>', views.reject_request, name='reject_request'),
    path('clear_all/', views.clear_all, name='clear_all'),
]    
