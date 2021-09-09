from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('home' ,  home  , name="home"),
     path('' ,  index  , name="index"),
    path('register' , register_attempt , name="register_attempt"),
    path('accounts/login/' , login_attempt , name="login_attempt"),
    path('token' , token_send , name="token_send"),
    path('success' , success , name='success'),
    path('verify/<auth_token>' , verify , name="verify"),
    path('logout_view' , logout_view , name='logout'),

    #path('error' , error_page , name="error")

    
   
]
