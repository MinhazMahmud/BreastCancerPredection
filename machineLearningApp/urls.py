from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name="index"), 
    path('homePage',views.home,name="home"),
    path('signInPage/',views.signInPage,name="signInPage"),    
    path('signUpPage/',views.signUpPage,name="signUpPage"),    
    path('historyPage/',views.historyPage,name="historyPage"),
    path('logOutPage/',views.logOutPage,name="logOutPage"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.contact,name="about"),
]
