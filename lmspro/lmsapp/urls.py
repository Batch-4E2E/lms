from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.home,name = "home"),
    path('accounts/loginn/',views.login),
    path('login/',views.login,name = "login"),
    path('signup',views.signup,name = "signup"),
    path('logout',views.logout_user,name ="logout"),
    path('aftersignup/',views.aftersignup),
    path('after_login',views.after_login,name = "after_login"),
    path('register',views.register),
    path("branch_students/<str:branch>",views.branch_students,name="branch_students"),
    path('aboutus',views.aboutus,name = "aboutus"),
    path('verify',views.verify),
    path('forgot',views.forgot,name = "forgot"),
    path('clear',views.clear),
    path("student_details/<str:rollnumber>",views.branch_students,name="student_details"),
    
]