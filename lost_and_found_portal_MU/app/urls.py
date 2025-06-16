from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('item/', views.itemList, name = "itemList"),
    path('signup/', views.signup, name = 'signup'),
    path('signin/', views.signin, name = 'signin'),
    path('logout/', views.logout_, name = 'logout_'),
    path('verify/', views.verify_user, name = 'verify_user'),
    path('create/', views.create_post, name = 'create_post'),
    path('found/', views.found_items_view, name = 'found_items_view'),
    path('lost/', views.lost_items_view, name = 'lost_items_view'),
]    
