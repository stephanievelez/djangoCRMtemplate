from django.contrib import admin
from django.urls import path

from mycrm import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.Register_user, name='register'),
]