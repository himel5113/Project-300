from django.contrib import admin
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('item/', views.itemList, name = "itemList"),
    path('signup/', views.signup, name = 'signup'),
]    
