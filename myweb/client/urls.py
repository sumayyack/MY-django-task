from django.urls import path
from client import views

urlpatterns=[
    path("",views.Home.as_view(),name="home"),
    path("accounts/register",views.sign_up,name="register"),
    path("accounts/login",views.sign_in,name="signin"),
    path("accounts/logout",views.sign_out,name="signout")
]