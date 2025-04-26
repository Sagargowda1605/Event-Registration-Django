#from django.contrib import admin
from django.urls import path
from .views import home_page,event_details,event_confirmation,user_login,user_register,user_logout,user_profile

urlpatterns = [
    path('', home_page,name='Home'),
    path('event/<str:pk>',event_details,name='event'),
    path('confrimation/<str:pk>',event_confirmation,name='confirmation'),
    path('login/',user_login,name="login_user"),
    path('regsiter/',user_register,name="user_register"),
    path('logout/',user_logout,name="user_logout"),
    path('profile/<str:pk>',user_profile,name="user_profile")
]