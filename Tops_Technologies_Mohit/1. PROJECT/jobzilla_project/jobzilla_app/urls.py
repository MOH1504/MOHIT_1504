"""jobzilla_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views

urlpatterns = [
    
     path('', views.home, name='home'),
     path('login/', views.login, name="login"),
     path('c-register/', views.c_register, name="c-register"),
     path('c-register/', views.c_register, name="c-register"),
     path('companies/',views.companies_panel,name="companies"),
     path('user-profile/',views.user_profile,name="user-profile"),
     path('logout/',views.logout,name="logout"),
    
     path('change-profile-js/',views.change_profile_js,name="change-profile-js"),
     path('change-account-js/',views.change_account_js,name="change-account-js"),
     path('change-password-js/',views.change_password_js,name="change-password-js"),
     path('user-profile-jp/',views.user_profile_jp,name="user-profile-jp"),
     path('change-profile-jp/',views.change_profile_jp,name="change-profile-jp"),
     path('change-account-jp/',views.change_account_jp,name="change-account-jp"),
     path('change-password-jp/',views.change_password_jp,name="change-password-jp"),
     path('job-apply/<int:id>/',views.job_apply,name="job-apply"),
     path('forgot-password/',views.forgot_password,name="forgot-password"),
     path('change-password/',views.change_password,name="change-password")

]


