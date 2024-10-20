from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path("account",views.Account,name="account"),
    path("logout",views.Logout,name="logout"),
    path("profile",views.Profile,name="profile"),
    path("address",views.Address,name="address")
]