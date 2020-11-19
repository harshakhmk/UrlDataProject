from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('user/SignUp',views.SignUp,name="SignUp"),
    path('user/Signin',views.Signin,name="Signin"),
    path('user/Signout',views.Signout,name="Signout"),
    path('',views.HomePage,name="Homepage"),
    path('',views.HomePage,name="Homepage"),
]
