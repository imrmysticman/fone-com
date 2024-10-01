from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path("cart/",views.Cart,name="cart"),
    path("addtocart",views.AddToCart,name="addtocart")

]