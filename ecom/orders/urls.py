from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path("cart/",views.Cart,name="cart"),
    path("addtocart",views.AddToCart,name="addtocart"),
    path("removeproduct",views.removeProduct,name="removeproduct"),
    path("checkout",views.checkout,name="checkout"),
    path("cancelorder/<int:id>",views.cancelOrder,name="cancel"),


]