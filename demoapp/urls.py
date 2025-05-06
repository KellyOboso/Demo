"""
URL configuration for mydemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('index/', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
    path('allmembers/', views.AllMembers, name='allmembers'),
    path('accounts/', views.accounts, name='accounts'),
    path('contact/', views.contact, name='contact'),
    path('single/', views.single, name='single'),
    path('loans/', views.loans, name='loans'),
    path('', views.LoginPage, name='login'),
    path('register/', views.RegisterPage, name='register'),
    path('settings/', views.settings, name='settings'),
    path('transactions/', views.transactions, name='transactions'),
    path('loginuser/', views.LoginUser, name='loginuser'),  
    path('registeruser/', views.UserRegister, name='registeruser'),  
    path("insertcontact/",views.InsertContact, name="insertcontact"),
    path("allmembers/",views.allmembers, name="allmembers"),
    path("inserttransactions/",views.InsertTransactions, name="inserttransactions"),
]
