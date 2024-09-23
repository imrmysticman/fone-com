from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("index",views.index, name = "index"),
    path("products/",views.ListProducts, name = "products"),
    path("product/id",views.ProductDetail,name="productdetails"),
    path("cart",views.Cart,name="cart")
]
