from django.contrib import admin
from django.urls import path, include

from schoolapp import views
app_name='schoolapp'
urlpatterns = [

    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('newpage',views.newpage,name='newpage'),
    path('form',views.form,name='form'),
    path('onclick',views.onclick,name='onclick'),
]