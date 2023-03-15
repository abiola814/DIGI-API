from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path("",views.SignupView.as_view(),name="signup"),
    path("login/",views.LoginView.as_view())
]